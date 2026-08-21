"""The second chance at a document, for papers already waiting to be read.

`pdf_fetch` runs inside collection and only sees papers arriving that run. A
paper queued before documents were fetched at all, or on a run where its host was
down, is never revisited: `seen.sqlite` remembers it, so collection will not
offer it again, and nothing else asks. The backlog it leaves is not a few papers
— on the archive this was written for it was every unread paper in the queue.

The properties worth defending are that it is bounded, that it is re-runnable,
and that failure changes nothing. A backfill that fetched twice, or that emptied
a host's patience in one pass, would be worse than the backlog.
"""

from __future__ import annotations

import unittest

from pipelines import backfill
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"
PDF_BYTES = b"%PDF-1.7\nnot really a pdf, but it starts like one\n"


class StubClient:
    def __init__(self, bodies: dict[str, bytes]) -> None:
        self.bodies = bodies
        self.calls: list[str] = []

    def get(self, url, params=None, headers=None):
        self.calls.append(url)
        from pipelines.common.http import HTTPError

        try:
            return self.bodies[url]
        except KeyError:
            raise HTTPError(f"GET {url} -> HTTP 404") from None


class BackfillTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.queue = Queue(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def _paper(self, index: int, *, pdf_url: str | None = None, score: float = 0.5,
               queued: bool = True, local_path: str = "", published: str = "2024-01-15",
               paper_id: str | None = None):
        paper = Paper(
            id=paper_id or f"arxiv:2401.0000{index}",
            title=f"Paper {index}",
            source="arxiv",
            published=published,
            topics=[SLUG],
            scores={SLUG: score},
            local_path=local_path,
            pdf_url=(f"https://x.test/{index}" if pdf_url is None else pdf_url),
        )
        self.store.save_paper(paper)
        if queued:
            self.queue.enqueue(
                kind="paper", item_id=paper.id, topics=[SLUG], language="en",
                instructions="", output_schema={}, payload={},
            )
        return paper

    def _candidates(self, **kwargs):
        return backfill.candidates(self.cfg, self.store, self.queue, **kwargs)

    # -- what counts as a candidate ------------------------------------------
    def test_a_waiting_paper_with_a_url_is_a_candidate(self):
        self._paper(1)
        ready, unreachable = self._candidates()
        self.assertEqual([p.id for p in ready], ["arxiv:2401.00001"])
        self.assertEqual(unreachable, 0)

    def test_a_paper_that_already_has_its_document_is_not(self):
        """Re-runnable: the whole point is that running it again costs nothing."""
        self._paper(1, local_path="data/pdfs/arxiv-2401-00001.pdf")
        ready, _ = self._candidates()
        self.assertEqual(ready, [])

    def test_a_paper_with_no_task_pending_is_not(self):
        """Nobody is waiting to read it, so fetching is speculative."""
        self._paper(1, queued=False)
        ready, _ = self._candidates()
        self.assertEqual(ready, [])

    def test_a_paper_naming_no_pdf_is_counted_not_dropped(self):
        """These are the input to a lookup asking where the document is.

        The id is deliberately not an arXiv one: an arXiv id implies its own
        document URL and is derived below, so a record that genuinely names no
        document has to come from a scheme that does not.
        """
        self._paper(1, pdf_url="", paper_id="doi:10.1145/3774904.3793054")
        ready, unreachable = self._candidates()
        self.assertEqual(ready, [])
        self.assertEqual(unreachable, 1)

    # -- a url the id already implies ----------------------------------------
    def test_an_arxiv_paper_with_no_pdf_url_derives_one(self):
        """It reached the archive through a bibliographic index, which carries
        a landing page and no document. Its own id says where the document is,
        and nothing else will ever revisit it: dedup has seen the paper."""
        self._paper(1, pdf_url="")
        ready, unreachable = self._candidates()
        self.assertEqual([p.id for p in ready], ["arxiv:2401.00001"])
        self.assertEqual(unreachable, 0)

    def test_the_derived_url_is_set_on_the_record_not_only_used(self):
        """So the fetch records where the document came from."""
        self._paper(1, pdf_url="")
        ready, _ = self._candidates()
        self.assertEqual(ready[0].pdf_url, "https://arxiv.org/pdf/2401.00001")

    def test_a_url_the_record_already_names_is_not_overwritten(self):
        """A publisher's own link outranks a guess from the identifier."""
        self._paper(1, pdf_url="https://x.test/chosen.pdf")
        ready, _ = self._candidates()
        self.assertEqual(ready[0].pdf_url, "https://x.test/chosen.pdf")

    def test_a_version_suffix_is_dropped_from_the_derived_url(self):
        """Versions are revisions, not new papers."""
        paper = Paper(id="arxiv:2401.00009v3", title="T", source="semanticscholar")
        self.assertEqual(
            backfill.derived_pdf_url(paper), "https://arxiv.org/pdf/2401.00009"
        )

    def test_nothing_is_derived_for_a_non_arxiv_identifier(self):
        for bad in ("doi:10.1145/x", "local:49199e3b0f694ee1", "title:abc", "", "arxiv:"):
            with self.subTest(bad):
                self.assertEqual(backfill.derived_pdf_url(Paper(id=bad, title="T", source="dblp")), "")

    def test_topic_narrows_both_halves_of_the_count(self):
        self._paper(1)
        # Not an arXiv id: an arXiv one would have its document URL derived and
        # would land in `ready`, which is not what this test is about.
        other = self._paper(2, pdf_url="", paper_id="doi:10.1145/3774904.3793054")
        other.topics = ["another-topic"]
        self.store.save_paper(other)
        ready, unreachable = self._candidates(topic_slugs=["another-topic"])
        self.assertEqual(ready, [])
        self.assertEqual(unreachable, 1, "the skipped count must answer --topic too")

    # -- order ---------------------------------------------------------------
    def test_the_backlog_is_ordered_by_score(self):
        self._paper(1, score=0.2)
        self._paper(2, score=0.9)
        self._paper(3, score=0.5)
        ready, _ = self._candidates()
        ready.sort(key=lambda p: backfill._sort_key(p, "score"))
        self.assertEqual(
            [p.id for p in ready],
            ["arxiv:2401.00002", "arxiv:2401.00003", "arxiv:2401.00001"],
        )

    def test_a_paper_wanted_by_two_topics_outranks_one_wanted_badly(self):
        """Sum, not max — leverage is breadth across what the group tracks."""
        broad = Paper(id="arxiv:b", title="Broad", source="arxiv",
                      topics=[SLUG, "second"], scores={SLUG: 0.5, "second": 0.5})
        narrow = Paper(id="arxiv:n", title="Narrow", source="arxiv",
                       topics=[SLUG], scores={SLUG: 0.9})
        self.assertGreater(backfill.leverage(broad), backfill.leverage(narrow))

    def test_ties_are_broken_the_same_way_every_run(self):
        """A bound is applied after the sort, so an unstable order fetches a
        different set each time and the backlog drains in no direction at all."""
        a = self._paper(1, score=0.5, published="2024-01-15")
        b = self._paper(2, score=0.5, published="2024-06-01")
        keys = [backfill._sort_key(p, "score") for p in (a, b)]
        self.assertLess(keys[1], keys[0], "newer first among equal scores")

    def test_an_undated_paper_sorts_after_dated_ones(self):
        dated = self._paper(1, score=0.5, published="2024-01-15")
        undated = self._paper(2, score=0.5, published="")
        self.assertLess(
            backfill._sort_key(dated, "score"), backfill._sort_key(undated, "score")
        )

    # -- fetching ------------------------------------------------------------
    def test_the_limit_bounds_what_is_fetched(self):
        for index in (1, 2, 3):
            self._paper(index, score=1.0 - index / 10)
        client = StubClient({f"https://x.test/{i}": PDF_BYTES for i in (1, 2, 3)})
        result = backfill.run(self.cfg, limit=1, client=client)
        self.assertEqual(result["fetched"], 1)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(client.calls, ["https://x.test/1"], "the best one first")

    def test_a_fetched_document_is_saved_onto_the_record(self):
        self._paper(1)
        client = StubClient({"https://x.test/1": PDF_BYTES})
        backfill.run(self.cfg, client=client)
        reloaded = RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001")
        self.assertTrue(reloaded.local_path)
        self.assertTrue((self.cfg.layout.root / reloaded.local_path).is_file())

    def test_a_failure_leaves_the_paper_and_its_task_alone(self):
        """Failure is ordinary: the reading still happens, from the abstract."""
        self._paper(1)
        client = StubClient({})  # every request 404s
        result = backfill.run(self.cfg, client=client)
        self.assertEqual(result["fetched"], 0)
        self.assertEqual(result["failed"], 1)
        self.assertEqual(
            RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001").local_path, ""
        )
        self.assertEqual(self.queue.pending_ids(kind="paper"), ["paper__arxiv-2401-00001"])

    def test_running_it_twice_fetches_once(self):
        self._paper(1)
        client = StubClient({"https://x.test/1": PDF_BYTES})
        backfill.run(self.cfg, client=client)
        second = backfill.run(self.cfg, client=client)
        self.assertEqual(second["candidates"], 0)
        self.assertEqual(len(client.calls), 1)

    def test_a_dry_run_requests_nothing_and_writes_nothing(self):
        self._paper(1)
        client = StubClient({"https://x.test/1": PDF_BYTES})
        result = backfill.run(self.cfg, dry_run=True, client=client)
        self.assertEqual(client.calls, [])
        self.assertEqual(result["fetched"], 0)
        self.assertEqual(result["candidates"], 1)
        self.assertEqual(
            RecordStore(self.cfg.layout).load_paper("arxiv:2401.00001").local_path, ""
        )

    def test_it_queues_nothing_and_reads_nothing(self):
        """It is not a collector: no new record, no new task, no summary."""
        self._paper(1)
        before = sorted(p.name for p in self.cfg.layout.papers.glob("*.json"))
        client = StubClient({"https://x.test/1": PDF_BYTES})
        backfill.run(self.cfg, client=client)
        self.assertEqual(
            sorted(p.name for p in self.cfg.layout.papers.glob("*.json")), before
        )
        self.assertEqual(len(self.queue.pending_ids()), 1)
        self.assertEqual(list(self.cfg.layout.summaries.rglob("*.json")), [])


if __name__ == "__main__":
    unittest.main()
