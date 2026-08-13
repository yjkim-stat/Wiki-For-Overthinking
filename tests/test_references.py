"""Things checked outside the archive, and the line they must never cross.

The archive can be asked what it holds. It cannot be asked what a published
implementation does, and sessions go and find that out — so what they learned
needs somewhere to live other than the prose of a finding, where the next person
can neither verify it nor find it again.

The whole risk of adding such a record is one sentence, and it is the reason for
the second half of this file:

    **An external reference must never contribute to entity promotion.**

`Concept.evidence` counts papers and talks the archive has read, and that count
promotes an entity to a note of its own. If a blog post could raise it, nothing
afterwards could say what the wiki had grown from — and unlike a wrong link or a
bad definition, that damage cannot be undone by deleting the post, because the
notes it promoted are already there and look exactly like the rest.
"""

from __future__ import annotations

import unittest

from pipelines import render
from pipelines.common.schema import (
    Paper,
    PaperSummary,
    Reference,
    normalize_url,
    reference_id,
)
from pipelines.common.store import RecordStore
from pipelines.enrich import findings, references
from pipelines.enrich.queue import Queue

from .sandbox import Sandbox

SLUG = "test-topic"

GOOD = {
    "url": "https://github.com/example/thing",
    "title": "example/thing",
    "publisher": "github.com/example",
    "kind": "code",
    "retrieved_at": "2026-08-13",
    "quoted": "The scheduler defaults to 30 denoising steps.",
}


class ValidationTests(unittest.TestCase):
    def test_a_complete_reference_is_accepted(self):
        self.assertEqual(references.validate(GOOD), [])

    def test_a_url_is_required(self):
        errors = references.validate({**GOOD, "url": ""})
        self.assertTrue(any("url" in e for e in errors), errors)

    def test_a_non_http_url_is_refused(self):
        errors = references.validate({**GOOD, "url": "ftp://example.com/x"})
        self.assertTrue(any("http" in e for e in errors), errors)

    def test_retrieved_at_is_required(self):
        """Without it a claim about a page cannot be checked against anything.

        Asserted against the *required-field* message rather than the field
        name. Both branches below mention `retrieved_at`, so a test that only
        looked for the name passed even with the requirement removed — the
        malformed-value branch caught the empty string and reported it as a
        different problem.
        """
        errors = references.validate({**GOOD, "retrieved_at": ""})
        self.assertTrue(
            any("missing or empty required field: retrieved_at" in e for e in errors),
            errors,
        )

    def test_a_bare_year_is_not_a_retrieval_date(self):
        errors = references.validate({**GOOD, "retrieved_at": "2026"})
        self.assertTrue(any("ISO date" in e for e in errors), errors)

    def test_a_quotation_is_required(self):
        """When the page moves it is the only evidence that survives."""
        errors = references.validate({**GOOD, "quoted": ""})
        self.assertTrue(
            any("missing or empty required field: quoted" in e for e in errors), errors
        )

    def test_an_unknown_kind_is_refused(self):
        errors = references.validate({**GOOD, "kind": "tweet"})
        self.assertTrue(any("kind" in e for e in errors), errors)


class IdentityTests(unittest.TestCase):
    """The same page cited twice is one record; two pages are never one."""

    def test_spellings_of_one_page_agree(self):
        for variant in (
            "https://github.com/example/thing",
            "https://github.com/example/thing/",
            "https://GitHub.com/example/thing",
            "https://github.com:443/example/thing",
            "https://github.com/example/thing#readme",
        ):
            self.assertEqual(
                reference_id(variant), reference_id(GOOD["url"]), variant
            )

    def test_a_query_string_selects_a_different_page(self):
        """Left alone deliberately: on a great many sites it is the page."""
        self.assertNotEqual(
            reference_id("https://example.com/view?id=1"),
            reference_id("https://example.com/view?id=2"),
        )

    def test_path_case_is_significant(self):
        self.assertNotEqual(
            reference_id("https://example.com/A"),
            reference_id("https://example.com/a"),
        )

    def test_normalizing_keeps_the_scheme(self):
        self.assertTrue(normalize_url("HTTPS://X.test/a").startswith("https://"))


class RecordingTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

    def tearDown(self):
        self.sandbox.close()

    def test_a_reference_is_stored_and_reloads(self):
        recorded = references.record(self.cfg, GOOD, self.store)
        again = RecordStore(self.cfg.layout).load_reference(recorded.id)
        self.assertEqual(again.url, GOOD["url"])
        self.assertEqual(again.quoted, GOOD["quoted"])
        self.assertEqual(again.kind, "code")

    def test_the_same_page_twice_is_one_record(self):
        first = references.record(self.cfg, GOOD, self.store)
        second = references.record(
            self.cfg, {**GOOD, "url": GOOD["url"] + "/", "quoted": "Something else."},
            self.store,
        )
        self.assertEqual(first.id, second.id)
        self.assertEqual(len(list(self.store.iter_references())), 1)

    def test_a_second_visit_updates_the_quotation_and_keeps_first_seen(self):
        first = references.record(self.cfg, GOOD, self.store)
        second = references.record(
            self.cfg, {**GOOD, "quoted": "It now says something else."}, self.store
        )
        self.assertEqual(second.quoted, "It now says something else.")
        self.assertEqual(second.first_seen, first.first_seen)

    def test_the_publisher_falls_back_to_the_host(self):
        recorded = references.record(
            self.cfg, {**GOOD, "publisher": ""}, self.store
        )
        self.assertEqual(recorded.publisher, "github.com")

    def test_an_invalid_reference_is_refused_and_stores_nothing(self):
        with self.assertRaises(ValueError):
            references.record(self.cfg, {**GOOD, "quoted": ""}, self.store)
        self.assertEqual(list(self.store.iter_references()), [])


class FindingLinkTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.reference = references.record(self.cfg, GOOD, self.store)

    def tearDown(self):
        self.sandbox.close()

    def _finding(self, **extra) -> dict:
        base = {
            "kind": "fact",
            "statement": "The published implementation defaults to 30 steps.",
            "rationale": "Read off the scheduler config.",
            "topics": [SLUG],
        }
        base.update(extra)
        return base

    def test_a_finding_may_cite_a_recorded_reference(self):
        recorded = findings.record(
            self.cfg, self._finding(references=[self.reference.id]), self.store
        )
        self.assertEqual(recorded.references, [self.reference.id])

    def test_a_finding_citing_an_unrecorded_reference_is_refused(self):
        """The same check `papers` gets, for the same reason."""
        errors = findings.validate(
            self.cfg, self._finding(references=["web:deadbeefdeadbeef"]), self.store
        )
        self.assertTrue(any("references" in e for e in errors), errors)

    def test_a_finding_without_references_is_unchanged(self):
        recorded = findings.record(self.cfg, self._finding(), self.store)
        self.assertEqual(recorded.references, [])

    def test_an_older_finding_without_the_field_still_loads(self):
        from pipelines.common.schema import Finding

        raw = Finding(id="finding:x", kind="fact", statement="A statement.").to_dict()
        raw.pop("references")
        self.assertEqual(Finding.from_dict(raw).references, [])


class PromotionIsSealedOffTests(unittest.TestCase):
    """The assertion this whole record type is on probation for.

    Two papers mention an entity, which is the promotion threshold. A reference
    and a finding that cites it are then added. Neither the count nor the set of
    notes may move.
    """

    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)

        for index in (1, 2):
            paper_id = f"arxiv:2401.0000{index}"
            self.store.save_paper(
                Paper(id=paper_id, title=f"Paper {index}", source="arxiv",
                      published="2024-01-15", year=2024, topics=[SLUG])
            )
            self.store.save_paper_summary(
                PaperSummary(
                    paper_id=paper_id,
                    one_liner="It does a thing.",
                    relevance={SLUG: "Relevant."},
                    concepts=["Instrumental Variable"],
                )
            )

    def tearDown(self):
        self.sandbox.close()

    def _state(self) -> tuple[int, set[str]]:
        concept = self.store.load_concept("instrumental-variable")
        notes = {p.name for p in self.cfg.layout.wiki.rglob("*.md")}
        return concept.mention_count, notes

    def test_a_reference_does_not_raise_mention_count_or_add_a_note(self):
        render.run(self.cfg)
        before = self._state()

        references.record(self.cfg, GOOD, self.store)
        findings.record(
            self.cfg,
            {
                "kind": "fact",
                "statement": "The implementation contradicts the paper's table 3.",
                "concepts": ["Instrumental Variable", "A Thing Only The Web Mentions"],
                "references": [reference_id(GOOD["url"])],
                "topics": [SLUG],
            },
            self.store,
        )
        render.run(self.cfg)

        self.assertEqual(self._state(), before)

    def test_an_entity_named_only_by_a_finding_is_never_promoted(self):
        """A finding may name an entity the archive has not read about.

        It gets no note from that, however many references back it: a note is
        what the *literature* converging on a term produces.
        """
        render.run(self.cfg)
        references.record(self.cfg, GOOD, self.store)
        findings.record(
            self.cfg,
            {
                "kind": "fact",
                "statement": "A thing only the web mentions is worth knowing about.",
                "concepts": ["A Thing Only The Web Mentions"],
                "references": [reference_id(GOOD["url"])],
                "topics": [SLUG],
            },
            self.store,
        )
        render.run(self.cfg)

        self.assertIsNone(self.store.load_concept("a-thing-only-the-web-mentions"))

    def test_nothing_under_enrich_concepts_reads_a_reference(self):
        """Static, so a future path no fixture reaches cannot cross the line.

        The behavioural tests above prove today's code does not count a
        reference. This one is what keeps that true when somebody adds a
        plausible-looking line to the harvest.
        """
        from pipelines.common.paths import REPO_ROOT

        source = (REPO_ROOT / "pipelines" / "enrich" / "concepts.py").read_text(
            encoding="utf-8"
        )
        for forbidden in ("reference", "Reference"):
            self.assertNotIn(forbidden, source)

    def test_a_reference_is_not_a_paper(self):
        references.record(self.cfg, GOOD, self.store)
        ids = {p.id for p in self.store.iter_papers()}
        self.assertEqual(ids, {"arxiv:2401.00001", "arxiv:2401.00002"})
        self.assertNotIn(reference_id(GOOD["url"]), ids)


if __name__ == "__main__":
    unittest.main()
