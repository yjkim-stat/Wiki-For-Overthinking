"""ACL Anthology collector tests.

The fixture is modelled on the live event page and keeps the two properties of
its markup that a parser written from memory gets wrong. **Attributes are not
quoted** — `href=/2024.acl-long.1/`, not `href="..."` — which is what an earlier
draft of the collector assumed and why it matched nothing at all. And the
abstract sits in a sibling `collapse` block keyed by the paper's id with its
dots doubled into hyphens, rather than inside the entry it belongs to.

The other thing asserted here is what an event *is*. An ACL event page carries
the conference, Findings, and every co-located workshop; a workshop paper is
published at the workshop, and filing it under the conference would put a false
claim in the archive. So the default keeps the venue's own tracks, and what it
leaves out is reported rather than dropped.
"""

from __future__ import annotations

import unittest
from datetime import date

from pipelines.collect import anthology
from pipelines.common.http import HTTPError

from .sandbox import Sandbox

MATCHING = "Causal inference with an instrumental variable, at scale."
OTHER = "A study of unrelated nonsense in low-resource settings."


def _entry(paper_id: str, title: str, abstract: str = "", authors=("Ada Lovelace",)) -> str:
    people = "\n|\n".join(f"<a href=/people/{a.lower().replace(' ', '-')}/>{a}</a>"
                          for a in authors)
    block = ""
    if abstract:
        key = paper_id.replace(".", "--")
        block = (f'<div class="card bg-light mb-2 collapse abstract-collapse" '
                 f'id=abstract-{key}><div class="card-body p-3 small">{abstract}</div></div>')
    return (f'<span class=d-block><strong><a class=align-middle href=/{paper_id}/>'
            f'{title}</a></strong><br>{people}</span></div>{block}')


def _page(*entries: str) -> str:
    return "<html><body>" + "".join(entries) + "</body></html>"


EVENT = _page(
    _entry("2024.naacl-long.0", "Proceedings of the 2024 Conference"),
    _entry("2024.naacl-long.1", MATCHING, "An abstract about causal inference.",
           ("Ada Lovelace", "Alan Turing")),
    _entry("2024.findings-naacl.7", "Instrumental variable estimation revisited",
           "More on instrumental variable methods."),
    _entry("2024.woah-1.24", MATCHING, "A workshop paper about causal inference."),
    _entry("2024.naacl-short.3", OTHER, "Nothing a topic here tracks."),
)


class StubClient:
    def __init__(self, pages: dict[str, str], fail: bool = False) -> None:
        self.pages = pages
        self.fail = fail
        self.calls: list[str] = []

    def get(self, url, params=None, headers=None):
        self.calls.append(url)
        if self.fail:
            raise HTTPError("simulated outage")
        body = self.pages.get(url)
        if body is None:
            raise HTTPError(f"GET {url} -> HTTP 404")
        return body.encode("utf-8")


class ParseTests(unittest.TestCase):
    def test_an_entry_is_read_from_unquoted_markup(self):
        """The trap. A pattern written for `href="..."` finds nothing here."""
        entries = {e.anthology_id: e for e in anthology.parse_event(EVENT)}
        entry = entries["2024.naacl-long.1"]
        self.assertEqual(entry.title, MATCHING)
        self.assertEqual(entry.authors, ["Ada Lovelace", "Alan Turing"])
        self.assertIn("causal inference", entry.abstract)

    def test_each_abstract_goes_to_the_paper_it_belongs_to(self):
        entries = {e.anthology_id: e for e in anthology.parse_event(EVENT)}
        self.assertIn("instrumental variable", entries["2024.findings-naacl.7"].abstract)
        self.assertIn("workshop", entries["2024.woah-1.24"].abstract)

    def test_a_paper_without_an_abstract_does_not_borrow_a_neighbour_s(self):
        """Why the block is keyed by id rather than taken as the next one.

        An entry's slice runs to the following entry's anchor, so a stray
        abstract block inside it — one belonging to a paper listed elsewhere on
        the page — is exactly what a positional match would pick up. Silently
        attaching the wrong abstract is worse than attaching none: the record
        looks complete, and it is read, scored and archived against text from a
        different paper.
        """
        stray = ('<div class="card collapse abstract-collapse" '
                 'id=abstract-2024--naacl-long--99><div class="card-body p-3 small">'
                 'Text belonging to a different paper.</div></div>')
        page = _page(
            _entry("2024.naacl-demo.2", "A demo with no abstract of its own") + stray,
            _entry("2024.naacl-long.4", "Another paper", "Its own abstract."),
        )
        entries = {e.anthology_id: e for e in anthology.parse_event(page)}
        self.assertEqual(entries["2024.naacl-demo.2"].abstract, "")
        self.assertEqual(entries["2024.naacl-long.4"].abstract, "Its own abstract.")

    def test_front_matter_is_not_a_paper(self):
        ids = [e.anthology_id for e in anthology.parse_event(EVENT)]
        self.assertNotIn("2024.naacl-long.0", ids)

    def test_the_volume_is_recorded(self):
        volumes = {e.anthology_id: e.volume for e in anthology.parse_event(EVENT)}
        self.assertEqual(volumes["2024.findings-naacl.7"], "findings-naacl")
        self.assertEqual(volumes["2024.woah-1.24"], "woah-1")

    def test_an_entry_without_an_abstract_still_parses(self):
        page = _page(_entry("2024.naacl-long.9", "A title and nothing else"))
        entry = anthology.parse_event(page)[0]
        self.assertEqual(entry.abstract, "")
        self.assertEqual(entry.title, "A title and nothing else")

    def test_the_same_paper_listed_twice_is_one_entry(self):
        page = _page(_entry("2024.naacl-long.1", MATCHING),
                     _entry("2024.naacl-long.1", MATCHING))
        self.assertEqual(len(anthology.parse_event(page)), 1)

    def test_markup_running_through_a_word_does_not_split_it(self):
        """`acl-fixed-case` spans wrap letters mid-word to protect their case.

        Replacing a tag with a space is the right default for a page of prose
        and wrong here: it turns "InsCL:" into "I ns CL :", which then fails to
        match a keyword, mis-sorts in the index, and titles a wiki note with a
        name that appears in no paper.
        """
        page = _page(_entry(
            "2024.naacl-long.37",
            "<span class=acl-fixed-case>I</span>ns<span class=acl-fixed-case>CL"
            "</span>: A Data-efficient Paradigm",
        ))
        self.assertEqual(anthology.parse_event(page)[0].title,
                         "InsCL: A Data-efficient Paradigm")

    def test_a_line_break_is_still_a_space(self):
        page = _page(_entry("2024.naacl-long.38", "First part<br>second part"))
        self.assertEqual(anthology.parse_event(page)[0].title,
                         "First part second part")

    def test_entities_are_decoded(self):
        page = _page(_entry("2024.naacl-long.39", "Caf&eacute; conversations"))
        self.assertEqual(anthology.parse_event(page)[0].title, "Café conversations")

    def test_the_doi_follows_from_the_identifier(self):
        entry = anthology.parse_event(_page(_entry("2024.acl-long.5", "T")))[0]
        self.assertEqual(entry.doi, "10.18653/v1/2024.acl-long.5")


class VolumeTests(unittest.TestCase):
    def test_the_default_is_the_venue_and_its_findings(self):
        self.assertEqual(anthology.wanted_volumes("acl", None),
                         ["acl-", "findings-acl"])

    def test_an_explicit_list_wins(self):
        self.assertEqual(anthology.wanted_volumes("acl", ["ACL-Long"]), ["acl-long"])

    def test_a_workshop_is_not_the_conference(self):
        keep = anthology.wanted_volumes("naacl", None)
        self.assertTrue(anthology._keeps("naacl-long", keep))
        self.assertTrue(anthology._keeps("findings-naacl", keep))
        self.assertFalse(anthology._keeps("woah-1", keep))
        self.assertFalse(anthology._keeps("semeval-1", keep))


class CollectTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.cfg.sources.setdefault("conferences", {})["anthology"] = {
            "enabled": True,
            "base_url": "https://anthology.test",
            "years": [2024],
        }
        self.venues = [{"name": "NAACL", "anthology_key": "naacl"}]
        self.url = "https://anthology.test/events/naacl-2024/"
        self.topics = self.cfg.topics

    def _collect(self, client, errors=None, venues=None):
        return anthology.collect(
            self.cfg, self.topics, venues if venues is not None else self.venues,
            date(2024, 1, 1), client, errors,
        )

    def test_a_matching_paper_becomes_a_record(self):
        papers = self._collect(StubClient({self.url: EVENT}))
        by_id = {p.id: p for p in papers}
        paper = by_id["doi:10.18653/v1/2024.naacl-long.1"]
        self.assertEqual(paper.venue, "NAACL")
        self.assertEqual(paper.year, 2024)
        self.assertEqual(paper.source, "anthology")
        self.assertEqual(paper.url, "https://anthology.test/2024.naacl-long.1/")
        self.assertIn("causal inference", paper.abstract)

    def test_the_abstract_arrives_with_the_record(self):
        """The whole reason this collector is cheaper than a listing crawl:
        one request per venue-year, and nothing needs fetching afterwards."""
        client = StubClient({self.url: EVENT})
        papers = self._collect(client)
        self.assertEqual(len(client.calls), 1)
        self.assertTrue(all(p.abstract for p in papers))

    def test_a_workshop_paper_is_not_filed_under_the_conference(self):
        papers = self._collect(StubClient({self.url: EVENT}))
        self.assertNotIn("doi:10.18653/v1/2024.woah-1.24", {p.id for p in papers})

    def test_what_was_left_out_is_reported(self):
        """No silent caps: a run that halved its own reach must say so."""
        with self.assertLogs("pipelines.collect.anthology", level="INFO") as logs:
            self._collect(StubClient({self.url: EVENT}))
        said = "\n".join(logs.output)
        self.assertIn("left out", said)
        self.assertIn("woah-1", said)

    def test_a_paper_no_topic_wants_is_dropped(self):
        papers = self._collect(StubClient({self.url: EVENT}))
        self.assertNotIn("doi:10.18653/v1/2024.naacl-short.3", {p.id for p in papers})

    def test_a_venue_without_a_key_is_not_fetched(self):
        client = StubClient({self.url: EVENT})
        papers = self._collect(client, venues=[{"name": "NeurIPS"}])
        self.assertEqual(papers, [])
        self.assertEqual(client.calls, [])

    def test_a_year_the_venue_did_not_run_is_not_a_fault(self):
        self.cfg.sources["conferences"]["anthology"]["years"] = [2024, 2199]
        errors: list[str] = []
        papers = self._collect(StubClient({self.url: EVENT}), errors)
        self.assertTrue(papers)
        self.assertEqual(errors, [])

    def test_every_request_failing_is_reported(self):
        errors: list[str] = []
        self.assertEqual(self._collect(StubClient({}, fail=True), errors), [])
        self.assertTrue(any("anthology" in e for e in errors), errors)

    def test_a_page_over_the_cap_is_refused_rather_than_parsed(self):
        self.cfg.sources["conferences"]["anthology"]["max_bytes"] = 10
        with self.assertLogs("pipelines.collect.anthology", level="WARNING") as logs:
            self.assertEqual(self._collect(StubClient({self.url: EVENT})), [])
        self.assertIn("over the cap", "\n".join(logs.output))

    def test_a_page_that_parses_to_nothing_says_the_shape_may_have_changed(self):
        with self.assertLogs("pipelines.collect.anthology", level="WARNING") as logs:
            self._collect(StubClient({self.url: "<html>nothing here</html>"}))
        self.assertIn("shape", "\n".join(logs.output))

    def test_disabling_it_makes_no_requests(self):
        self.cfg.sources["conferences"]["anthology"]["enabled"] = False
        client = StubClient({self.url: EVENT})
        self.assertEqual(self._collect(client), [])
        self.assertEqual(client.calls, [])


if __name__ == "__main__":
    unittest.main()
