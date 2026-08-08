import unittest

from pipelines.common import md


class InlineTests(unittest.TestCase):
    def test_escapes_html(self):
        self.assertEqual(md.inline("a < b & c"), "a &lt; b &amp; c")

    def test_code_span_is_not_reinterpreted(self):
        # Emphasis markers inside a code span are literal text.
        self.assertEqual(md.inline("`a * b * c`"), "<code>a * b * c</code>")

    def test_bold_and_italic(self):
        self.assertEqual(md.inline("**hi** and *there*"),
                         "<strong>hi</strong> and <em>there</em>")

    def test_underscores_inside_words_are_left_alone(self):
        self.assertEqual(md.inline("latent_action_model"), "latent_action_model")

    def test_link(self):
        self.assertEqual(
            md.inline("[x](https://e.org)"), '<a href="https://e.org">x</a>'
        )

    def test_link_text_is_escaped(self):
        self.assertIn("&lt;script&gt;", md.inline("[<script>](https://e.org)"))

    def test_bare_url_is_linked(self):
        self.assertEqual(
            md.inline("see https://e.org now"),
            'see <a href="https://e.org">https://e.org</a> now',
        )

    def test_math_span(self):
        self.assertIn('<span class="math">a + b</span>', md.inline("$a + b$"))

    def test_strip_markdown(self):
        self.assertEqual(md.strip_markdown("**bold** [x](y) `z`"), "bold x z")


class BlockTests(unittest.TestCase):
    def test_headings(self):
        self.assertIn("<h2>Title</h2>", md.to_html("## Title"))

    def test_paragraph(self):
        self.assertEqual(md.to_html("one\ntwo"), "<p>one two</p>")

    def test_unordered_list(self):
        html = md.to_html("- a\n- b")
        self.assertIn("<ul>", html)
        self.assertEqual(html.count("<li>"), 2)
        self.assertIn("</ul>", html)

    def test_ordered_list(self):
        html = md.to_html("1. a\n2. b")
        self.assertIn("<ol>", html)
        self.assertEqual(html.count("<li>"), 2)

    def test_list_then_paragraph_closes_the_list(self):
        html = md.to_html("- a\n\nafter")
        self.assertLess(html.index("</ul>"), html.index("<p>after</p>"))

    def test_fenced_code_is_not_parsed(self):
        html = md.to_html("```python\n# not a heading\n- not a list\n```")
        self.assertIn("<pre><code", html)
        self.assertIn("# not a heading", html)
        self.assertNotIn("<h1>", html)
        self.assertNotIn("<li>", html)

    def test_table_with_header(self):
        html = md.to_html("| a | b |\n| --- | --- |\n| 1 | 2 |")
        self.assertIn("<thead>", html)
        self.assertIn("<th>a</th>", html)
        self.assertIn("<td>1</td>", html)

    def test_blockquote(self):
        html = md.to_html("> quoted")
        self.assertIn("<blockquote>", html)
        self.assertIn("</blockquote>", html)

    def test_horizontal_rule(self):
        self.assertIn("<hr>", md.to_html("text\n\n---\n\nmore"))

    def test_every_tag_is_closed(self):
        html = md.to_html("## H\n\n- a\n- b\n\n> q\n\n| a |\n| --- |\n| 1 |\n")
        for tag in ("ul", "blockquote", "table"):
            self.assertEqual(html.count(f"<{tag}>"), html.count(f"</{tag}>"))

    def test_empty_input(self):
        self.assertEqual(md.to_html(""), "")


if __name__ == "__main__":
    unittest.main()
