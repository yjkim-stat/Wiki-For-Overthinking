"""A small Markdown -> HTML converter.

Reports and slides must be self-contained single files with no external
requests, which rules out a client-side Markdown renderer. Rather than pull in
a dependency, this covers the subset the generators actually emit: headings,
paragraphs, lists, tables, blockquotes, fenced code, horizontal rules, inline
emphasis, code spans, links, images and math spans.

Math is wrapped in ``<span class="math">`` rather than typeset: a
self-contained page cannot fetch a typesetting library, so the source is shown
in a distinct style instead.
"""

from __future__ import annotations

import html
import re

__all__ = ["to_html", "inline", "escape", "strip_markdown"]

escape = html.escape

_FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_UL_ITEM = re.compile(r"^\s*[-*+]\s+(.*)$")
_OL_ITEM = re.compile(r"^\s*\d+[.)]\s+(.*)$")
_HR = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
_QUOTE = re.compile(r"^\s*>\s?(.*)$")
_TABLE_DIV = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")

_CODE_SPAN = re.compile(r"`([^`]+)`")
_MATH_BLOCK = re.compile(r"\$\$(.+?)\$\$", re.S)
_MATH_INLINE = re.compile(r"(?<![\\$])\$([^$\n]+?)\$")
_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
_BOLD = re.compile(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", re.S)
_ITALIC = re.compile(r"(?<![\w*_])([*_])(?=\S)(.+?)(?<=\S)\1(?![\w*_])", re.S)
_STRIKE = re.compile(r"~~(?=\S)(.+?)(?<=\S)~~", re.S)
_BARE_URL = re.compile(r"(?<![\"'>=])\bhttps?://[^\s<>\")\]]+")

_MD_MARKS = re.compile(r"[*_`~]|\[\[|\]\]")


def strip_markdown(text: str) -> str:
    """Plain-text form, for titles and metadata fields."""
    text = _IMAGE.sub(r"\1", text or "")
    text = _LINK.sub(r"\1", text)
    text = _WIKILINK.sub(lambda m: m.group(2) or m.group(1), text)
    return _MD_MARKS.sub("", text).strip()


def inline(text: str) -> str:
    """Render inline Markdown in ``text`` to HTML."""
    placeholders: list[str] = []

    def stash(markup: str) -> str:
        placeholders.append(markup)
        return f"\x00{len(placeholders) - 1}\x00"

    # Code spans and math are literal: protect them before anything else can
    # interpret their contents as emphasis.
    text = _CODE_SPAN.sub(lambda m: stash(f"<code>{escape(m.group(1))}</code>"), text or "")
    text = _MATH_BLOCK.sub(
        lambda m: stash(f'<span class="math math-block">{escape(m.group(1).strip())}</span>'),
        text,
    )
    text = _MATH_INLINE.sub(
        lambda m: stash(f'<span class="math">{escape(m.group(1).strip())}</span>'), text
    )

    text = _IMAGE.sub(
        lambda m: stash(
            f'<img src="{escape(m.group(2), quote=True)}" alt="{escape(m.group(1), quote=True)}">'
        ),
        text,
    )
    text = _LINK.sub(
        lambda m: stash(
            f'<a href="{escape(m.group(2), quote=True)}">{escape(m.group(1))}</a>'
        ),
        text,
    )
    text = _WIKILINK.sub(
        lambda m: stash(
            f'<a class="wikilink" href="{escape(m.group(1), quote=True)}.md">'
            f"{escape(m.group(2) or m.group(1))}</a>"
        ),
        text,
    )

    text = escape(text)
    text = _BARE_URL.sub(lambda m: f'<a href="{m.group(0)}">{m.group(0)}</a>', text)
    text = _BOLD.sub(r"<strong>\2</strong>", text)
    text = _ITALIC.sub(r"<em>\2</em>", text)
    text = _STRIKE.sub(r"<del>\1</del>", text)

    for index, markup in enumerate(placeholders):
        text = text.replace(f"\x00{index}\x00", markup)
    return text


class _Builder:
    """Accumulates HTML while tracking which block is currently open."""

    def __init__(self) -> None:
        self.out: list[str] = []
        self.stack: list[str] = []
        self.para: list[str] = []

    def close_paragraph(self) -> None:
        if self.para:
            self.out.append(f"<p>{inline(' '.join(self.para))}</p>")
            self.para = []

    def close_until(self, *keep: str) -> None:
        self.close_paragraph()
        while self.stack and self.stack[-1] not in keep:
            self.out.append(f"</{self.stack.pop()}>")

    def open(self, tag: str, attrs: str = "") -> None:
        self.out.append(f"<{tag}{attrs}>")
        self.stack.append(tag)

    def close_all(self) -> None:
        self.close_until()

    def html(self) -> str:
        self.close_all()
        return "\n".join(self.out)


def _render_table(rows: list[str], has_header: bool) -> str:
    def cells(line: str) -> list[str]:
        line = line.strip().strip("|")
        return [c.strip() for c in line.split("|")]

    parts = ["<table>"]
    body_start = 0
    if has_header and rows:
        parts.append("<thead><tr>")
        parts += [f"<th>{inline(c)}</th>" for c in cells(rows[0])]
        parts.append("</tr></thead>")
        body_start = 1
    parts.append("<tbody>")
    for row in rows[body_start:]:
        parts.append("<tr>")
        parts += [f"<td>{inline(c)}</td>" for c in cells(row)]
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "".join(parts)


def to_html(text: str) -> str:
    """Convert a Markdown document to an HTML fragment."""
    builder = _Builder()
    lines = (text or "").replace("\r\n", "\n").split("\n")
    index = 0

    while index < len(lines):
        line = lines[index]

        fence = _FENCE.match(line)
        if fence:
            marker, language = fence.group(1), fence.group(2)
            builder.close_until()
            index += 1
            block: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith(marker[0] * 3):
                block.append(lines[index])
                index += 1
            index += 1  # consume the closing fence
            cls = f' class="language-{escape(language, quote=True)}"' if language else ""
            builder.out.append(
                f"<pre><code{cls}>{escape(chr(10).join(block))}</code></pre>"
            )
            continue

        if not line.strip():
            builder.close_until()
            index += 1
            continue

        if _HR.match(line) and not builder.para:
            builder.close_until()
            builder.out.append("<hr>")
            index += 1
            continue

        heading = _HEADING.match(line)
        if heading:
            builder.close_until()
            level = len(heading.group(1))
            builder.out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        quote = _QUOTE.match(line)
        if quote:
            if "blockquote" not in builder.stack:
                builder.close_until()
                builder.open("blockquote")
            builder.para.append(quote.group(1))
            index += 1
            continue

        if "|" in line and line.strip().startswith("|"):
            block = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                block.append(lines[index])
                index += 1
            has_header = len(block) > 1 and bool(_TABLE_DIV.match(block[1]))
            if has_header:
                block.pop(1)
            builder.close_until()
            builder.out.append(_render_table(block, has_header))
            continue

        item = _UL_ITEM.match(line)
        if item:
            if builder.stack[-1:] != ["ul"]:
                builder.close_until()
                builder.open("ul")
            else:
                builder.close_paragraph()
            builder.out.append(f"<li>{inline(item.group(1))}</li>")
            index += 1
            continue

        item = _OL_ITEM.match(line)
        if item:
            if builder.stack[-1:] != ["ol"]:
                builder.close_until()
                builder.open("ol")
            else:
                builder.close_paragraph()
            builder.out.append(f"<li>{inline(item.group(1))}</li>")
            index += 1
            continue

        if builder.stack[-1:] in (["ul"], ["ol"]):
            builder.close_until()
        builder.para.append(line.strip())
        index += 1

    return builder.html()
