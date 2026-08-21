"""Regression guard for three silent under-collection defects.

These live in a file of their own rather than in `tests/test_arxiv_listing.py`,
which is the file a wholesale update would replace. The fixes below were lost
exactly that way once: made inside general-purpose files, registered nowhere,
and reverted the moment a newer version of those files was adopted. A test that
sits apart from the code it guards is what makes that loud instead of silent.

Each class corresponds to one defect. All three shared a failure mode: the run
reported success while collecting less than it should, which is indistinguishable
from a quiet day.
"""

from __future__ import annotations

import unittest
from datetime import date

from pipelines.collect import arxiv, arxiv_listing
from pipelines.common.http import HTTPError

from .sandbox import Sandbox


def _entry(number: str, title: str, authors: str = "Ada Lovelace, Alan Turing") -> str:
    return f"""
<dt>
  <a name="item1">[1]</a>
  <a href="/abs/{number}" title="Abstract">arXiv:{number}</a>
  [<a href="/pdf/{number}" title="Download PDF">pdf</a>,
   <a href="/format/{number}">other</a>]
</dt>
<dd>
  <div class="meta">
    <div class="list-title mathjax"><span class="descriptor">Title:</span> {title}</div>
    <div class="list-authors"><span class="descriptor">Authors:</span> {authors}</div>
    <div class="list-subjects"><span class="descriptor">Subjects:</span>
      <span class="primary-subject">Computation and Language (cs.CL)</span>;
      Machine Learning (cs.LG)</div>
  </div>
</dd>
"""


def page(entries: str, total: int = 2) -> str:
    return f"""
<html><body>
  <h2>Computation and Language</h2>
  <!-- The browse-context sidebar links to /abs/ too, but carries no <dt>. -->
  <div class="browse"><a href="/abs/0000.00000">previous</a></div>
  <p>Showing 1-50 of {total:,} entries</p>
  <small>total of {total:,} entries</small>
  <dl id="articles">{entries}</dl>
</body></html>
"""


LISTING = page(
    _entry("2501.00001", "Causal Inference from Panel Data")
    + _entry("2501.00002", "A Paper About Nothing Tracked")
)


ABS_PAGE = """
<html><head>
  <meta name="citation_title" content="Causal Inference from Panel Data">
  <meta name="citation_abstract" content="We estimate effects with an instrumental
   variable.">
</head><body>
  <blockquote class="abstract mathjax">
    <span class="descriptor">Abstract:</span> ignored, the meta tag wins
  </blockquote>
</body></html>
"""


class StubClient:
    """Serves pages by URL, ignoring query parameters unless asked to page."""

    def __init__(self, pages: dict[str, str], fail: bool = False) -> None:
        self.pages = pages
        self.fail = fail
        self.calls: list[tuple[str, dict]] = []

    def get(self, url, params=None, headers=None):
        self.calls.append((url, dict(params or {})))
        if self.fail:
            raise HTTPError("simulated outage")
        key = url
        if params and "skip" in params:
            key = f"{url}?skip={params['skip']}"
        body = self.pages.get(key, self.pages.get(url))
        if body is None:
            raise HTTPError(f"GET {url} -> HTTP 404")
        return body.encode("utf-8")


ONE_ENTRY_FEED = """
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2501.09999</id>
    <title>Causal Inference from Registry Data</title>
    <published>2025-01-02T00:00:00Z</published>
    <summary>An instrumental variable argument.</summary>
  </entry>
</feed>
"""


class PerTopicFallbackTests(unittest.TestCase):
    """The `auto` gate is per topic, not per run.

    Gating on the whole run meant one topic returning a single paper suppressed
    the fallback for every other topic — so the topics the API answered with
    nothing, the ones the fallback exists for, were exactly the ones that never
    got it.
    """

    def setUp(self):
        self.sandbox = Sandbox({"topic-a": "Topic A", "topic-b": "Topic B"})
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"] = {
            "enabled": True,
            "categories": ["cs.CL"],
            "api_url": "https://api.test",
            "listing": {"mode": "auto", "fetch_abstracts": False},
        }
        self.url = "https://arxiv.org/list/cs.CL/recent"

    def tearDown(self):
        self.sandbox.close()

    class _FirstTopicAnswers(StubClient):
        """The API answers the first topic's queries and nothing after."""

        def __init__(self, pages):
            super().__init__(pages)
            self.answered = False

        def get_xml(self, url, params=None, headers=None):
            import xml.etree.ElementTree as ET

            self.calls.append((url, dict(params or {})))
            if not self.answered:
                self.answered = True
                return ET.fromstring(ONE_ENTRY_FEED)
            return ET.fromstring('<feed xmlns="http://www.w3.org/2005/Atom"/>')

    def test_the_topic_the_api_answered_does_not_suppress_the_other(self):
        client = self._FirstTopicAnswers({self.url: DAY_LISTING})
        papers = arxiv.collect(
            self.cfg, self.cfg.topics, date(2025, 1, 1), client=client
        )
        ids = sorted(p.id for p in papers)
        # The API's paper for the first topic, and the listing's for the second.
        self.assertEqual(ids, ["arxiv:2501.00001", "arxiv:2501.09999"])
        self.assertIn(self.url, [c[0] for c in client.calls])

    def test_no_listing_request_when_every_topic_was_answered(self):
        class _AllAnswered(StubClient):
            def get_xml(inner, url, params=None, headers=None):
                import xml.etree.ElementTree as ET

                inner.calls.append((url, dict(params or {})))
                return ET.fromstring(ONE_ENTRY_FEED)

        client = _AllAnswered({self.url: DAY_LISTING})
        arxiv.collect(self.cfg, self.cfg.topics, date(2025, 1, 1), client=client)
        self.assertNotIn(self.url, [c[0] for c in client.calls])


DAY_LISTING = (
    '<html><body><h3>Fri, 8 Aug 2025 (showing 2 of 213 entries )</h3>'
    '<dl id="articles">'
    + _entry("2501.00001", "Causal Inference from Panel Data")
    + _entry("2501.00002", "A Paper About Nothing Tracked")
    + "</dl></body></html>"
)


class AnnouncementDateTests(unittest.TestCase):
    """A listing record must carry the day it was announced under.

    Without it `publish/archive.py` files the paper under
    `archive/papers/unknown/` and the flat index sorts it below everything
    dated, so a paper would be second-class purely because the API missed it
    and the listing caught it.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"] = {
            "enabled": True,
            "categories": ["cs.CL"],
            "listing": {
                "mode": "always",
                "page_size": 250,
                "max_pages": 1,
                "fetch_abstracts": False,
            },
        }
        self.url = "https://arxiv.org/list/cs.CL/recent"

    def tearDown(self):
        self.sandbox.close()

    def test_the_day_heading_dates_every_entry_beneath_it(self):
        days = arxiv_listing.parse_days(DAY_LISTING)
        self.assertEqual([e.announced for e in days[0].entries],
                         ["2025-08-08", "2025-08-08"])

    def test_a_collected_paper_carries_that_day_as_published(self):
        papers = arxiv_listing.collect(
            self.cfg, self.cfg.topics, date.today(),
            StubClient({self.url: DAY_LISTING}),
        )
        self.assertEqual([p.published for p in papers], ["2025-08-08"])
        self.assertEqual(papers[0].year, 2025)

    def test_a_page_with_no_day_heading_leaves_the_date_empty(self):
        """An undated page is answered with no date, not with a guess."""
        papers = arxiv_listing.collect(
            self.cfg, self.cfg.topics, date.today(),
            StubClient({self.url: LISTING}),
        )
        self.assertEqual(papers[0].published, "")
        self.assertEqual(papers[0].year, 0)

    def test_parse_listing_alone_still_reports_no_day(self):
        """The day belongs to the section, not the entry's own markup."""
        entries = arxiv_listing.parse_listing(DAY_LISTING)
        self.assertEqual([e.announced for e in entries], ["", ""])


class SweepLedgerTests(unittest.TestCase):
    """The ledger must survive a run whose backfill never happens.

    The listing pass costs a handful of requests and produces arXiv's own
    per-day count; the backfill costs one request per announced paper. If the
    ledger is only written after the backfill, a run cut short records nothing,
    and a sweep that is always cut short is indistinguishable from one that was
    never enabled.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"] = {
            "enabled": True,
            "categories": ["cs.CL"],
            "listing": {
                "page_size": 250,
                "max_pages": 1,
                "sweep": {"enabled": True, "max_abstracts_per_run": 0},
            },
        }
        self.url = "https://arxiv.org/list/cs.CL/recent"

    def tearDown(self):
        self.sandbox.close()

    def _sweep(self, client):
        from pipelines.common.store import RecordStore

        return arxiv_listing.sweep(
            self.cfg, self.cfg.topics, RecordStore(self.cfg.layout), client=client
        )

    def test_the_day_count_is_on_disk_before_the_first_abstract_request(self):
        """The ordering is the point, not the end state.

        A budget of zero would pass even with the ledger written last, because
        nothing interrupts the function. So this watches the filesystem from
        inside the abstract fetch: by the time the first `/abs/` request goes
        out, the day must already be recorded, because that is the moment after
        which a killed process loses everything not yet written.
        """
        from pipelines.enrich import coverage

        self.cfg.sources["arxiv"]["listing"]["sweep"]["max_abstracts_per_run"] = 5
        observed: list[dict] = []

        class WatchingClient(StubClient):
            def get(inner, url, params=None, headers=None):
                if "/abs/" in url:
                    observed.append(coverage.load(self.cfg.layout))
                return super().get(url, params, headers)

        counts = self._sweep(
            WatchingClient({
                self.url: DAY_LISTING,
                "https://arxiv.org/abs/2501.00001": ABS_PAGE,
                "https://arxiv.org/abs/2501.00002": ABS_PAGE,
            })
        )

        self.assertTrue(observed, "no abstract was requested; the test proves nothing")
        first = observed[0]
        self.assertIn(("cs.CL", "2025-08-08"), first)
        self.assertEqual(first[("cs.CL", "2025-08-08")].announced, 213)
        self.assertEqual(counts["days"], 1)

    def test_no_abstract_request_is_made_when_the_budget_is_zero(self):
        client = StubClient({self.url: DAY_LISTING})
        self._sweep(client)
        self.assertEqual(
            [c[0] for c in client.calls if "/abs/" in c[0]], []
        )

    def test_the_gap_is_visible_as_a_debt_rather_than_an_error(self):
        from pipelines.enrich import coverage

        self._sweep(StubClient({self.url: DAY_LISTING}))
        gaps = coverage.gaps(self.cfg.layout)
        self.assertEqual(len(gaps), 1)
        # 213 announced against 2 paginated, and no abstract for either.
        self.assertEqual(gaps[0].listing_gap, 211)
        self.assertEqual(gaps[0].abstract_gap, 2)


if __name__ == "__main__":
    unittest.main()
