"""Deciding whether a phrase occurs in a piece of text.

One rule, in one place, because two of them would be worse than either. Topic
scoring asks "does this paper mention *causal inference*"; a search over the
archive asks the same question of the same corpus, and if the two answered
differently the disagreement would be invisible — a paper found by one and not
the other, with nothing to say which was right.

Deliberately transparent, which is the property `enrich/score.py` was written
for and this inherits: a rule somebody can read and correct beats a matcher
nobody can argue with. No stemming, no dependency, and irregular plurals stay
the author's problem, which is the right place for them.
"""

from __future__ import annotations

import re

_CACHE: dict[str, re.Pattern] = {}


def _plural_tail(word: str) -> str:
    """Match ``word`` or its regular English plural.

    Two rules, applied to one word. Not stemming: the design goal is that
    somebody can read a rule and correct it, and a lemmatizer is neither
    readable nor dependency-free.
    """
    escaped = re.escape(word)
    lowered = word.lower()
    if lowered.endswith("y") and not lowered.endswith(("ay", "ey", "iy", "oy", "uy")):
        return rf"(?:{escaped}|{re.escape(word[:-1])}ies)"  # policy -> policies
    if lowered.endswith(("s", "x", "z", "ch", "sh")):
        return rf"{escaped}(?:es)?"  # bias -> biases
    return rf"{escaped}s?"


def matcher(term: str) -> re.Pattern:
    """Case-insensitive matcher for ``term``.

    Word boundaries keep "ATE" from matching inside "Water"; multi-word terms
    tolerate any run of whitespace or hyphens between words so that "causal
    inference", "causal-inference" and a line-wrapped abstract all match.

    Only the final word is inflected, so "latent action model" matches "latent
    action models" but not "latent actions model" — the plural of a phrase is
    the plural of its head, and inflecting the modifiers would match phrases
    that mean something else.
    """
    cached = _CACHE.get(term)
    if cached is None:
        words = [p for p in re.split(r"[\s\-_]+", term.strip()) if p]
        if not words:
            words = [term.strip()]
        parts = [re.escape(p) for p in words[:-1]] + [_plural_tail(words[-1])]
        body = r"[\s\-_]+".join(parts)
        cached = re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)
        _CACHE[term] = cached
    return cached


def contains(term: str, text: str) -> bool:
    """Whether ``term`` occurs in ``text`` under the rule above."""
    return bool(text) and matcher(term).search(text) is not None
