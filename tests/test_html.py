"""Tests for the shared HTML helpers.

Two collectors read pages nobody gave them an API for. What they need from a
page is the same three things, so it lives here rather than being written twice
and drifting.
"""

from __future__ import annotations

import unittest

from pipelines.common import html as html_util


class TextTests(unittest.TestCase):
    def test_tags_are_dropped_and_whitespace_collapsed(self):
        self.assertEqual(html_util.text("<h5>A  <b>Bold</b>\n Title</h5>"), "A Bold Title")

    def test_entities_are_unescaped(self):
        self.assertEqual(html_util.text("Bayes&#39; rule &amp; more"), "Bayes' rule & more")

    def test_script_bodies_do_not_become_text(self):
        self.assertEqual(html_util.text("<div>Real<script>var x=1;</script></div>"), "Real")

    def test_empty_input_is_empty_output(self):
        self.assertEqual(html_util.text(""), "")

    def test_a_field_descriptor_is_stripped(self):
        fragment = '<span class="descriptor">Title:</span> The Real Title'
        self.assertEqual(html_util.field_text(fragment), "The Real Title")

    def test_a_colon_inside_a_title_survives(self):
        """Only a leading label is a descriptor."""
        fragment = '<span class="descriptor">Title:</span> RoCA: Robust Driving'
        self.assertEqual(html_util.field_text(fragment), "RoCA: Robust Driving")


class MetaTests(unittest.TestCase):
    PAGE = """
    <meta name="citation_author" content="Ada Lovelace">
    <meta name="citation_author" content="Alan Turing">
    <meta property="og:description" content="A description.">
    <meta name="citation_title" content="A &amp; B">
    <meta name="empty" content="">
    """

    def test_repeated_names_keep_every_value_in_order(self):
        self.assertEqual(
            html_util.meta(self.PAGE)["citation_author"], ["Ada Lovelace", "Alan Turing"]
        )

    def test_property_is_read_as_a_name(self):
        self.assertEqual(html_util.meta(self.PAGE)["og:description"], ["A description."])

    def test_content_is_unescaped(self):
        self.assertEqual(html_util.meta(self.PAGE)["citation_title"], ["A & B"])

    def test_an_empty_content_is_not_recorded(self):
        self.assertNotIn("empty", html_util.meta(self.PAGE))


class AbstractBlockTests(unittest.TestCase):
    def test_a_div_that_calls_itself_an_abstract(self):
        page = '<div class="card-abstract"><p>A <b>bare</b> abstract.</p></div>'
        self.assertEqual(html_util.abstract_block(page), "A bare abstract.")

    def test_a_blockquote_as_arxiv_uses(self):
        page = (
            '<blockquote class="abstract mathjax">'
            '<span class="descriptor">Abstract:</span> We estimate effects.'
            "</blockquote>"
        )
        self.assertEqual(html_util.abstract_block(page), "We estimate effects.")

    def test_no_abstract_is_empty_not_invented(self):
        self.assertEqual(html_util.abstract_block("<html><body>x</body></html>"), "")


if __name__ == "__main__":
    unittest.main()
