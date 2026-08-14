"""Migration tests.

The thing being tested is a move between two environments, so the tests build
two sandboxes: one standing in for the container being abandoned, one for the
fresh clone. The second gets `data/` copied into it directly, which is what a
`git clone` does, and gets its documents only from the bundle.
"""

from __future__ import annotations

import hashlib
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


class OrphanReportTests(unittest.TestCase):
    """A document nobody claims is otherwise invisible.

    `shelve_documents` files documents *by record*, so it never visits one; the
    day's digest counts what was collected, not what is on disk. And they are
    not inert: `build_plan` cannot establish provenance for a file nobody
    claims, so it tiers it `irreplaceable` — inflating the one number that
    decides how large a bundle has to be.

    The defect that produced them was found by reading code. This is what would
    have found it by running something.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = _archive(self.sandbox)
        self.documents = migrate.check_documents(self.cfg)

    def test_an_unclaimed_document_is_counted_and_named(self):
        self.assertEqual(self.documents["orphaned"], 1)
        self.assertEqual(
            self.documents["orphan_examples"], ["data/pdfs/orphan.pdf"]
        )

    def test_a_claimed_document_is_not_an_orphan(self):
        named = self.documents["orphan_examples"]
        self.assertNotIn("data/pdfs/hand-filed.pdf", named)
        self.assertNotIn("data/pdfs/read/fetched.pdf", named)

    def test_a_shelved_document_is_reached(self):
        """`pdfs/read/` counts: a shelved file whose record went is an orphan."""
        _write(self.cfg.layout.root / "data/pdfs/read/nobody.pdf", PDF + b"gone")
        documents = migrate.check_documents(self.cfg)
        self.assertIn("data/pdfs/read/nobody.pdf", documents["orphan_examples"])

    def test_the_inbox_is_not_scanned(self):
        """A file there is unclaimed on purpose — it is on its way in."""
        named = self.documents["orphan_examples"]
        self.assertNotIn("inbox/waiting.pdf", named)

    def test_both_directions_are_reported_at_once(self):
        """A record with no file and a file with no record are different faults."""
        store = RecordStore(self.cfg.layout)
        store.save_paper(
            Paper(id="arxiv:2401.00002", title="Claims A Ghost", source="arxiv",
                  local_path="data/pdfs/not-there.pdf")
        )
        documents = migrate.check_documents(self.cfg)
        self.assertEqual(documents["missing"], 1)
        self.assertEqual(documents["orphaned"], 1)

    def test_the_report_writes_nothing(self):
        """It reports; a person decides. Nothing here deletes under `data/`."""
        before = _tree(self.cfg.layout.data)
        migrate.check_documents(self.cfg)
        migrate.status(self.cfg)
        self.assertEqual(_tree(self.cfg.layout.data), before)


def _tree(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


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


class PackVerificationTests(unittest.TestCase):
    """Did pack actually carry what its manifest says it carried?

    A bundle is only worth the claim it makes about itself, and that claim is
    checked here against the filesystem rather than against the manifest's own
    arithmetic.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = _archive(self.sandbox)
        self.root = self.cfg.layout.root
        self.dest = self.root / "migration"
        self.payload = self.dest / "payload"

    def test_every_packed_file_is_byte_identical_to_its_original(self):
        manifest = migrate.pack(self.cfg, self.dest)
        for entry in manifest["files"]:
            self.assertEqual(
                (self.payload / entry["path"]).read_bytes(),
                (self.root / entry["path"]).read_bytes(),
                entry["path"],
            )

    def test_the_recorded_checksum_is_the_files_real_checksum(self):
        """Recomputed independently, so the manifest cannot vouch for itself."""
        manifest = migrate.pack(self.cfg, self.dest)
        for entry in manifest["files"]:
            digest = hashlib.sha256(
                (self.payload / entry["path"]).read_bytes()
            ).hexdigest()
            self.assertEqual(digest, entry["sha256"], entry["path"])

    def test_the_totals_describe_the_bytes_actually_written(self):
        manifest = migrate.pack(self.cfg, self.dest)
        on_disk = [p for p in self.payload.rglob("*") if p.is_file()]
        self.assertEqual(len(on_disk), len(manifest["files"]))
        self.assertEqual(
            sum(p.stat().st_size for p in on_disk),
            sum(totals["bytes"] for totals in manifest["totals"].values()),
        )

    def test_files_and_skipped_together_account_for_every_source_file(self):
        """The completeness guarantee, stated as an assertion."""
        manifest = migrate.pack(self.cfg, self.dest, tier="irreplaceable")
        accounted = {entry["path"] for entry in manifest["files"]} | {
            entry["path"] for entry in manifest["skipped"]
        }
        present = {
            path.relative_to(self.root).as_posix()
            for directory in ("data/pdfs", "data/abstracts", "data/raw", "data/logs", "inbox")
            for path in (self.root / directory).rglob("*")
            if path.is_file()
        }
        self.assertEqual(present - accounted, set())

    def test_a_freshly_packed_bundle_verifies(self):
        migrate.pack(self.cfg, self.dest)
        self.assertTrue(migrate.verify(self.dest)["ok"])

    def test_verify_rejects_a_bundle_carrying_what_its_manifest_omits(self):
        migrate.pack(self.cfg, self.dest)
        (self.payload / "data/pdfs/stowaway.pdf").write_bytes(PDF)
        result = migrate.verify(self.dest)
        self.assertFalse(result["ok"])
        self.assertEqual(result["unlisted"], ["data/pdfs/stowaway.pdf"])

    def test_repacking_over_an_earlier_bundle_is_refused(self):
        """Silently clearing it would delete the only copy after a --move."""
        migrate.pack(self.cfg, self.dest)
        with self.assertRaises(FileExistsError) as caught:
            migrate.pack(self.cfg, self.dest, tier="irreplaceable")
        self.assertIn("--replace", str(caught.exception))

    def test_replace_leaves_a_bundle_that_matches_its_manifest(self):
        migrate.pack(self.cfg, self.dest)
        manifest = migrate.pack(
            self.cfg, self.dest, tier="irreplaceable", replace=True
        )
        result = migrate.verify(self.dest)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["unlisted"], [])
        self.assertEqual(len(manifest["files"]), 3)

    def test_an_archive_with_nothing_untracked_packs_and_verifies(self):
        """Nothing to carry is a valid answer, not a failure."""
        empty = Sandbox()
        self.addCleanup(empty.close)
        cfg = empty.config()
        manifest = migrate.pack(cfg, cfg.layout.root / "migration")
        self.assertEqual(manifest["files"], [])
        self.assertTrue(migrate.verify(cfg.layout.root / "migration")["ok"])

    def test_no_checksum_still_catches_a_size_change_but_not_a_same_size_edit(self):
        """The cost of --no-checksum, asserted rather than described."""
        migrate.pack(self.cfg, self.dest, checksum=False)
        target = self.payload / "data/pdfs/hand-filed.pdf"
        original = target.read_bytes()
        target.unlink()
        target.write_bytes(original + b"longer")
        self.assertFalse(migrate.verify(self.dest, checksum=False)["ok"])

        target.unlink()
        target.write_bytes(b"X" * len(original))
        self.assertTrue(migrate.verify(self.dest, checksum=False)["ok"])


class UnpackVerificationTests(unittest.TestCase):
    """Did unpack put back what the bundle held, and say so honestly?"""

    def setUp(self):
        self.source = Sandbox()
        self.addCleanup(self.source.close)
        self.destination = Sandbox()
        self.addCleanup(self.destination.close)

        self.source_cfg = _archive(self.source)
        self.bundle = self.source_cfg.layout.root / "migration"
        migrate.pack(self.source_cfg, self.bundle)

        self.dest_cfg = self.destination.config()
        shutil.copytree(
            self.source_cfg.layout.papers,
            self.dest_cfg.layout.papers,
            dirs_exist_ok=True,
        )
        self.dest_root = self.dest_cfg.layout.root

    def test_every_restored_file_is_byte_identical_to_the_original(self):
        migrate.unpack(self.dest_cfg, self.bundle)
        manifest = migrate.load_manifest(self.bundle)
        for entry in manifest["files"]:
            self.assertEqual(
                (self.dest_root / entry["path"]).read_bytes(),
                (self.source_cfg.layout.root / entry["path"]).read_bytes(),
                entry["path"],
            )

    def test_the_backlog_and_the_read_shelf_land_where_they_belong(self):
        """`data/pdfs/` is what is still owed; `read/` is what is done."""
        migrate.unpack(self.dest_cfg, self.bundle)
        self.assertTrue((self.dest_root / "data/pdfs/hand-filed.pdf").exists())
        self.assertTrue((self.dest_root / "data/pdfs/read/fetched.pdf").exists())
        self.assertFalse((self.dest_root / "data/pdfs/fetched.pdf").exists())

    def test_a_corrupt_file_is_refused_and_what_was_there_is_left_alone(self):
        migrate.unpack(self.dest_cfg, self.bundle)
        good = (self.dest_root / "data/pdfs/hand-filed.pdf").read_bytes()

        target = self.bundle / "payload/data/pdfs/hand-filed.pdf"
        target.unlink()
        target.write_bytes(PDF + b"tampered in transit")

        result = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertEqual(result["checksum_failed"], ["data/pdfs/hand-filed.pdf"])
        self.assertEqual(
            (self.dest_root / "data/pdfs/hand-filed.pdf").read_bytes(), good
        )

    def test_a_file_missing_from_the_payload_does_not_stop_the_rest(self):
        (self.bundle / "payload/data/pdfs/hand-filed.pdf").unlink()
        result = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertEqual(result["missing_from_bundle"], ["data/pdfs/hand-filed.pdf"])
        self.assertEqual(result["restored"], 6)
        self.assertTrue((self.dest_root / "data/pdfs/read/fetched.pdf").exists())

    def test_a_partial_restore_is_reported_rather_than_passed_off_as_success(self):
        (self.bundle / "payload/data/pdfs/hand-filed.pdf").unlink()
        result = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertEqual(result["documents"]["missing"], 1)
        self.assertIn("local:abc", result["documents"]["examples"][0])

    def test_unpacking_twice_changes_nothing(self):
        first = migrate.unpack(self.dest_cfg, self.bundle)
        before = (self.dest_root / "data/pdfs/hand-filed.pdf").read_bytes()
        second = migrate.unpack(self.dest_cfg, self.bundle)
        self.assertEqual(second["restored"], first["restored"])
        self.assertEqual(second["documents"]["missing"], 0)
        self.assertEqual(
            (self.dest_root / "data/pdfs/hand-filed.pdf").read_bytes(), before
        )

    def test_the_document_check_reads_the_records_not_the_bundle(self):
        """A record added after the move is still answered for."""
        migrate.unpack(self.dest_cfg, self.bundle)
        RecordStore(self.dest_cfg.layout).save_paper(
            Paper(
                id="local:never-arrived",
                title="Filed On The Old Container",
                source="local",
                local_path="data/pdfs/never-arrived.pdf",
            )
        )
        documents = migrate.check_documents(self.dest_cfg)
        self.assertEqual(documents["expected"], 3)
        self.assertEqual(documents["missing"], 1)
        self.assertIn("never-arrived", documents["examples"][0])

    def test_a_dry_run_reports_what_it_would_do_and_touches_nothing(self):
        result = migrate.unpack(self.dest_cfg, self.bundle, dry_run=True)
        self.assertTrue(result["dry_run"])
        self.assertEqual(result["restored"], 7)
        self.assertEqual(
            [p for p in (self.dest_root / "data/pdfs").rglob("*") if p.is_file()], []
        )


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
