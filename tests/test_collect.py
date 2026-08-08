"""Collector tests against recorded responses.

The collectors talk to third-party APIs, so the parsing has to be verified
without a network: these feed each one a captured payload through a stub client
and check that it lands in the normalized schema correctly.
"""

from __future__ import annotations

import json
import os
import unittest
import xml.etree.ElementTree as ET
from datetime import date
from unittest import mock

from pipelines.collect import arxiv, conferences, youtube
from pipelines.common.http import HTTPError

from .sandbox import Sandbox

ARXIV_ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2401.12345v2</id>
    <updated>2024-02-01T10:00:00Z</updated>
    <published>2024-01-22T09:30:00Z</published>
    <title>Causal Inference
      from Panel Data</title>
    <summary>  We estimate treatment effects with an instrumental variable.  </summary>
    <author><name>Ada Lovelace</name></author>
    <author><name>Alan Turing</name></author>
    <arxiv:doi>10.1000/example</arxiv:doi>
    <arxiv:journal_ref>NeurIPS 2024</arxiv:journal_ref>
    <link href="http://arxiv.org/abs/2401.12345v2" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/2401.12345v2" rel="related"/>
    <category term="stat.ML" scheme="http://arxiv.org/schemas/atom"/>
    <category term="cs.LG" scheme="http://arxiv.org/schemas/atom"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2402.00001v1</id>
    <published>2024-02-02T00:00:00Z</published>
    <title>Unrelated Chemistry Paper</title>
    <summary>Nothing to do with the tracked topic.</summary>
    <author><name>Someone Else</name></author>
  </entry>
</feed>
"""

YOUTUBE_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:yt="http://www.youtube.com/xml/schemas/2015"
      xmlns:media="http://search.yahoo.com/mrss/">
  <entry>
    <yt:videoId>abc123XYZ</yt:videoId>
    <yt:channelId>UC0000000000000000000000</yt:channelId>
    <title>Causal inference in observational studies</title>
    <author><name>Research Seminar</name></author>
    <published>2024-03-01T12:00:00+00:00</published>
    <media:group>
      <media:description>A talk on instrumental variables.</media:description>
    </media:group>
  </entry>
</feed>
"""

SEMANTIC_SCHOLAR = {
    "total": 1,
    "data": [
        {
            "paperId": "abcdef",
            "title": "A Doubly Robust Estimator",
            "abstract": "We study doubly robust estimation.",
            "venue": "ICLR",
            "year": 2025,
            "publicationDate": "2025-01-10",
            "authors": [{"name": "Grace Hopper"}],
            "externalIds": {"ArXiv": "2501.00002", "DOI": "10.1000/ws"},
            "url": "https://www.semanticscholar.org/paper/abcdef",
            "openAccessPdf": {"url": "https://example.org/paper.pdf"},
        }
    ],
}

OPENREVIEW = {
    "notes": [
        {
            "id": "note123",
            "content": {
                "title": {"value": "Instrumental Variable Estimation"},
                "abstract": {"value": "We estimate effects under weak instruments."},
                "authors": {"value": ["Barbara Liskov"]},
                "pdf": {"value": "/pdf/note123.pdf"},
                "venue": {"value": "ICLR 2025 Poster"},
            },
        }
    ]
}

DBLP = {
    "result": {
        "hits": {
            "hit": [
                {
                    "info": {
                        "key": "conf/iclr/Example25",
                        "title": "A Causal Inference Paper.",
                        "authors": {"author": [{"text": "Donald Knuth"}]},
                        "venue": "ICLR",
                        "year": "2025",
                        "doi": "10.1000/dblp",
                        "ee": "https://doi.org/10.1000/dblp",
                    }
                }
            ]
        }
    }
}


class StubClient:
    """Returns canned payloads, or raises to simulate an unreachable host.

    The signatures mirror the real ``Client`` exactly, including the named
    ``headers`` parameter. An earlier version absorbed it through ``**kw``, and
    that permissiveness is what let a `TypeError` in ``Client.get_json`` — one
    that disabled the Semantic Scholar collector outright — pass the whole
    suite. A stub looser than the thing it stands in for tests nothing.
    """

    def __init__(self, xml: str = "", payload=None, fail: bool = False) -> None:
        self.xml = xml
        self.payload = payload
        self.fail = fail
        self.calls: list[tuple[str, dict]] = []
        self.headers: list[dict] = []

    def _record(self, url, params, headers):
        self.calls.append((url, params or {}))
        self.headers.append(dict(headers or {}))
        if self.fail:
            raise HTTPError("simulated outage")

    def get_xml(self, url, params=None, headers=None):
        self._record(url, params, headers)
        return ET.fromstring(self.xml)

    def get_json(self, url, params=None, headers=None):
        self._record(url, params, headers)
        return json.loads(json.dumps(self.payload))


class ArxivTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["arxiv"]["enabled"] = True

    def tearDown(self):
        self.sandbox.close()

    def _collect(self, client, errors=None):
        return arxiv.collect(
            self.cfg, self.cfg.topics, date(2024, 1, 1), client=client, errors=errors
        )

    def test_parses_every_entry(self):
        papers = self._collect(StubClient(xml=ARXIV_ATOM))
        self.assertEqual(len(papers), 2)

    def test_fields_are_normalized(self):
        papers = {p.id: p for p in self._collect(StubClient(xml=ARXIV_ATOM))}
        paper = papers["arxiv:2401.12345"]
        self.assertEqual(paper.title, "Causal Inference from Panel Data")
        self.assertEqual(paper.authors, ["Ada Lovelace", "Alan Turing"])
        self.assertEqual(
            paper.abstract, "We estimate treatment effects with an instrumental variable."
        )
        self.assertEqual(paper.published, "2024-01-22")
        self.assertEqual(paper.year, 2024)
        self.assertEqual(paper.doi, "10.1000/example")
        self.assertEqual(paper.venue, "NeurIPS 2024")
        self.assertEqual(paper.categories, ["stat.ML", "cs.LG"])
        self.assertEqual(paper.pdf_url, "http://arxiv.org/pdf/2401.12345v2")
        self.assertEqual(paper.url, "https://arxiv.org/abs/2401.12345")

    def test_version_suffix_does_not_reach_the_id(self):
        ids = {p.id for p in self._collect(StubClient(xml=ARXIV_ATOM))}
        self.assertIn("arxiv:2401.12345", ids)
        self.assertNotIn("arxiv:2401.12345v2", ids)

    def test_query_carries_categories_and_date_window(self):
        client = StubClient(xml=ARXIV_ATOM)
        self._collect(client)
        query = client.calls[0][1]["search_query"]
        self.assertIn("cat:stat.ML", query)
        self.assertIn('all:"causal inference"', query)
        self.assertIn("submittedDate:[20240101", query)

    def test_long_keyword_lists_are_split_across_requests(self):
        self.cfg.topics[0].keywords_any = [f"term{i}" for i in range(20)]
        client = StubClient(xml=ARXIV_ATOM)
        self._collect(client)
        self.assertEqual(len(client.calls), 3)  # 20 terms, 8 per request

    def test_failure_is_reported_not_swallowed(self):
        errors: list[str] = []
        papers = self._collect(StubClient(fail=True), errors=errors)
        self.assertEqual(papers, [])
        self.assertTrue(errors, "a dead source must surface in the run's errors")
        self.assertIn("arxiv", errors[0])

    def test_disabled_source_is_skipped(self):
        self.cfg.sources["arxiv"]["enabled"] = False
        client = StubClient(xml=ARXIV_ATOM)
        self.assertEqual(self._collect(client), [])
        self.assertEqual(client.calls, [])


class YouTubeTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["youtube"]["enabled"] = True
        self.cfg.sources["youtube"]["channels"] = [
            {"name": "Research Seminar", "channel_id": "UC0000000000000000000000"}
        ]

    def tearDown(self):
        self.sandbox.close()

    def _collect(self, client, errors=None):
        return youtube.collect(
            self.cfg, self.cfg.topics, date(2000, 1, 1), client=client, errors=errors
        )

    def test_parses_a_channel_feed(self):
        videos = self._collect(StubClient(xml=YOUTUBE_FEED))
        self.assertEqual(len(videos), 1)
        video = videos[0]
        self.assertEqual(video.id, "youtube:abc123XYZ")
        self.assertEqual(video.title, "Causal inference in observational studies")
        self.assertEqual(video.channel, "Research Seminar")
        self.assertEqual(video.description, "A talk on instrumental variables.")
        self.assertEqual(video.published, "2024-03-01")
        self.assertEqual(video.url, "https://www.youtube.com/watch?v=abc123XYZ")

    def test_videos_older_than_the_window_are_dropped(self):
        videos = youtube.collect(
            self.cfg, self.cfg.topics, date(2030, 1, 1), client=StubClient(xml=YOUTUBE_FEED)
        )
        self.assertEqual(videos, [])

    def test_no_channels_means_no_requests(self):
        self.cfg.sources["youtube"]["channels"] = []
        client = StubClient(xml=YOUTUBE_FEED)
        self.assertEqual(self._collect(client), [])
        self.assertEqual(client.calls, [])

    def test_failure_is_reported(self):
        errors: list[str] = []
        self._collect(StubClient(fail=True), errors=errors)
        self.assertTrue(errors)

    def test_missing_transcript_library_is_not_an_error(self):
        # The optional dependency is absent in CI; an empty transcript is the
        # documented outcome, not an exception.
        self.assertEqual(youtube.fetch_transcript("abc123XYZ"), [])

    def test_transcript_text_joins_segments(self):
        text = youtube.transcript_text(
            [{"start_s": 0, "text": "hello"}, {"start_s": 2, "text": "world"}]
        )
        self.assertEqual(text, "hello world")


class ConferenceTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.cfg.sources["conferences"] = {
            "enabled": True,
            "semantic_scholar": {"enabled": True, "api_url": "https://s2.test"},
            "openreview": {"enabled": False},
            "dblp": {"enabled": False},
            "venues": [{"name": "ICLR", "openreview_prefix": "ICLR.cc", "dblp_key": "ICLR"}],
        }

    def tearDown(self):
        self.sandbox.close()

    def test_semantic_scholar_mapping(self):
        papers = conferences.collect(
            self.cfg,
            self.cfg.topics,
            date(2025, 1, 1),
            client=StubClient(payload=SEMANTIC_SCHOLAR),
        )
        self.assertEqual(len(papers), 1)
        paper = papers[0]
        self.assertEqual(paper.id, "arxiv:2501.00002")  # arXiv id beats the DOI
        self.assertEqual(paper.venue, "ICLR")
        self.assertEqual(paper.year, 2025)
        self.assertEqual(paper.authors, ["Grace Hopper"])
        self.assertEqual(paper.pdf_url, "https://example.org/paper.pdf")

    def test_semantic_scholar_query_uses_or_syntax(self):
        client = StubClient(payload=SEMANTIC_SCHOLAR)
        conferences.collect(self.cfg, self.cfg.topics, date(2025, 1, 1), client=client)
        params = client.calls[0][1]
        self.assertIn("|", params["query"])
        self.assertEqual(params["venue"], "ICLR")
        self.assertEqual(params["year"], "2025-")

    def test_an_api_key_reaches_the_request(self):
        """End to end: the env var is read and arrives as a header."""
        client = StubClient(payload=SEMANTIC_SCHOLAR)
        with mock.patch.dict(os.environ, {"SEMANTIC_SCHOLAR_API_KEY": "secret"}):
            conferences.collect(
                self.cfg, self.cfg.topics, date(2025, 1, 1), client=client
            )
        self.assertEqual(client.headers[0].get("x-api-key"), "secret")

    def test_no_api_key_still_queries(self):
        """The header dict is empty here, which is what used to raise."""
        client = StubClient(payload=SEMANTIC_SCHOLAR)
        with mock.patch.dict(os.environ, {}, clear=True):
            papers = conferences.collect(
                self.cfg, self.cfg.topics, date(2025, 1, 1), client=client
            )
        self.assertEqual(len(papers), 1)
        self.assertNotIn("x-api-key", client.headers[0])

    def test_openreview_mapping(self):
        self.cfg.sources["conferences"]["semantic_scholar"]["enabled"] = False
        self.cfg.sources["conferences"]["openreview"] = {
            "enabled": True,
            "api_url": "https://or.test",
        }
        papers = conferences.collect(
            self.cfg, self.cfg.topics, date(2025, 1, 1), client=StubClient(payload=OPENREVIEW)
        )
        self.assertTrue(papers)
        paper = papers[0]
        self.assertEqual(paper.title, "Instrumental Variable Estimation")
        self.assertEqual(paper.authors, ["Barbara Liskov"])
        self.assertEqual(paper.url, "https://openreview.net/forum?id=note123")
        self.assertEqual(paper.pdf_url, "https://openreview.net/pdf/note123.pdf")

    def test_dblp_mapping(self):
        self.cfg.sources["conferences"]["semantic_scholar"]["enabled"] = False
        self.cfg.sources["conferences"]["dblp"] = {
            "enabled": True,
            "api_url": "https://dblp.test",
        }
        papers = conferences.collect(
            self.cfg, self.cfg.topics, date(2025, 1, 1), client=StubClient(payload=DBLP)
        )
        self.assertTrue(papers)
        paper = papers[0]
        self.assertEqual(paper.title, "A Causal Inference Paper")  # trailing period dropped
        self.assertEqual(paper.id, "doi:10.1000/dblp")
        self.assertEqual(paper.authors, ["Donald Knuth"])

    def test_failure_is_reported(self):
        errors: list[str] = []
        conferences.collect(
            self.cfg,
            self.cfg.topics,
            date(2025, 1, 1),
            client=StubClient(fail=True),
            errors=errors,
        )
        self.assertTrue(errors)

    def test_disabled_source_is_skipped(self):
        self.cfg.sources["conferences"]["enabled"] = False
        client = StubClient(payload=SEMANTIC_SCHOLAR)
        self.assertEqual(
            conferences.collect(self.cfg, self.cfg.topics, date(2025, 1, 1), client=client),
            [],
        )
        self.assertEqual(client.calls, [])


if __name__ == "__main__":
    unittest.main()
