"""Virtual-site collector tests.

The parsers are exercised against fixtures rather than the live sites, so the
fixtures below are what the tests actually assert about. The listing fixture
carries the two things that matter about the real page: the programme lives in
a ``<noscript>`` fallback, and the navigation bar links to a poster path that
is not a paper.
"""

from __future__ import annotations

import unittest
from datetime import date

from pipelines.collect import virtual_site
from pipelines.common.http import HTTPError

from .sandbox import Sandbox

LISTING = """
<html><body>
  <nav class="navbar">
    <!-- The login link points at a poster path too. It is not a paper, and it
         is the reason only the noscript block is parsed. -->
    <a href="/virtual/2026/poster/00000">Login</a>
  </nav>
  <div id="root"><!-- everything real is rendered by JavaScript --></div>
  <noscript class="noscript">Enable Javascript in your browser to see the papers page.
  <ul>
    <li><a href="/virtual/2026/poster/31415">Causal Inference from Panel Data</a></li>
    <li><a href="/virtual/2026/oral/27182">Instrumental Variable Bounds</a></li>
    <li><a href="/virtual/2026/poster/16180">A Paper About Nothing Tracked</a></li>
    <li><a href="/virtual/2026/poster/31415">Causal Inference from Panel Data</a></li>
  </ul>
  </noscript>
</body></html>
"""

DETAIL = """
<html><head>
  <meta name="citation_title" content="Causal Inference from Panel Data">
  <meta name="citation_author" content="Ada Lovelace">
  <meta name="citation_author" content="Alan Turing">
  <meta name="citation_abstract" content="We estimate treatment effects with an
   instrumental variable.">
</head><body><div class="abstract">ignored, the meta tag wins</div></body></html>
"""

DETAIL_NO_META = """
<html><body>
  <div class="card-abstract"><p>A <b>bare</b> abstract in the markup.</p></div>
</body></html>
"""


class StubClient:
    """Serves pages by URL; anything unmapped raises, as a 404 would."""

    def __init__(self, pages: dict[str, str], fail: bool = False) -> None:
        self.pages = pages
        self.fail = fail
        self.calls: list[str] = []

    def get(self, url, params=None, headers=None):
        # Mirrors the real Client.get signature exactly; see the note on
        # StubClient in test_collect.py for why that matters.
        self.calls.append(url)
        if self.fail:
            raise HTTPError("simulated outage")
        try:
            return self.pages[url].encode("utf-8")
        except KeyError:
            raise HTTPError(f"GET {url} -> HTTP 404") from None


class ParseListingTests(unittest.TestCase):
    def test_extracts_papers_and_ignores_programme_furniture(self):
        entries = virtual_site.parse_listing(LISTING, "https://icml.cc")
        titles = sorted(e.title for e in entries)
        self.assertEqual(
            titles,
            [
                "A Paper About Nothing Tracked",
                "Causal Inference from Panel Data",
                "Instrumental Variable Bounds",
            ],
        )

    def test_collapses_repeated_links_to_one_paper(self):
        entries = virtual_site.parse_listing(LISTING, "https://icml.cc")
        self.assertEqual(len([e for e in entries if e.site_id == "31415"]), 1)

    def test_normalizes_url_kind_and_year(self):
        entries = virtual_site.parse_listing(LISTING, "https://icml.cc")
        oral = next(e for e in entries if e.site_id == "27182")
        self.assertEqual(oral.url, "https://icml.cc/virtual/2026/oral/27182")
        self.assertEqual(oral.kind, "oral")
        self.assertEqual(oral.year, 2026)

    def test_unrecognized_markup_yields_nothing_rather_than_junk(self):
        self.assertEqual(virtual_site.parse_listing("<html></html>", "https://x"), [])

    def test_the_navbar_login_link_is_not_a_paper(self):
        """It points at a poster path. Only the noscript block is parsed."""
        entries = virtual_site.parse_listing(LISTING, "https://icml.cc")
        self.assertNotIn("00000", [e.site_id for e in entries])
        self.assertNotIn("Login", [e.title for e in entries])

    def test_a_page_without_the_fallback_block_yields_nothing(self):
        """Not the shape we understand -- guessing at the rest invents papers."""
        page = '<html><body><li><a href="/virtual/2026/poster/1">X</a></li></body></html>'
        self.assertEqual(virtual_site.parse_listing(page, "https://x"), [])


class ParseDetailTests(unittest.TestCase):
    def test_reads_highwire_meta_tags(self):
        abstract, authors = virtual_site.parse_detail(DETAIL)
        self.assertEqual(authors, ["Ada Lovelace", "Alan Turing"])
        self.assertIn("instrumental variable", abstract)

    def test_falls_back_to_an_abstract_block(self):
        abstract, authors = virtual_site.parse_detail(DETAIL_NO_META)
        self.assertEqual(abstract, "A bare abstract in the markup.")
        self.assertEqual(authors, [])

    def test_missing_abstract_is_empty_not_invented(self):
        self.assertEqual(virtual_site.parse_detail("<html></html>"), ("", []))


class YearSweepTests(unittest.TestCase):
    def test_years_back_covers_the_current_cycle_and_the_previous_one(self):
        years = virtual_site._years({"years_back": 2}, date(2026, 8, 1), date(2026, 8, 1))
        self.assertEqual(years, [2026, 2025])

    def test_a_wide_backfill_reaches_further(self):
        years = virtual_site._years({"years_back": 2}, date(2023, 1, 1), date(2026, 8, 1))
        self.assertEqual(years, [2026, 2025, 2024, 2023])

    def test_a_split_year_lists_each_location(self):
        venue = {
            "virtual_host": "neurips.cc",
            "virtual_locations": {"2025": ["san-diego", "mexico-city"]},
        }
        urls = [url for _, url, _ in virtual_site._listing_urls(venue, [2026, 2025])]
        self.assertEqual(
            urls,
            [
                "https://neurips.cc/virtual/2026/papers.html",
                "https://neurips.cc/virtual/2025/loc/san-diego/papers.html",
                "https://neurips.cc/virtual/2025/loc/mexico-city/papers.html",
            ],
        )

    def test_a_venue_without_a_host_is_skipped(self):
        self.assertEqual(virtual_site._listing_urls({"name": "JMLR"}, [2026]), [])

    def test_a_venue_may_pin_its_own_years(self):
        """The venues are not on the same cycle; a shared window misses pages."""
        venue = {"virtual_host": "neurips.cc", "virtual_years": [2025, 2024]}
        urls = [url for _, url, _ in virtual_site._listing_urls(venue, [2026, 2025])]
        self.assertEqual(
            urls,
            [
                "https://neurips.cc/virtual/2025/papers.html",
                "https://neurips.cc/virtual/2024/papers.html",
            ],
        )


class CollectTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["conferences"] = {
            "enabled": True,
            "virtual_site": {"enabled": True, "years_back": 1, "fetch_details": True},
        }
        self.venues = [{"name": "ICML", "virtual_host": "icml.cc"}]
        self.today = date.today()
        self.listing_url = f"https://icml.cc/virtual/{self.today.year}/papers.html"

    def tearDown(self):
        self.sandbox.close()

    def _pages(self, **extra):
        listing = LISTING.replace("2026", str(self.today.year))
        pages = {self.listing_url: listing}
        pages.update(extra)
        return pages

    def _collect(self, client, errors=None):
        return virtual_site.collect(
            self.cfg, self.cfg.topics, self.venues, self.today, client, errors
        )

    def test_keeps_only_papers_a_topic_tracks(self):
        papers = self._collect(StubClient(self._pages()))
        titles = sorted(p.title for p in papers)
        self.assertEqual(
            titles, ["Causal Inference from Panel Data", "Instrumental Variable Bounds"]
        )

    def test_detail_pages_fill_the_abstract_and_authors(self):
        year = self.today.year
        detail = f"https://icml.cc/virtual/{year}/poster/31415"
        papers = self._collect(StubClient(self._pages(**{detail: DETAIL})))
        paper = next(p for p in papers if p.source_id.endswith("31415"))
        self.assertEqual(paper.authors, ["Ada Lovelace", "Alan Turing"])
        self.assertIn("instrumental variable", paper.abstract)

    def test_an_untracked_paper_costs_no_detail_request(self):
        client = StubClient(self._pages())
        self._collect(client)
        self.assertNotIn(f"https://icml.cc/virtual/{self.today.year}/poster/16180", client.calls)

    def test_details_can_be_switched_off(self):
        self.cfg.sources["conferences"]["virtual_site"]["fetch_details"] = False
        client = StubClient(self._pages())
        papers = self._collect(client)
        self.assertEqual(client.calls, [self.listing_url])
        self.assertTrue(all(p.abstract == "" for p in papers))

    def test_records_are_normalized(self):
        papers = self._collect(StubClient(self._pages()))
        paper = next(p for p in papers if p.title == "Instrumental Variable Bounds")
        self.assertEqual(paper.source, "virtualsite")
        # The venue carries the year: "accepted at ICML 2026" is the fact.
        self.assertEqual(paper.venue, f"ICML {self.today.year}")
        self.assertEqual(paper.year, self.today.year)
        self.assertTrue(paper.id.startswith("title:"))

    def test_an_unreachable_site_is_reported_not_raised(self):
        errors: list[str] = []
        self.assertEqual(self._collect(StubClient({}, fail=True), errors), [])
        self.assertTrue(any("virtual_site" in e for e in errors))

    def test_a_disabled_block_fetches_nothing(self):
        self.cfg.sources["conferences"]["virtual_site"]["enabled"] = False
        client = StubClient(self._pages())
        self.assertEqual(self._collect(client), [])
        self.assertEqual(client.calls, [])

    def test_the_detail_cap_bounds_the_requests(self):
        self.cfg.sources["conferences"]["virtual_site"]["max_details_per_run"] = 1
        client = StubClient(self._pages())
        self._collect(client)
        self.assertEqual(len(client.calls), 2)  # the listing, then one detail


if __name__ == "__main__":
    unittest.main()
