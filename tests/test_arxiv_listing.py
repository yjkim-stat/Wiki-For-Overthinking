"""arXiv listing collector tests.

The fixture below is what these tests actually assert about. It is modelled on
the definition-list shape the listing pages have used for years — a ``<dt>``
carrying the identifier and a ``<dd>`` carrying ``list-title`` / ``list-authors``
/ ``list-subjects`` — and it is the first file to correct if arXiv changes the
page underneath the collector.
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


class ParseListingTests(unittest.TestCase):
    def test_every_announcement_is_extracted(self):
        entries = arxiv_listing.parse_listing(LISTING)
        self.assertEqual([e.arxiv_id for e in entries], ["2501.00001", "2501.00002"])

    def test_the_title_loses_its_descriptor_label(self):
        entries = arxiv_listing.parse_listing(LISTING)
        self.assertEqual(entries[0].title, "Causal Inference from Panel Data")

    def test_a_title_containing_a_colon_survives(self):
        entries = arxiv_listing.parse_listing(page(_entry("2501.00007", "RoCA: Robust Driving")))
        self.assertEqual(entries[0].title, "RoCA: Robust Driving")

    def test_authors_and_categories_are_read(self):
        entries = arxiv_listing.parse_listing(LISTING)
        self.assertEqual(entries[0].authors, ["Ada Lovelace", "Alan Turing"])
        self.assertIn("cs.CL", entries[0].categories)
        self.assertIn("cs.LG", entries[0].categories)

    def test_a_sidebar_abs_link_is_not_an_announcement(self):
        """Only a link inside a <dt> paired with a <dd> is an entry."""
        ids = [e.arxiv_id for e in arxiv_listing.parse_listing(LISTING)]
        self.assertNotIn("0000.00000", ids)

    def test_the_version_suffix_is_stripped(self):
        entries = arxiv_listing.parse_listing(page(_entry("2501.00003v2", "Titled")))
        self.assertEqual(entries[0].arxiv_id, "2501.00003")

    def test_an_entry_with_no_readable_title_is_dropped(self):
        broken = "<dt><a href=\"/abs/2501.00009\">arXiv:2501.00009</a></dt><dd></dd>"
        self.assertEqual(arxiv_listing.parse_listing(page(broken)), [])

    def test_unrecognized_markup_yields_nothing_rather_than_junk(self):
        self.assertEqual(arxiv_listing.parse_listing("<html></html>"), [])

    def test_the_total_is_read_for_pagination(self):
        self.assertEqual(arxiv_listing.parse_total(page("", total=1234)), 1234)

    def test_a_page_that_does_not_say_a_total_reports_zero(self):
        self.assertEqual(arxiv_listing.parse_total("<html></html>"), 0)


class ParseAbstractTests(unittest.TestCase):
    def test_the_citation_meta_tag_wins(self):
        self.assertIn("instrumental", arxiv_listing.parse_abstract(ABS_PAGE))

    def test_the_blockquote_is_the_fallback(self):
        page_html = (
            '<blockquote class="abstract mathjax">'
            '<span class="descriptor">Abstract:</span> A bare abstract.'
            "</blockquote>"
        )
        self.assertEqual(arxiv_listing.parse_abstract(page_html), "A bare abstract.")

    def test_no_abstract_is_empty_not_invented(self):
        self.assertEqual(arxiv_listing.parse_abstract("<html></html>"), "")


class CollectTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"] = {
            "enabled": True,
            "categories": ["cs.CL"],
            "listing": {"mode": "always", "page_size": 250, "max_pages": 3},
        }
        self.url = "https://arxiv.org/list/cs.CL/recent"

    def tearDown(self):
        self.sandbox.close()

    def _collect(self, client, errors=None):
        return arxiv_listing.collect(self.cfg, self.cfg.topics, date.today(), client, errors)

    def test_only_titles_a_topic_tracks_are_kept(self):
        papers = self._collect(StubClient({self.url: LISTING}))
        self.assertEqual([p.title for p in papers], ["Causal Inference from Panel Data"])

    def test_records_carry_an_arxiv_id_so_dedupe_can_merge(self):
        papers = self._collect(StubClient({self.url: LISTING}))
        self.assertEqual(papers[0].id, "arxiv:2501.00001")
        self.assertEqual(papers[0].source, "arxiv")
        self.assertTrue(papers[0].pdf_url.endswith("2501.00001"))

    def test_a_match_costs_one_abstract_request(self):
        client = StubClient({
            self.url: LISTING,
            "https://arxiv.org/abs/2501.00001": ABS_PAGE,
        })
        papers = self._collect(client)
        self.assertIn("instrumental", papers[0].abstract)
        self.assertIn("https://arxiv.org/abs/2501.00001", [c[0] for c in client.calls])

    def test_an_untracked_title_costs_no_abstract_request(self):
        client = StubClient({self.url: LISTING})
        self._collect(client)
        self.assertNotIn("https://arxiv.org/abs/2501.00002", [c[0] for c in client.calls])

    def test_abstract_fetching_can_be_switched_off(self):
        self.cfg.sources["arxiv"]["listing"]["fetch_abstracts"] = False
        client = StubClient({self.url: LISTING})
        papers = self._collect(client)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(papers[0].abstract, "")

    def test_pagination_walks_until_the_total_is_covered(self):
        full = page(
            "".join(_entry(f"2501.{i:05d}", "Causal inference study") for i in range(2)),
            total=4,
        )
        client = StubClient({
            f"{self.url}?skip=0": full,
            f"{self.url}?skip=2": page(
                "".join(
                    _entry(f"2501.{i:05d}", "Causal inference study") for i in range(2, 4)
                ),
                total=4,
            ),
            f"{self.url}?skip=4": page("", total=4),
        })
        self.cfg.sources["arxiv"]["listing"]["page_size"] = 2
        self.cfg.sources["arxiv"]["listing"]["fetch_abstracts"] = False
        papers = self._collect(client)
        self.assertEqual(len(papers), 4)
        self.assertEqual([c[1]["skip"] for c in client.calls], [0, 2])

    def test_max_pages_bounds_the_crawl(self):
        """arXiv asks not to be crawled hard; the bound is not advisory."""
        big = page("".join(_entry(f"2501.{i:05d}", "Causal study") for i in range(2)),
                   total=1000)
        client = StubClient({f"{self.url}?skip={i * 2}": big for i in range(10)})
        self.cfg.sources["arxiv"]["listing"]["page_size"] = 2
        self.cfg.sources["arxiv"]["listing"]["max_pages"] = 3
        self.cfg.sources["arxiv"]["listing"]["fetch_abstracts"] = False
        self._collect(client)
        self.assertEqual(len(client.calls), 3)

    def test_a_dead_listing_is_reported_not_raised(self):
        errors: list[str] = []
        self.assertEqual(self._collect(StubClient({}, fail=True), errors), [])
        self.assertTrue(any("arxiv_listing" in e for e in errors))

    def test_no_categories_means_no_requests(self):
        self.cfg.sources["arxiv"]["categories"] = []
        client = StubClient({self.url: LISTING})
        self.assertEqual(self._collect(client), [])
        self.assertEqual(client.calls, [])


class FallbackModeTests(unittest.TestCase):
    """`auto` reaches for the listing only when the API produced nothing."""

    def setUp(self):
        self.sandbox = Sandbox()
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

    class _Client(StubClient):
        """The API answers with an empty Atom feed; the listing answers HTML."""

        def get_xml(self, url, params=None, headers=None):
            import xml.etree.ElementTree as ET

            self.calls.append((url, dict(params or {})))
            return ET.fromstring('<feed xmlns="http://www.w3.org/2005/Atom"/>')

    def test_an_empty_api_result_falls_through_to_the_listing(self):
        client = self._Client({self.url: LISTING})
        papers = arxiv.collect(self.cfg, self.cfg.topics, date(2025, 1, 1), client=client)
        self.assertEqual([p.id for p in papers], ["arxiv:2501.00001"])

    def test_never_means_the_api_result_stands(self):
        self.cfg.sources["arxiv"]["listing"]["mode"] = "never"
        client = self._Client({self.url: LISTING})
        self.assertEqual(
            arxiv.collect(self.cfg, self.cfg.topics, date(2025, 1, 1), client=client), []
        )
        self.assertNotIn(self.url, [c[0] for c in client.calls])


if __name__ == "__main__":
    unittest.main()
