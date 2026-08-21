"""The read-only window onto the archive.

Two properties carry this feature, and neither is about search quality.

**It writes nothing.** The port is reachable by every process on the host,
including ones nobody meant to run, so the guarantee that reading cannot change
the archive is what makes it safe to open at all. Asserted the way
`tests/test_layering.py` asserts its boundary: `data/` is snapshotted by content,
every endpoint is exercised, and the snapshot must be unchanged.

**It composes nothing.** Every answer is a record the archive already wrote. The
pipeline calls no model, so a server that produced prose would be inventing it,
and a plausible invented answer is worse to a colleague than an honest "nothing
here" — they cannot tell it from a real one.
"""

from __future__ import annotations

import hashlib
import json
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from pipelines import serve
from pipelines.common.schema import Concept, Paper, PaperSummary
from pipelines.common.store import RecordStore
from pipelines.enrich import findings

from .sandbox import Sandbox

SLUG = "test-topic"


def _snapshot(directory: Path) -> dict[str, str]:
    return {
        path.relative_to(directory).as_posix(): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


class ServeTests(unittest.TestCase):
    """Driven over a real socket, because the properties are about the port."""

    @classmethod
    def setUpClass(cls):
        cls.sandbox = Sandbox()
        cls.cfg = cls.sandbox.config()
        store = RecordStore(cls.cfg.layout)

        store.save_paper(
            Paper(
                id="arxiv:2401.00001",
                title="Instrumental Variables for Causal Inference",
                source="arxiv",
                abstract="We estimate effects with an instrumental variable.",
                url="https://arxiv.org/abs/2401.00001",
                topics=[SLUG],
            )
        )
        store.save_paper_summary(
            PaperSummary(
                paper_id="arxiv:2401.00001",
                one_liner="It estimates a treatment effect without randomisation.",
                problem="Confounding.",
                method="By reweighting.",
                results="Beats the baseline by 12 points.",
                relevance={SLUG: "Relevant."},
            )
        )
        store.save_paper(
            Paper(
                id="arxiv:2401.00002",
                title="An Unread Paper About Diffusion",
                source="arxiv",
                abstract="Something about diffusion policies.",
                topics=[SLUG],
            )
        )
        store.save_concept(
            Concept(
                slug="instrumental-variable",
                name="Instrumental Variable",
                kind="concept",
                definition="A variable that shifts treatment but not the outcome.",
                aliases=["IV"],
            )
        )
        findings.record(
            cls.cfg,
            {
                "kind": "decision",
                "statement": "The group prefers instrumental variables to matching here.",
                "rationale": "Matching cannot address unobserved confounding.",
                "topics": [SLUG],
            },
            store,
        )

        cls.server = serve.build(cls.cfg, port=0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)
        cls.sandbox.close()

    def _get(self, path: str) -> tuple[int, dict]:
        url = f"http://127.0.0.1:{self.port}{path}"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read())

    # -- it answers ----------------------------------------------------------
    def test_health_says_what_the_archive_holds(self):
        status, body = self._get("/health")
        self.assertEqual(status, 200)
        self.assertEqual(body["archive"]["papers"], 2)
        self.assertEqual(body["archive"]["findings"], 1)

    def test_a_question_returns_what_the_archive_wrote(self):
        status, body = self._get("/ask?q=instrumental+variable")
        self.assertEqual(status, 200)
        bodies = [h["body"] for h in body["hits"]]
        self.assertIn(
            "A variable that shifts treatment but not the outcome.", bodies
        )

    def test_the_settled_position_comes_before_the_definition(self):
        """The archive's own ordering of authority, kept in the answer.

        A search that returned papers before the sentence the group had already
        agreed on would be answering a different question.
        """
        _, body = self._get("/ask?q=instrumental+variable")
        kinds = [h["kind"] for h in body["hits"]]
        self.assertEqual(kinds[0], "finding")
        self.assertLess(kinds.index("concept"), kinds.index("summary"))

    def test_an_unread_paper_is_offered_last_and_marked(self):
        _, body = self._get("/ask?q=diffusion")
        self.assertEqual([h["kind"] for h in body["hits"]], ["paper"])
        self.assertEqual(body["hits"][0]["body"], "", "nothing has read it yet")

    def test_nothing_found_says_so_rather_than_guessing(self):
        status, body = self._get("/ask?q=xenotransplantation")
        self.assertEqual(status, 404)
        self.assertEqual(body["hits"], [])
        self.assertIn("nothing", body["message"])

    def test_the_terms_it_searched_for_come_back(self):
        """A search that found nothing is only useful if you can see why."""
        _, body = self._get("/ask?q=the+causal+effect")
        self.assertNotIn("the", body["terms"], "stopwords would match everything")
        self.assertIn("causal", body["terms"])

    def test_a_quoted_phrase_is_one_term(self):
        _, body = self._get('/ask?q=%22instrumental+variable%22')
        self.assertEqual(body["terms"], ["instrumental variable"])

    def test_an_empty_question_is_a_bad_request(self):
        status, _ = self._get("/ask?q=")
        self.assertEqual(status, 400)

    def test_an_unknown_endpoint_is_a_404(self):
        status, body = self._get("/nope")
        self.assertEqual(status, 404)
        self.assertIn("endpoints", body)

    # -- it is bounded -------------------------------------------------------
    def test_the_result_count_is_capped_and_says_so(self):
        """Asserted on the limit that was applied, not on the hits returned.

        A fixture never has more records than the cap, so counting hits passes
        whether or not the cap exists — which is how the first version of this
        test missed it entirely.
        """
        _, body = self._get("/ask?q=instrumental+variable&limit=99999")
        self.assertEqual(body["limit"], serve.MAX_LIMIT)
        self.assertLessEqual(len(body["hits"]), serve.MAX_LIMIT)

    def test_a_limit_below_the_cap_is_honoured(self):
        _, body = self._get("/ask?q=instrumental+variable&limit=1")
        self.assertEqual(body["limit"], 1)
        self.assertEqual(len(body["hits"]), 1)

    def test_a_nonsense_limit_does_not_crash_it(self):
        status, _ = self._get("/ask?q=causal&limit=banana")
        self.assertEqual(status, 200)

    def test_an_enormous_query_is_truncated_not_served(self):
        status, _ = self._get("/ask?q=" + "a" * 5000)
        self.assertIn(status, (200, 404))

    # -- it cannot write -----------------------------------------------------
    def test_post_is_refused_and_says_where_writing_happens(self):
        request = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/ask", data=b"{}", method="POST"
        )
        try:
            urllib.request.urlopen(request, timeout=5)
            self.fail("POST should be refused")
        except urllib.error.HTTPError as exc:
            self.assertEqual(exc.code, 405)
            self.assertIn("read-only", json.loads(exc.read())["error"])

    def test_serving_every_endpoint_changes_no_record(self):
        """The property that makes it safe to open the port at all."""
        before = _snapshot(self.cfg.layout.data)
        for path in (
            "/health",
            "/",
            "/ask?q=instrumental+variable",
            "/ask?q=xenotransplantation",
            "/ask?q=",
            "/nope",
            "/ask?q=../../etc/passwd",
        ):
            self._get(path)
        self.assertEqual(_snapshot(self.cfg.layout.data), before)

    def test_a_path_in_the_query_is_just_a_query(self):
        """Nothing opens a file named by a caller; ids go through the store."""
        status, body = self._get("/ask?q=%2Fetc%2Fpasswd")
        self.assertIn(status, (200, 404))
        self.assertNotIn("root:", json.dumps(body))


class UnansweredQuestionTests(unittest.TestCase):
    """What the archive does not know is the most useful thing this port makes.

    It is the only signal anywhere of what people came looking for and did not
    find, and it would be lost the moment the caller closed the connection. It
    goes into the same drop folder a colleague would use by hand, so it enters
    the archive only if a person approves it — inventing a second way in would
    be a second thing to secure.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.addCleanup(self.sandbox.close)
        self.cfg = self.sandbox.config()
        self.cfg.layout.ensure()
        self.server = serve.build(self.cfg, port=0)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.thread.join, 5)
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)

    def _ask(self, query: str) -> tuple[int, dict]:
        url = f"http://127.0.0.1:{self.port}/ask?q={urllib.parse.quote(query)}"
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read())

    def _waiting(self) -> list[Path]:
        return sorted(self.cfg.layout.requests_pending.glob("question-*.md"))

    def test_a_question_nobody_could_answer_is_left_for_review(self):
        status, body = self._ask("xenotransplantation tolerance")
        self.assertEqual(status, 404)
        self.assertTrue(body["recorded"])
        self.assertEqual(len(self._waiting()), 1)

    def test_it_lands_as_a_reviewable_request(self):
        self._ask("xenotransplantation tolerance")
        text = self._waiting()[0].read_text(encoding="utf-8")
        self.assertIn("kind: question", text)
        self.assertIn("xenotransplantation tolerance", text)

        from pipelines import requests as req

        pending = req.load_all(self.cfg, "pending")
        self.assertEqual(len(pending), 1)
        self.assertTrue(pending[0].ok, pending[0].problems)
        self.assertEqual(pending[0].kind, "question")

    def test_asking_the_same_thing_again_is_one_file(self):
        for _ in range(5):
            self._ask("xenotransplantation tolerance")
        self.assertEqual(len(self._waiting()), 1)

    def test_a_question_the_archive_answers_is_not_recorded(self):
        """Only what it could not answer is worth a person's attention."""
        RecordStore(self.cfg.layout).save_concept(
            Concept(slug="a-thing", name="A Thing", kind="concept",
                    definition="It is a thing.")
        )
        status, body = self._ask("a thing")
        self.assertEqual(status, 200)
        self.assertNotIn("recorded", body)
        self.assertEqual(self._waiting(), [])

    def test_recording_stops_at_the_cap(self):
        """An unauthenticated port that can write without a ceiling fills a disk."""
        original = serve.MAX_QUESTIONS
        serve.MAX_QUESTIONS = 3
        self.addCleanup(setattr, serve, "MAX_QUESTIONS", original)

        for index in range(6):
            _, body = self._ask(f"a question about nothing number {index}")
        self.assertEqual(len(self._waiting()), 3)
        self.assertFalse(body["recorded"], "and it says it did not record")

    def test_it_still_touches_no_record(self):
        """The write is in the staging folder. `data/` is untouched, as before."""
        before = _snapshot(self.cfg.layout.data)
        self._ask("xenotransplantation tolerance")
        self.assertEqual(_snapshot(self.cfg.layout.data), before)


class BindingTests(unittest.TestCase):
    def test_it_binds_to_loopback_and_nothing_else(self):
        """Not configurable, so "other users on this machine" stays the audience."""
        self.assertEqual(serve.HOST, "127.0.0.1")
        with Sandbox() as sandbox:
            server = serve.build(sandbox.config(), port=0)
            try:
                self.assertEqual(server.server_address[0], "127.0.0.1")
            finally:
                server.server_close()

    def test_no_flag_can_move_it_off_loopback(self):
        import inspect

        source = inspect.getsource(serve)
        self.assertNotIn("0.0.0.0", source)
        self.assertNotIn("--host", source)


if __name__ == "__main__":
    unittest.main()
