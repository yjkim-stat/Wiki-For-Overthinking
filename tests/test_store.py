"""Record store tests.

Transcripts are written into the same directory as the video records they
belong to, so the tests that matter here are the ones that put a transcript on
disk and then exercise the readers that glob that directory.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import Video, canonical_video_id
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
