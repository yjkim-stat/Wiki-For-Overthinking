"""Curated-list collector tests.

The fixtures below are what these tests actually assert about, so they carry
the three things that matter about a real weekly list: the entry text is a
nickname and a paragraph of commentary rather than a bibliography, the
commentary cites work the editor did *not* pick, and some picks are not papers
on arXiv at all.
"""

from __future__ import annotations

import unittest
import xml.etree.ElementTree as ET
from datetime import date

from pipelines.collect import curated
from pipelines.common.http import HTTPError
from pipelines.common.schema import Paper
from pipelines.common.store import RecordStore

from .sandbox import Sandbox

INDEX_URL = "https://example.test/list/README.md"
YEAR_2026_URL = "https://example.test/list/years/2026.md"
YEAR_2025_URL = "https://example.test/list/years/2025.md"

INDEX = """
# Papers of the Week

[Subscribe to the newsletter](https://example.test/newsletter) for these by mail.

## 2026
- [Top Papers (July 27 - August 2)](years/2026.md#top-papers-july-27---august-2---2026)
- [Top Papers (July 20 - July 26)](years/2026.md#top-papers-july-20---july-26---2026)

## 2025
- [Top Papers (December 22 - December 28)](years/2025.md#top-papers-december-22---december-28---2025)
"""

YEAR_2026 = """
# Papers of the Week - 2026

[Back to the index](../README.md)

## Top Papers (July 27 - August 2) - 2026
| **Paper** | **Links** |
| --- | --- |
| 1) **NOOA** - A nickname, not a title. Extends [an earlier idea](https://arxiv.org/abs/2101.11111) that the editor did not pick. | [Paper](https://arxiv.org/abs/2607.20709), [Tweet](https://x.test/a/1) |
| 2) **GEOCALC** - A pick with no bibliography anywhere to read it from. | [Paper](https://www.example.test/blog/geometric-calculator) |

## Top Papers (July 20 - July 26) - 2026
| **Paper** | **Links** |
| --- | --- |
| 1) **ReOPD** - Another nickname. | [Paper](https://arxiv.org/abs/2607.04763v2), [Tweet](https://x.test/a/2) |

## How this list is made
Every week we read [everything](https://arxiv.org/abs/2001.99999) and pick ten.
"""

YEAR_2025 = """
# Papers of the Week - 2025

## Top Papers (December 22 - December 28) - 2025
| **Paper** | **Links** |
| --- | --- |
| 1) **OLDER** - From last year. | [Paper](https://arxiv.org/abs/2512.00001) |
"""

# One page, no index of issues: the shape a plain "awesome list" has.
SINGLE_PAGE = """
# An Awesome List

## Recently
- **THING** - a pick. [Paper](https://arxiv.org/abs/2606.00001)
"""

ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2607.20709v1</id>
    <title>Object-Oriented Agents for Causal Inference Tooling</title>
    <summary>We study instrumental variable estimation inside an agent
      framework.</summary>
    <published>2026-07-28T00:00:00Z</published>
    <updated>2026-07-28T00:00:00Z</updated>
    <author><name>Ada Lovelace</name></author>
    <link title="pdf" href="https://arxiv.org/pdf/2607.20709v1"/>
  </entry>
</feed>
"""


class StubClient:
    """Serves pages by URL; anything unmapped raises, as a 404 would."""

    def __init__(self, pages: dict[str, str], fail: bool = False) -> None:
        self.pages = pages
        self.fail = fail
        self.calls: list[str] = []
        self.id_lists: list[str] = []

    def get(self, url, params=None, headers=None):
        self.calls.append(url)
        if self.fail:
            raise HTTPError("simulated outage")
        try:
            return self.pages[url].encode("utf-8")
        except KeyError:
            raise HTTPError(f"GET {url} -> HTTP 404") from None

    def get_xml(self, url, params=None, headers=None):
        # Stands in for the arXiv id lookup the collector delegates to.
        self.id_lists.append((params or {}).get("id_list", ""))
        return ET.fromstring(ATOM)


def _pages() -> dict[str, str]:
    return {
        INDEX_URL: INDEX,
        YEAR_2026_URL: YEAR_2026,
        YEAR_2025_URL: YEAR_2025,
    }


def _sandbox(**block) -> Sandbox:
    """A sandbox whose sources.yaml carries a curated list."""
    options = {"enabled": True, "max_issues": 4, "link_label": "Paper", **block}
    lines = [
        "arxiv:",
        "  enabled: false",
        "  categories: [stat.ML]",
        "conferences:",
        "  enabled: false",
        "  venues: []",
        "youtube:",
        "  enabled: false",
        "  channels: []",
        "curated:",
    ]
    for key, value in options.items():
        rendered = str(value).lower() if isinstance(value, bool) else value
        lines.append(f"  {key}: {rendered}")
    lines += [
        "  lists:",
        '    - name: "Test Weekly"',
        f'      url: "{INDEX_URL}"',
    ]
    sandbox = Sandbox()
    (sandbox.root / "config" / "sources.yaml").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    return sandbox


class ReadListTests(unittest.TestCase):
    def test_reads_the_issues_the_index_points_at_newest_first(self):
        client = StubClient(_pages())
        ids, others, issues = curated._read_list(client, INDEX_URL, 4, "Paper")
        self.assertEqual(
            issues,
            [
                "Top Papers (July 27 - August 2) - 2026",
                "Top Papers (July 20 - July 26) - 2026",
                "Top Papers (December 22 - December 28) - 2025",
            ],
        )
        self.assertEqual(ids, ["2607.20709", "2607.04763", "2512.00001"])
        self.assertEqual(others, ["https://www.example.test/blog/geometric-calculator"])

    def test_a_paper_the_commentary_merely_cites_is_not_a_pick(self):
        """Following those would archive what was mentioned, not what was chosen."""
        ids, _, _ = curated._read_list(StubClient(_pages()), INDEX_URL, 4, "Paper")
        self.assertNotIn("2101.11111", ids)

    def test_a_section_the_index_does_not_list_is_not_an_issue(self):
        ids, _, issues = curated._read_list(StubClient(_pages()), INDEX_URL, 4, "Paper")
        self.assertNotIn("How this list is made", issues)
        self.assertNotIn("2001.99999", ids)

    def test_version_suffixes_are_stripped_so_v1_and_v2_are_one_paper(self):
        ids, _, _ = curated._read_list(StubClient(_pages()), INDEX_URL, 4, "Paper")
        self.assertIn("2607.04763", ids)

    def test_max_issues_bounds_the_read_and_takes_the_newest(self):
        ids, _, issues = curated._read_list(StubClient(_pages()), INDEX_URL, 1, "Paper")
        self.assertEqual(issues, ["Top Papers (July 27 - August 2) - 2026"])
        self.assertEqual(ids, ["2607.20709"])

    def test_only_the_pages_the_selected_issues_live_on_are_fetched(self):
        client = StubClient(_pages())
        curated._read_list(client, INDEX_URL, 1, "Paper")
        self.assertNotIn(YEAR_2025_URL, client.calls)

    def test_a_page_is_fetched_once_however_many_issues_it_holds(self):
        client = StubClient(_pages())
        curated._read_list(client, INDEX_URL, 2, "Paper")
        self.assertEqual(client.calls.count(YEAR_2026_URL), 1)

    def test_a_list_with_no_index_is_read_as_one_issue(self):
        client = StubClient({INDEX_URL: SINGLE_PAGE})
        ids, _, issues = curated._read_list(client, INDEX_URL, 4, "Paper")
        self.assertEqual(issues, ["Recently"])
        self.assertEqual(ids, ["2606.00001"])
        self.assertEqual(client.calls, [INDEX_URL])

    def test_headings_that_match_no_anchor_fall_back_to_page_order_and_warn(self):
        """Silence here would read the same age of issue forever."""
        renamed = YEAR_2026.replace("Top Papers", "Weekly Roundup")
        client = StubClient({INDEX_URL: INDEX, YEAR_2026_URL: renamed, YEAR_2025_URL: YEAR_2025})
        with self.assertLogs("pipelines.collect.curated", level="WARNING") as logs:
            ids, _, issues = curated._read_list(client, INDEX_URL, 1, "Paper")
        self.assertIn("falling back to page order", "\n".join(logs.output))
        self.assertEqual(issues, ["Weekly Roundup (July 27 - August 2) - 2026"])
        self.assertEqual(ids, ["2607.20709"])

    def test_an_unlabelled_list_falls_back_to_any_arxiv_link(self):
        page = "## Week\n- **X** - see [here](https://arxiv.org/abs/2605.00002).\n"
        ids, _, _ = curated._read_list(StubClient({INDEX_URL: page}), INDEX_URL, 4, "Paper")
        self.assertEqual(ids, ["2605.00002"])


class CollectTests(unittest.TestCase):
    def test_the_bibliography_comes_from_arxiv_not_from_the_nickname(self):
        with _sandbox(max_issues=1) as sandbox:
            cfg = sandbox.config()
            client = StubClient(_pages())
            papers = curated.collect(
                cfg, cfg.topics, date(2026, 8, 1), store=RecordStore(cfg.layout),
                client=client,
            )
        self.assertEqual(len(papers), 1)
        self.assertEqual(
            papers[0].title, "Object-Oriented Agents for Causal Inference Tooling"
        )
        self.assertNotIn("NOOA", papers[0].title)
        self.assertEqual(papers[0].authors, ["Ada Lovelace"])
        self.assertEqual(papers[0].source, "curated")

    def test_a_pick_with_no_arxiv_id_is_skipped_and_named(self):
        with _sandbox(max_issues=1) as sandbox:
            cfg = sandbox.config()
            with self.assertLogs("pipelines.collect.curated", level="INFO") as logs:
                papers = curated.collect(
                    cfg, cfg.topics, date(2026, 8, 1),
                    store=RecordStore(cfg.layout), client=StubClient(_pages()),
                )
        self.assertEqual([p.id for p in papers], ["arxiv:2607.20709"])
        self.assertIn("geometric-calculator", "\n".join(logs.output))

    def test_a_pick_already_held_is_re_emitted_so_dedup_can_stamp_it(self):
        with _sandbox(max_issues=1) as sandbox:
            cfg = sandbox.config()
            store = RecordStore(cfg.layout)
            store.save_paper(
                Paper(
                    id="arxiv:2607.20709",
                    title="Object-Oriented Agents for Causal Inference Tooling",
                    source="arxiv",
                    abstract="Already collected from arXiv itself.",
                )
            )
            client = StubClient(_pages())
            papers = curated.collect(
                cfg, cfg.topics, date(2026, 8, 1), store=store, client=client,
            )
        self.assertEqual([p.source for p in papers], ["curated"])
        self.assertEqual(papers[0].title, "Object-Oriented Agents for Causal Inference Tooling")
        # No lookup: the archive already had the bibliography.
        self.assertEqual(client.id_lists, [])

    def test_an_unreachable_list_is_recorded_and_returns_nothing(self):
        with _sandbox() as sandbox:
            cfg = sandbox.config()
            errors: list[str] = []
            papers = curated.collect(
                cfg, cfg.topics, date(2026, 8, 1),
                store=RecordStore(cfg.layout),
                client=StubClient({}, fail=True), errors=errors,
            )
        self.assertEqual(papers, [])
        self.assertTrue(any("curated[Test Weekly]" in e for e in errors))

    def test_a_list_that_parses_to_nothing_says_so(self):
        """The format is one editor's markdown; a silent zero would look normal."""
        with _sandbox() as sandbox:
            cfg = sandbox.config()
            with self.assertLogs("pipelines.collect.curated", level="WARNING") as logs:
                papers = curated.collect(
                    cfg, cfg.topics, date(2026, 8, 1),
                    store=RecordStore(cfg.layout),
                    client=StubClient({INDEX_URL: "# Nothing here\n"}),
                )
        self.assertEqual(papers, [])
        self.assertIn("format may have changed", "\n".join(logs.output))

    def test_a_disabled_block_collects_nothing(self):
        with _sandbox(enabled=False) as sandbox:
            cfg = sandbox.config()
            papers = curated.collect(
                cfg, cfg.topics, date(2026, 8, 1),
                store=RecordStore(cfg.layout), client=StubClient(_pages()),
            )
        self.assertEqual(papers, [])


if __name__ == "__main__":
    unittest.main()
