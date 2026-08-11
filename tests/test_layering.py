"""The boundary between the code and the archive it accumulates.

This repository is deployed into projects that then run it for months. The code
gets replaced; the archive does not. That only works if the two halves are
actually separate, and the separation this file defends is one rule:

    **Rendering reads `data/`. It never writes to it.**

Everything that writes to the source of truth lives under `collect/` (things
arriving from outside) or `enrich/` (things derived from what already arrived).
`publish/` draws what those two produced.

The rule used to be false. `publish/wiki.py` derived the concept records it drew
and saved them, so `render --only wiki` could delete a record from `data/` — a
renderer, mutating the archive. It is asserted here rather than believed,
because nothing about the old arrangement looked wrong from the outside.
"""

from __future__ import annotations

import hashlib
import re
import unittest
from pathlib import Path

from pipelines import render
from pipelines.common.paths import REPO_ROOT
from pipelines.common.schema import Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import concepts as concepts_mod
from pipelines.publish import wiki

from .sandbox import Sandbox

SLUG = "test-topic"


def _summary(paper_id: str) -> PaperSummary:
    return PaperSummary(
        paper_id=paper_id,
        one_liner="It does a thing.",
        problem="The thing was hard.",
        method="By reweighting.",
        results="Beats the baseline.",
        relevance={SLUG: "Moves the topic forward."},
        concepts=["Instrumental Variable"],
        methods=["Behaviour Cloning"],
        datasets=["Open X-Embodiment"],
    )


def _snapshot(directory: Path) -> dict[str, str]:
    """Every file under ``directory``, by content. The archive, as bytes."""
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


class RenderingDoesNotWriteToData(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        store = RecordStore(self.cfg.layout)
        for index in (1, 2):
            paper_id = f"arxiv:2401.0000{index}"
            store.save_paper(
                Paper(
                    id=paper_id,
                    title=f"Paper {index}: causal inference",
                    source="arxiv",
                    abstract="We estimate effects with an instrumental variable.",
                    published="2024-01-15",
                    year=2024,
                    topics=[SLUG],
                )
            )
            store.save_paper_summary(_summary(paper_id))
        # One full pass, so `data/` holds derived entities as well as records.
        render.run(self.cfg, skip_queueing=True)
        self.data = self.cfg.layout.data

    def test_the_wiki_renderer_leaves_the_archive_untouched(self):
        concepts, live = concepts_mod.rebuild(self.cfg)
        before = _snapshot(self.data)
        wiki.update(self.cfg, concepts, live)
        self.assertEqual(_snapshot(self.data), before)

    def test_the_archive_renderer_leaves_the_archive_untouched(self):
        before = _snapshot(self.data)
        render.rebuild_archive(self.cfg)
        self.assertEqual(_snapshot(self.data), before)

    def test_the_output_renderers_leave_the_archive_untouched(self):
        before = _snapshot(self.data)
        render.rebuild_outputs(self.cfg)
        self.assertEqual(_snapshot(self.data), before)

    def test_a_wiki_note_is_rebuilt_from_nothing(self):
        note = wiki.note_path(self.cfg.layout, "concept", "instrumental-variable")
        self.assertTrue(note.exists())
        note.unlink()
        concepts, live = concepts_mod.rebuild(self.cfg)
        wiki.update(self.cfg, concepts, live)
        self.assertTrue(note.exists())


class NoRendererHoldsAWriteToTheSourceOfTruth(unittest.TestCase):
    """A tripwire, cheaper than the behavioural tests and easier to read.

    The behavioural tests above catch a write that happens; this catches one
    that has merely been written down, including on a path no fixture reaches.
    """

    WRITERS = re.compile(r"\.save_(paper|video|concept|finding|abstracts|transcript)")

    def test_no_module_under_publish_saves_a_record(self):
        offenders = []
        for path in sorted((REPO_ROOT / "pipelines" / "publish").glob("*.py")):
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                if self.WRITERS.search(line):
                    offenders.append(f"{path.name}:{number}: {line.strip()}")
        self.assertEqual(
            offenders,
            [],
            "publish/ is a pure function of data/; move the write to enrich/",
        )

    def test_the_derivation_of_entities_lives_under_enrich(self):
        """Where `harvest` lives is the whole point, so it is asserted."""
        self.assertTrue(hasattr(concepts_mod, "harvest"))
        self.assertFalse(hasattr(wiki, "harvest"))


if __name__ == "__main__":
    unittest.main()
