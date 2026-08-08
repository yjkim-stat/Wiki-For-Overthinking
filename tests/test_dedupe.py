import unittest

from pipelines.common.schema import Paper, canonical_paper_id, normalize_title
from pipelines.common.store import RecordStore, SeenStore
from pipelines.enrich.dedupe import Deduplicator, merge_papers, paper_keys

from .sandbox import Sandbox


def paper(**kwargs) -> Paper:
    base = dict(id="", title="A World Model", source="arxiv")
    base.update(kwargs)
    if not base["id"]:
        base["id"] = canonical_paper_id(
            arxiv_id=base.get("arxiv_id", ""),
            doi=base.get("doi", ""),
            title=base["title"],
        )
    return Paper(**base)


class CanonicalIdTests(unittest.TestCase):
    def test_arxiv_id_wins_over_doi(self):
        self.assertEqual(
            canonical_paper_id(arxiv_id="2401.12345", doi="10.1/x"), "arxiv:2401.12345"
        )

    def test_version_suffix_is_dropped(self):
        self.assertEqual(canonical_paper_id(arxiv_id="2401.12345v3"), "arxiv:2401.12345")

    def test_title_fallback_is_stable(self):
        self.assertEqual(
            canonical_paper_id(title="A World Model!"),
            canonical_paper_id(title="a  world   model"),
        )

    def test_requires_at_least_one_identifier(self):
        with self.assertRaises(ValueError):
            canonical_paper_id()

    def test_title_normalization(self):
        self.assertEqual(normalize_title("A  World-Model: Part 1"), "a world model part 1")


class MergeTests(unittest.TestCase):
    def test_longer_field_wins(self):
        merged = merge_papers(
            paper(abstract="short"), paper(abstract="a much longer abstract")
        )
        self.assertEqual(merged.abstract, "a much longer abstract")

    def test_existing_value_survives_an_empty_incoming_one(self):
        merged = paper(abstract="kept")
        merged = merge_papers(merged, paper(abstract=""))
        self.assertEqual(merged.abstract, "kept")

    def test_earliest_publication_date_wins(self):
        merged = merge_papers(
            paper(published="2024-06-01"), paper(published="2024-01-15")
        )
        self.assertEqual(merged.published, "2024-01-15")

    def test_sources_accumulate(self):
        merged = merge_papers(paper(source="arxiv"), paper(source="dblp"))
        self.assertIn("arxiv", merged.source)
        self.assertIn("dblp", merged.source)

    def test_categories_are_unioned_without_duplicates(self):
        merged = merge_papers(
            paper(categories=["cs.RO"]), paper(categories=["cs.RO", "cs.LG"])
        )
        self.assertEqual(sorted(merged.categories), ["cs.LG", "cs.RO"])

    def test_richer_author_list_wins(self):
        merged = merge_papers(paper(authors=["A"]), paper(authors=["A", "B"]))
        self.assertEqual(merged.authors, ["A", "B"])


class DeduplicatorTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = Sandbox()
        self.cfg = self.sandbox.config()
        self.store = RecordStore(self.cfg.layout)
        self.seen = SeenStore(self.cfg.layout.seen_db)
        self.deduper = Deduplicator(self.seen, self.store)

    def tearDown(self):
        self.seen.close()
        self.sandbox.close()

    def test_first_sighting_is_new(self):
        _, is_new = self.deduper.resolve_paper(paper(arxiv_id="2401.00001"))
        self.assertTrue(is_new)

    def test_second_sighting_is_not_new(self):
        first, _ = self.deduper.resolve_paper(paper(arxiv_id="2401.00001"))
        self.store.save_paper(first)
        _, is_new = self.deduper.resolve_paper(paper(arxiv_id="2401.00001"))
        self.assertFalse(is_new)

    def test_same_title_from_another_source_collapses_onto_the_arxiv_record(self):
        first, _ = self.deduper.resolve_paper(
            paper(arxiv_id="2401.00001", title="A World Model")
        )
        self.store.save_paper(first)

        second, is_new = self.deduper.resolve_paper(
            paper(title="A World Model", source="dblp", venue="ICLR", doi="10.1/x")
        )
        self.assertFalse(is_new)
        self.assertEqual(second.id, "arxiv:2401.00001")
        self.assertEqual(second.venue, "ICLR")

    def test_paper_keys_cover_every_alias(self):
        keys = paper_keys(paper(arxiv_id="2401.00001", doi="10.1/X"))
        self.assertIn("arxiv:2401.00001", keys)
        self.assertIn("doi:10.1/x", keys)
        self.assertTrue(any(k.startswith("title:") for k in keys))


if __name__ == "__main__":
    unittest.main()
