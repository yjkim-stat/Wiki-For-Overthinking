"""Coverage ledger and the arXiv sweep.

The property these tests exist for is the one the rest of the pipeline cannot
express: the difference between "the source announced nothing" and "we failed
to read what the source announced".
"""

from __future__ import annotations

import unittest

from pipelines.collect import arxiv_listing
from pipelines.common.store import RecordStore
from pipelines.enrich import coverage

from .sandbox import Sandbox
from .test_arxiv_listing import ABS_PAGE, StubClient, _entry


def day_page(sections: list[tuple[str, int, str]]) -> str:
    """A listing page split into announcement days, as arXiv heads them."""
    parts = []
    for label, total, entries in sections:
        shown = entries.count("<dt>")
        parts.append(
            f"<h3>{label} (showing {shown} of {total} entries )</h3>"
            f'<dl id="articles">{entries}</dl>'
        )
    return f"<html><body>{''.join(parts)}</body></html>"


TWO_DAYS = day_page([
    ("Fri, 8 Aug 2025", 213, _entry("2508.00001", "Causal Inference from Panel Data")
     + _entry("2508.00002", "A Paper About Nothing Tracked")),
    ("Thu, 7 Aug 2025", 190, _entry("2508.00003", "Instrumental Variable Bounds")),
])


class DayParsingTests(unittest.TestCase):
    def test_each_day_carries_its_own_announced_count(self):
        days = arxiv_listing.parse_days(TWO_DAYS)
        self.assertEqual([(d.day, d.announced) for d in days],
                         [("2025-08-08", 213), ("2025-08-07", 190)])

    def test_entries_are_attributed_to_the_day_they_appear_under(self):
        days = arxiv_listing.parse_days(TWO_DAYS)
        self.assertEqual([e.arxiv_id for e in days[0].entries],
                         ["2508.00001", "2508.00002"])
        self.assertEqual([e.arxiv_id for e in days[1].entries], ["2508.00003"])

    def test_a_page_without_day_headings_degrades_to_one_undated_day(self):
        """A redesign that drops them costs the day split, not the entries."""
        from .test_arxiv_listing import LISTING

        days = arxiv_listing.parse_days(LISTING)
        self.assertEqual(len(days), 1)
        self.assertEqual(days[0].day, "")
        self.assertEqual(len(days[0].entries), 2)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def _row(self, **kw):
        base = {"category": "cs.CL", "day": "2025-08-08",
                "announced": 100, "listed": 100, "captured": 100}
        base.update(kw)
        return coverage.DayCoverage(**base)

    def test_a_complete_day_is_not_a_gap(self):
        coverage.record(self.cfg.layout, [self._row()])
        self.assertEqual(coverage.gaps(self.cfg.layout), [])

    def test_a_short_listing_is_a_gap(self):
        coverage.record(self.cfg.layout, [self._row(listed=40, captured=40)])
        gap = coverage.gaps(self.cfg.layout)[0]
        self.assertEqual(gap.listing_gap, 60)
        self.assertEqual(gap.abstract_gap, 0)

    def test_missing_abstracts_are_a_different_gap(self):
        coverage.record(self.cfg.layout, [self._row(captured=30)])
        gap = coverage.gaps(self.cfg.layout)[0]
        self.assertEqual(gap.listing_gap, 0)
        self.assertEqual(gap.abstract_gap, 70)

    def test_counts_only_ever_go_up(self):
        """A later run that paginated less must not erase what an earlier saw."""
        coverage.record(self.cfg.layout, [self._row(listed=100, captured=90)])
        coverage.record(self.cfg.layout, [self._row(listed=20, captured=20)])
        row = coverage.load(self.cfg.layout)[("cs.CL", "2025-08-08")]
        self.assertEqual((row.listed, row.captured), (100, 90))

    def test_gaps_are_worst_first(self):
        coverage.record(self.cfg.layout, [
            self._row(day="2025-08-08", captured=95),
            self._row(day="2025-08-07", captured=10),
        ])
        self.assertEqual([g.day for g in coverage.gaps(self.cfg.layout)],
                         ["2025-08-07", "2025-08-08"])

    def test_the_summary_totals_what_is_owed(self):
        coverage.record(self.cfg.layout, [
            self._row(day="2025-08-08", listed=80, captured=50),
        ])
        self.assertEqual(
            coverage.summarize(self.cfg.layout),
            {"days": 1, "incomplete_days": 1, "missing_listings": 20,
             "missing_abstracts": 30},
        )


class SweepTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"] = {
            "enabled": True,
            "categories": ["cs.CL"],
            "listing": {"page_size": 250, "max_pages": 2, "sweep": {"enabled": True}},
        }
        self.store = RecordStore(self.cfg.layout)
        self.url = "https://arxiv.org/list/cs.CL/recent"

    def tearDown(self):
        self.sandbox.close()

    def _sweep(self, client, errors=None):
        return arxiv_listing.sweep(self.cfg, self.cfg.topics, self.store, client, errors)

    def test_every_announced_paper_is_recorded_not_only_the_matches(self):
        """The untracked title is stored too -- that is the point of the sweep."""
        self._sweep(StubClient({self.url: TWO_DAYS}))
        held = self.store.load_abstracts("cs.CL", "2025-08-08")
        self.assertEqual(sorted(held), ["2508.00001", "2508.00002"])

    def test_the_ledger_records_arxivs_own_count_against_ours(self):
        self._sweep(StubClient({self.url: TWO_DAYS}))
        rows = coverage.load(self.cfg.layout)
        friday = rows[("cs.CL", "2025-08-08")]
        self.assertEqual(friday.announced, 213)
        self.assertEqual(friday.listed, 2)
        self.assertEqual(friday.listing_gap, 211)

    def test_a_short_day_is_reported_as_a_gap_rather_than_a_quiet_day(self):
        self._sweep(StubClient({self.url: TWO_DAYS}))
        self.assertEqual(coverage.summarize(self.cfg.layout)["incomplete_days"], 2)

    def test_abstracts_are_fetched_relevance_first(self):
        client = StubClient({
            self.url: TWO_DAYS,
            "https://arxiv.org/abs/2508.00001": ABS_PAGE,
        })
        self.cfg.sources["arxiv"]["listing"]["sweep"]["max_abstracts_per_run"] = 1
        self._sweep(client)
        fetched = [c[0] for c in client.calls if "/abs/" in c[0]]
        self.assertEqual(fetched, ["https://arxiv.org/abs/2508.00001"])

    def test_a_captured_abstract_is_stored_against_its_day(self):
        client = StubClient({
            self.url: TWO_DAYS,
            "https://arxiv.org/abs/2508.00001": ABS_PAGE,
        })
        self._sweep(client)
        held = self.store.load_abstracts("cs.CL", "2025-08-08")
        self.assertIn("instrumental", held["2508.00001"]["abstract"])

    def test_the_budget_bounds_a_run_and_the_rest_is_carried(self):
        self.cfg.sources["arxiv"]["listing"]["sweep"]["max_abstracts_per_run"] = 1
        client = StubClient({self.url: TWO_DAYS})
        counts = self._sweep(client)
        self.assertEqual(len([c for c in client.calls if "/abs/" in c[0]]), 1)
        self.assertGreater(coverage.summarize(self.cfg.layout)["missing_abstracts"], 0)
        self.assertEqual(counts["days"], 2)

    def test_a_second_run_does_not_refetch_what_it_holds(self):
        pages = {self.url: TWO_DAYS, "https://arxiv.org/abs/2508.00001": ABS_PAGE}
        self.cfg.sources["arxiv"]["listing"]["sweep"]["max_abstracts_per_run"] = 1
        self._sweep(StubClient(pages))
        second = StubClient(pages)
        self._sweep(second)
        self.assertNotIn("https://arxiv.org/abs/2508.00001",
                         [c[0] for c in second.calls])

    def test_disabled_means_no_requests(self):
        self.cfg.sources["arxiv"]["listing"]["sweep"]["enabled"] = False
        client = StubClient({self.url: TWO_DAYS})
        self.assertEqual(self._sweep(client)["days"], 0)
        self.assertEqual(client.calls, [])

    def test_a_dead_listing_is_reported_not_raised(self):
        errors: list[str] = []
        self._sweep(StubClient({}, fail=True), errors)
        self.assertTrue(any("arxiv_sweep" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
