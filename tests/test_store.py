"""Record store tests.

Transcripts are written into the same directory as the video records they
belong to, so the tests that matter here are the ones that put a transcript on
disk and then exercise the readers that glob that directory.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Paper, PaperSummary, Video, canonical_video_id
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

SEGMENTS = [
    {"start_s": 0.0, "text": "hello"},
    {"start_s": 2.0, "text": "world"},
]


class TranscriptsBesideRecordsTests(unittest.TestCase):
    """A stored transcript must not be mistaken for a video record.

    The transcript file matches the same ``*.json`` glob as the records, and a
    transcript is a JSON *array*, so a reader that hands it to
    ``Video.from_dict`` raises ``AttributeError: 'list' object has no attribute
    'items'``. Both entry points call ``rebuild_indexes``, so that took down the
    whole pipeline — and only for deployments that had installed the optional
    ``youtube-transcript-api``, which is why it stayed hidden.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.video = Video(
            id=canonical_video_id("abc123XYZ"),
            title="A seminar on causal inference",
            source_id="abc123XYZ",
            channel="Research Seminar",
            url="https://www.youtube.com/watch?v=abc123XYZ",
            description="A talk on instrumental variables.",
            published="2026-01-15",
            duration_s=3600,
            transcript_available=True,
            topics=["test-topic"],
            scores={"test-topic": 0.8},
        )
        self.store.save_video(self.video)
        self.store.save_transcript(self.video.id, SEGMENTS)

    def tearDown(self):
        self.sandbox.close()

    def test_both_files_share_the_glob(self):
        """If this stops being true the rest of the class is testing nothing."""
        names = sorted(p.name for p in self.cfg.layout.videos.glob("*.json"))
        self.assertEqual(len(names), 2)

    def test_iter_videos_yields_the_record_only(self):
        videos = list(self.store.iter_videos())
        self.assertEqual([v.id for v in videos], [self.video.id])

    def test_the_transcript_is_still_readable(self):
        self.assertEqual(self.store.load_transcript(self.video.id), SEGMENTS)

    def test_rebuild_indexes_counts_one_video(self):
        counts = self.store.rebuild_indexes()
        self.assertEqual(counts.get("videos"), 1)

    def test_a_full_render_completes_with_a_transcript_on_disk(self):
        """The one that would have failed: both entry points call rebuild_indexes."""
        result = render.run(self.cfg)
        self.assertEqual(result["archive"]["videos"], 1)

    def test_a_stray_non_record_is_skipped_rather_than_fatal(self):
        from pipelines.common.store import write_json

        write_json(self.cfg.layout.videos / "notes.json", ["not", "a", "record"])
        self.assertEqual([v.id for v in self.store.iter_videos()], [self.video.id])


if __name__ == "__main__":
    unittest.main()


class ShelvingTests(unittest.TestCase):
    """`data/pdfs/` is the backlog; `data/pdfs/read/` is what is done.

    Before this, both sat in one directory and the only way to tell them apart
    was to consult the queue. The pass is self-healing rather than
    transactional: a move and a record update cannot be made atomic together,
    so every render re-derives where a file belongs and corrects what it finds.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.paper = Paper(
            id="local:abc123",
            title="A Filed Paper",
            source="local",
            local_path="data/pdfs/local-abc123.pdf",
        )
        self.store.save_paper(self.paper)
        self.pending = self.cfg.layout.pdfs / "local-abc123.pdf"
        self.shelved = self.cfg.layout.pdfs_read / "local-abc123.pdf"
        self.pending.parent.mkdir(parents=True, exist_ok=True)
        self.pending.write_bytes(b"%PDF-1.4 pretend")

    def tearDown(self):
        self.sandbox.close()

    def _read(self):
        self.store.save_paper_summary(
            PaperSummary(paper_id=self.paper.id, one_liner="Read.")
        )

    def _reload(self):
        return self.store.load_paper(self.paper.id)

    def test_an_unread_document_stays_in_the_backlog(self):
        render.shelve_documents(self.cfg)
        self.assertTrue(self.pending.exists())
        self.assertFalse(self.shelved.exists())

    def test_a_read_document_moves_and_the_record_follows(self):
        self._read()
        counts = render.shelve_documents(self.cfg)
        self.assertEqual(counts["shelved"], 1)
        self.assertTrue(self.shelved.exists())
        self.assertFalse(self.pending.exists())
        self.assertEqual(self._reload().local_path, "data/pdfs/read/local-abc123.pdf")

    def test_the_pass_is_idempotent(self):
        self._read()
        render.shelve_documents(self.cfg)
        self.assertEqual(render.shelve_documents(self.cfg),
                         {"shelved": 0, "returned": 0, "repaired": 0})

    def test_a_stale_pointer_is_repaired(self):
        """The crash case: the file moved, the record never got saved."""
        self._read()
        self.shelved.parent.mkdir(parents=True, exist_ok=True)
        self.pending.replace(self.shelved)          # move happened
        # record still says data/pdfs/... — as it would after a crash
        counts = render.shelve_documents(self.cfg)
        self.assertEqual(counts["repaired"], 1)
        self.assertEqual(self._reload().local_path, "data/pdfs/read/local-abc123.pdf")

    def test_withdrawing_a_reading_returns_the_document(self):
        """Clearing a summary re-queues the paper, so the file comes back."""
        self._read()
        render.shelve_documents(self.cfg)
        self.store.paper_summary_path(self.paper.id).unlink()
        counts = render.shelve_documents(self.cfg)
        self.assertEqual(counts["returned"], 1)
        self.assertTrue(self.pending.exists())
        self.assertEqual(self._reload().local_path, "data/pdfs/local-abc123.pdf")

    def test_a_missing_document_leaves_the_record_alone(self):
        """A fresh clone has records whose PDFs were never committed."""
        self._read()
        self.pending.unlink()
        counts = render.shelve_documents(self.cfg)
        self.assertEqual(counts, {"shelved": 0, "returned": 0, "repaired": 0})
        self.assertEqual(self._reload().local_path, "data/pdfs/local-abc123.pdf")

    def test_a_paper_with_no_document_is_untouched(self):
        remote = Paper(id="arxiv:2401.1", title="Remote", source="arxiv")
        self.store.save_paper(remote)
        render.shelve_documents(self.cfg)
        self.assertEqual(self.store.load_paper("arxiv:2401.1").local_path, "")

    def test_the_shelf_lives_inside_the_ignored_directory(self):
        """So no deployment can forget to ignore it separately."""
        self.assertEqual(self.cfg.layout.pdfs_read.parent, self.cfg.layout.pdfs)
