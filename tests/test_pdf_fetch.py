"""Tests for fetching the document a reader is about to summarize.

The property under test throughout is that failure is *ordinary*. A paper with
no reachable PDF must still get its task, with its abstract — roughly one paper
in twelve has no obtainable PDF and that is a normal outcome, not an error.
"""

from __future__ import annotations

import unittest

from pipelines.collect import pdf_fetch
from pipelines.common.http import HTTPError
from pipelines.common.llm import get_summarizer, paper_instructions
from pipelines.common.schema import Paper
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

PDF_BYTES = b"%PDF-1.7\nnot really a pdf, but it starts like one\n"


class StubClient:
    """Serves bodies by URL; anything unmapped raises, as a 404 would."""

    def __init__(self, bodies: dict[str, bytes]) -> None:
        self.bodies = bodies
        self.calls: list[str] = []

    def get(self, url, params=None, headers=None):
        self.calls.append(url)
        try:
            return self.bodies[url]
        except KeyError:
            raise HTTPError(f"GET {url} -> HTTP 404") from None


class FetchTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()

    def tearDown(self):
        self.sandbox.close()

    def _paper(self, **extra) -> Paper:
        fields = {
            "id": "arxiv:2401.00001",
            "title": "A Causal Estimator",
            "source": "arxiv",
            "abstract": "An abstract.",
            "pdf_url": "https://arxiv.org/pdf/2401.00001",
        }
        fields.update(extra)
        return Paper(**fields)

    def test_a_fetched_pdf_lands_on_disk_and_on_the_record(self):
        paper = self._paper()
        client = StubClient({paper.pdf_url: PDF_BYTES})
        counts = pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(counts["fetched"], 1)
        self.assertTrue(paper.local_path.endswith(".pdf"))
        self.assertTrue((self.cfg.layout.root / paper.local_path).exists())

    def test_a_paper_with_no_pdf_url_is_skipped_not_failed(self):
        paper = self._paper(pdf_url="")
        client = StubClient({})
        counts = pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(counts["skipped"], 1)
        self.assertEqual(paper.local_path, "")
        self.assertEqual(client.calls, [])

    def test_an_unreachable_pdf_leaves_the_paper_intact(self):
        paper = self._paper()
        errors: list[str] = []
        counts = pdf_fetch.fetch_for(self.cfg, [paper], StubClient({}), errors)
        self.assertEqual(counts["failed"], 1)
        self.assertEqual(paper.local_path, "")
        self.assertTrue(errors)

    def test_a_login_page_is_not_stored_as_a_paper(self):
        """A paywall serves HTML with a 200. It is not the document."""
        paper = self._paper()
        client = StubClient({paper.pdf_url: b"<html><body>Sign in</body></html>"})
        counts = pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(counts["failed"], 1)
        self.assertEqual(paper.local_path, "")

    def test_a_hand_filed_pdf_is_never_refetched(self):
        """Its file is the original; there is nothing better to download."""
        paper = self._paper(source="local", local_path="data/pdfs/local-abc.pdf")
        client = StubClient({paper.pdf_url: PDF_BYTES})
        pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(client.calls, [])

    def test_an_already_downloaded_pdf_is_not_fetched_twice(self):
        first = self._paper()
        client = StubClient({first.pdf_url: PDF_BYTES})
        pdf_fetch.fetch_for(self.cfg, [first], client)
        second = self._paper()
        pdf_fetch.fetch_for(self.cfg, [second], client)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(second.local_path, first.local_path)

    def _three(self) -> list[Paper]:
        return [
            Paper(id=f"arxiv:{i}", title=f"P{i}", source="arxiv",
                  pdf_url=f"https://x.test/{i}")
            for i in range(3)
        ]

    def test_the_cap_bounds_a_run(self):
        self.cfg.settings["collect"]["pdfs"] = {"max_per_run": 1}
        papers = self._three()
        client = StubClient({p.pdf_url: PDF_BYTES for p in papers})
        counts = pdf_fetch.fetch_for(self.cfg, papers, client)
        self.assertEqual(counts["fetched"], 1)
        self.assertEqual(len(client.calls), 1)

    def test_the_cap_bounds_a_run_called_one_paper_at_a_time(self):
        """The shape `run_daily` actually uses.

        Collection fetches each paper as it files that paper's task, so the cap
        was checked against a counter that began again on every call and
        therefore bounded nothing. The test above hands over the whole list at
        once and never touches the production path.
        """
        self.cfg.settings["collect"]["pdfs"] = {"max_per_run": 1}
        papers = self._three()
        client = StubClient({p.pdf_url: PDF_BYTES for p in papers})

        budget = pdf_fetch.Budget.from_settings(self.cfg)
        for paper in papers:
            pdf_fetch.fetch_for(self.cfg, [paper], client, budget=budget)

        self.assertEqual(len(client.calls), 1, "the cap is per run, not per call")
        self.assertEqual([bool(p.local_path) for p in papers], [True, False, False])

    def test_without_a_budget_a_call_gets_the_whole_cap(self):
        """The old signature still means what it always did.

        One call's worth is the only reading under which it was ever correct,
        and a caller that wants a run has to say so by passing a budget.
        """
        self.cfg.settings["collect"]["pdfs"] = {"max_per_run": 1}
        papers = self._three()
        client = StubClient({p.pdf_url: PDF_BYTES for p in papers})
        for paper in papers:
            pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(len(client.calls), 3)

    def test_every_caller_of_fetch_for_passes_a_budget(self):
        """Static, because no fixture reaches the path that was broken.

        The behavioural tests above call `fetch_for` directly, so they pass
        whether or not collection shares a budget across its calls — which is
        exactly how the cap came to bound nothing in a real run while a test
        called `test_the_cap_bounds_a_run` was green.

        The same reasoning as `tests/test_layering.py`'s static half: a defect
        that lives in how a module is *called* is invisible to a test of the
        module.
        """
        import ast

        from pipelines.common.paths import REPO_ROOT

        offenders: list[str] = []
        for path in sorted((REPO_ROOT / "pipelines").rglob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                name = func.attr if isinstance(func, ast.Attribute) else getattr(func, "id", "")
                if name != "fetch_for":
                    continue
                if not any(kw.arg == "budget" for kw in node.keywords):
                    offenders.append(f"{path.relative_to(REPO_ROOT)}:{node.lineno}")

        self.assertEqual(
            offenders,
            [],
            "these call fetch_for without a budget, so the per-run cap resets: "
            + ", ".join(offenders),
        )

    def test_disabled_means_no_requests(self):
        self.cfg.settings["collect"]["pdfs"] = {"enabled": False}
        paper = self._paper()
        client = StubClient({paper.pdf_url: PDF_BYTES})
        pdf_fetch.fetch_for(self.cfg, [paper], client)
        self.assertEqual(client.calls, [])

    def test_pdf_fetching_gets_its_own_slower_floor(self):
        client = pdf_fetch.client_for(self.cfg)
        self.assertGreaterEqual(client.min_interval_s, 5.0)


class TaskWiringTests(unittest.TestCase):
    """A fetched PDF and a hand-filed one are the same thing to the reader."""

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.queue = Queue(self.cfg.layout)
        self.summarizer = get_summarizer(self.cfg.settings, enqueue=self.queue.enqueue)
        self.topics = [{"slug": "test-topic", "name": "Test", "description": "d"}]

    def tearDown(self):
        self.sandbox.close()

    def _task(self, paper: Paper) -> dict:
        self.summarizer.summarize_paper(paper, self.topics, "en")
        return self.queue.load(self.queue.pending_ids()[0])

    def test_a_remote_paper_with_a_pdf_carries_the_path(self):
        task = self._task(
            Paper(id="arxiv:1", title="t", source="arxiv",
                  local_path="data/pdfs/arxiv-1.pdf")
        )
        self.assertEqual(task["attachments"]["pdf_path"], "data/pdfs/arxiv-1.pdf")
        self.assertIn("attachments.pdf_path", task["instructions"])

    def test_a_remote_paper_without_one_is_unchanged(self):
        task = self._task(Paper(id="arxiv:2", title="t", source="arxiv"))
        self.assertEqual(task["attachments"], {})
        self.assertNotIn("attachments.pdf_path", task["instructions"])

    def test_the_prompt_points_at_the_experiments_not_the_abstract(self):
        text = paper_instructions(self.topics, "en", has_pdf=True)
        self.assertIn("experiments section", text)
        self.assertNotIn("experiments section", paper_instructions(self.topics, "en"))

    def test_a_hand_filed_pdf_still_asks_for_the_bibliography(self):
        """The two paths converge on the attachment, not on the contract."""
        task = self._task(
            Paper(id="local:abc", title="guessed", source="local",
                  local_path="data/pdfs/local-abc.pdf")
        )
        self.assertIn("bibliography", task["output_schema"])
        self.assertIn("filename is not evidence", task["instructions"])


if __name__ == "__main__":
    unittest.main()
