"""Migration tests.

The thing being tested is a move between two environments, so the tests build
two sandboxes: one standing in for the container being abandoned, one for the
fresh clone. The second gets `data/` copied into it directly, which is what a
`git clone` does, and gets its documents only from the bundle.
"""

from __future__ import annotations

import json
import shutil
import unittest
from pathlib import Path

from pipelines import migrate
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

PDF = b"%PDF-1.4\nnot really a pdf, but bytes are bytes\n"


def _write(path: Path, data: bytes | str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        path.write_text(data, encoding="utf-8")
    else:
        path.write_bytes(data)


def _archive(sandbox: Sandbox):
    """A small but complete archive: two documents, abstracts, logs, an inbox."""
    cfg = sandbox.config()
    root = cfg.layout.root
    store = RecordStore(cfg.layout)

    _write(root / "data/pdfs/hand-filed.pdf", PDF + b"hand")
    store.save_paper(
        Paper(
            id="local:abc",
            title="A Paper Somebody Filed",
            source="local",
            local_path="data/pdfs/hand-filed.pdf",
        )
    )

    _write(root / "data/pdfs/read/fetched.pdf", PDF + b"fetched")
    store.save_paper(
        Paper(
            id="arxiv:2401.00001",
            title="A Paper A Collector Found",
            source="arxiv",
            pdf_url="https://arxiv.org/pdf/2401.00001",
            local_path="data/pdfs/read/fetched.pdf",
        )
    )

    # On disk, but nothing points at it: provenance unknown.
    _write(root / "data/pdfs/orphan.pdf", PDF + b"orphan")

    _write(root / "data/abstracts/cs.LG/2026-08-01.jsonl", '{"id": "1"}\n')
    _write(root / "data/logs/2026-08-01.log", "INFO run complete\n")
    _write(root / "data/raw/2026-08-01/arxiv.json", "[]\n")
    _write(root / "inbox/waiting.pdf", PDF + b"waiting")
    _write(root / "inbox/README.md", "drop PDFs here\n")
    return cfg


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = _archive(self.sandbox)
        self.plan = migrate.build_plan(self.cfg, RecordStore(self.cfg.layout))
        self.tier = {item.path: item.tier for item in self.plan.items}

    def test_a_hand_filed_document_is_irreplaceable(self):
        """No URL was ever recorded for it. Losing it loses the document."""
        self.assertEqual(self.tier["data/pdfs/hand-filed.pdf"], "irreplaceable")

    def test_a_fetched_document_is_refetchable(self):
        self.assertEqual(self.tier["data/pdfs/read/fetched.pdf"], "refetchable")

    def test_a_document_no_record_claims_is_treated_as_irreplaceable(self):
        """Unknown provenance cannot be shown to be re-fetchable."""
        self.assertEqual(self.tier["data/pdfs/orphan.pdf"], "irreplaceable")

    def test_an_undrained_inbox_travels(self):
        self.assertEqual(self.tier["inbox/waiting.pdf"], "irreplaceable")

    def test_abstracts_are_refetchable_and_logs_are_disposable(self):
        self.assertEqual(self.tier["data/abstracts/cs.LG/2026-08-01.jsonl"], "refetchable")
        self.assertEqual(self.tier["data/logs/2026-08-01.log"], "disposable")
        self.assertEqual(self.tier["data/raw/2026-08-01/arxiv.json"], "disposable")

    def test_a_tracked_file_in_the_inbox_is_skipped_and_said_so(self):
        self.assertNotIn("inbox/README.md", self.tier)
        self.assertIn(
            "inbox/README.md", [entry["path"] for entry in self.plan.skipped]
        )


class PackTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = _archive(self.sandbox)
        self.dest = self.cfg.layout.root / "migration"

    def test_every_file_is_carried_and_none_is_sampled(self):
        manifest = migrate.pack(self.cfg, self.dest)
        packed = {entry["path"] for entry in manifest["files"]}
        plan = migrate.build_plan(self.cfg, RecordStore(self.cfg.layout))
        self.assertEqual(packed, {item.path for item in plan.items})
        self.assertTrue(migrate.verify(self.dest)["ok"])

    def test_a_narrower_tier_names_what_it_left_behind(self):
        manifest = migrate.pack(self.cfg, self.dest, tier="irreplaceable")
        packed = {entry["path"] for entry in manifest["files"]}
        self.assertEqual(
            packed,
            {"data/pdfs/hand-filed.pdf", "data/pdfs/orphan.pdf", "inbox/waiting.pdf"},
        )
        skipped = {entry["path"] for entry in manifest["skipped"]}
        self.assertIn("data/pdfs/read/fetched.pdf", skipped)
        self.assertIn("data/logs/2026-08-01.log", skipped)

    def test_verify_catches_a_truncated_transfer(self):
        migrate.pack(self.cfg, self.dest)
        (self.dest / "payload/data/pdfs/hand-filed.pdf").unlink()
        result = migrate.verify(self.dest)
        self.assertFalse(result["ok"])
        self.assertEqual(result["missing"], ["data/pdfs/hand-filed.pdf"])

    def test_verify_catches_a_corrupted_file(self):
        migrate.pack(self.cfg, self.dest)
        target = self.dest / "payload/data/pdfs/hand-filed.pdf"
        target.unlink()  # break the hard link rather than editing the original
        target.write_bytes(PDF + b"tampered")
        result = migrate.verify(self.dest)
        self.assertFalse(result["ok"])
        self.assertEqual(result["corrupt"], ["data/pdfs/hand-filed.pdf"])

    def test_packing_does_not_disturb_the_originals(self):
        migrate.pack(self.cfg, self.dest)
        self.assertTrue((self.cfg.layout.root / "data/pdfs/hand-filed.pdf").exists())

    def test_move_is_opt_in_and_empties_the_source(self):
        migrate.pack(self.cfg, self.dest, move=True)
        self.assertFalse((self.cfg.layout.root / "data/pdfs/hand-filed.pdf").exists())
        self.assertTrue(migrate.verify(self.dest)["ok"])

    def test_the_manifest_records_what_git_is_carrying(self):
        manifest = migrate.pack(self.cfg, self.dest)
        self.assertEqual(manifest["records"]["papers"], 2)
        self.assertEqual(manifest["records"]["papers_with_document"], 2)

    def test_an_unpushed_checkout_is_a_warning_not_a_silent_pass(self):
        """The expensive failure is a discarded container, not a dropped PDF."""
        manifest = migrate.pack(self.cfg, self.dest)
        self.assertTrue(manifest["git_warnings"])


class RoundTripTests(unittest.TestCase):
    """Pack from one checkout, restore into another that only got `data/`."""

    def setUp(self):
        self.source = Sandbox()
        self.addCleanup(self.source.close)
        self.destination = Sandbox()
        self.addCleanup(self.destination.close)

        self.source_cfg = _archive(self.source)
        self.bundle = self.source_cfg.layout.root / "migration"
        migrate.pack(self.source_cfg, self.bundle)

        # What `git clone` delivers: the records, and nothing gitignored.
        self.dest_cfg = self.destination.config()
        shutil.copytree(
            self.source_cfg.layout.papers,
            self.dest_cfg.layout.papers,
            dirs_exist_ok=True,
        )

    def test_a_fresh_clone_has_records_pointing_at_documents_it_lacks(self):
        before = migrate.check_documents(self.dest_cfg)
        self.assertEqual(before["expected"], 2)
        self.assertEqual(before["missing"], 2)

    def test_unpacking_makes_every_claimed_document_present(self):
        result = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertEqual(result["missing_from_bundle"], [])
        self.assertEqual(result["checksum_failed"], [])
        self.assertEqual(result["documents"]["missing"], 0)

    def test_the_restored_bytes_are_the_original_bytes(self):
        migrate.unpack(self.dest_cfg, self.bundle)
        restored = self.dest_cfg.layout.root / "data/pdfs/hand-filed.pdf"
        self.assertEqual(restored.read_bytes(), PDF + b"hand")

    def test_a_dry_run_restores_nothing(self):
        result = migrate.unpack(self.dest_cfg, self.bundle, dry_run=True)
        self.assertEqual(result["restored"], 7)
        self.assertFalse(
            (self.dest_cfg.layout.root / "data/pdfs/hand-filed.pdf").exists()
        )

    def test_a_record_count_that_differs_is_reported_as_a_git_problem(self):
        """The bundle cannot carry records, so a mismatch is never its fault."""
        (self.dest_cfg.layout.papers / "local-abc.json").unlink()
        result = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertIn("papers", result["records"]["differences"])

    def test_an_irreplaceable_only_bundle_leaves_the_refetchable_gap_visible(self):
        narrow = self.source_cfg.layout.root / "narrow"
        migrate.pack(self.source_cfg, narrow, tier="irreplaceable")
        migrate.unpack(self.dest_cfg, narrow)
        documents = migrate.check_documents(self.dest_cfg)
        self.assertEqual(documents["missing"], 1)
        self.assertIn("arxiv:2401.00001", documents["examples"][0])


class ManifestTests(unittest.TestCase):
    def test_the_manifest_is_readable_json_with_a_checksum_per_file(self):
        sandbox = Sandbox()
        self.addCleanup(sandbox.close)
        cfg = _archive(sandbox)
        dest = cfg.layout.root / "migration"
        migrate.pack(cfg, dest)
        manifest = json.loads((dest / "MANIFEST.json").read_text(encoding="utf-8"))
        self.assertTrue(all(entry["sha256"] for entry in manifest["files"]))
        self.assertEqual(
            sorted(manifest["totals"]), ["disposable", "irreplaceable", "refetchable"]
        )


if __name__ == "__main__":
    unittest.main()
