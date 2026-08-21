"""Minimal HTML reading, for the collectors that have no API to talk to.

Standard library only, and deliberately shallow. Nothing here builds a document
tree: these are the three things a collector actually needs from a page it was
not given an API for — the text inside a fragment, the ``<meta>`` tags, and the
block that announces itself as an abstract.

The parsing is regex-based, which is the right trade at this depth. A real
parser would be a dependency and would not make a scraper any less sensitive to
a site redesign; what protects against that is the caller checking that it got
something, and saying so loudly when it did not.
"""

from __future__ import annotations

import html as _html
import re

_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_TAG_RE = re.compile(r"<[^>]+>")
_SCRIPT_RE = re.compile(r"<(script|style)\b.*?</\1>", re.IGNORECASE | re.DOTALL)
_META_RE = re.compile(r"<meta\b(?P<attrs>[^>]*)>", re.IGNORECASE)
_ATTR_RE = re.compile(
    r"(?P<key>[a-zA-Z_:][-\w:.]*)\s*=\s*(\"(?P<dq>[^\"]*)\"|'(?P<sq>[^']*)')"
)
# A block whose class or id says it is the abstract. `blockquote` is here for
# arXiv, which has used it since long before the others existed.
_ABSTRACT_RE = re.compile(
    r"<(?P<tag>blockquote|div|section|p)\b[^>]*\b(?:id|class)=[\"'][^\"']*abstract"
    r"[^\"']*[\"'][^>]*>(?P<body>.*?)</(?P=tag)>",
    re.IGNORECASE | re.DOTALL,
)
# Pages label their fields inline: "Title:", "Authors:", "Abstract:".
_DESCRIPTOR_RE = re.compile(
    r"^\s*(?:title|authors?|abstract|subjects?|comments?)\s*:\s*", re.IGNORECASE
)


def strip_comments(page: str) -> str:
    """Remove HTML comments before matching on structure.

    A comment may contain anything, including markup identical to the structure
    being searched for — a note reading "this block carries no <dt>" is enough
    to hand a pattern a false entry, and a page's commented-out template is
    worse. Every structural parse in this repository starts here.
    """
    return _COMMENT_RE.sub(" ", page or "")


def text(fragment: str) -> str:
    """The readable text of an HTML fragment, whitespace collapsed."""
    without_code = _SCRIPT_RE.sub(" ", strip_comments(fragment))
    return " ".join(_html.unescape(_TAG_RE.sub(" ", without_code)).split())


def field_text(fragment: str) -> str:
    """``text()`` with a leading "Title:"-style descriptor removed."""
    return _DESCRIPTOR_RE.sub("", text(fragment)).strip()


def attrs(blob: str) -> dict[str, str]:
    """Attributes of a single tag, keyed by lowercase name."""
    out: dict[str, str] = {}
    for match in _ATTR_RE.finditer(blob or ""):
        value = match.group("dq")
        if value is None:
            value = match.group("sq") or ""
        out[match.group("key").lower()] = _html.unescape(value)
    return out


def meta(page: str) -> dict[str, list[str]]:
    """Every ``<meta>`` tag, as ``name`` (or ``property``) to its contents.

    A list per name because the Highwire convention repeats ``citation_author``
    once per author, and the order it appears in is the order they are credited.
    """
    found: dict[str, list[str]] = {}
    for match in _META_RE.finditer(page or ""):
        tag = attrs(match.group("attrs"))
        name = (tag.get("name") or tag.get("property") or "").lower()
        content = (tag.get("content") or "").strip()
        if name and content:
            found.setdefault(name, []).append(content)
    return found


def abstract_block(page: str) -> str:
    """The text of the first block that calls itself an abstract, if any."""
    match = _ABSTRACT_RE.search(page or "")
    return field_text(match.group("body")) if match else ""
