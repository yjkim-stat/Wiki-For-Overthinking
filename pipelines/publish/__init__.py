"""Renderers.

Everything here is a pure function of ``data/``: delete ``archive/``, ``wiki/``
and ``outputs/`` and a single ``render.py`` run rebuilds them. Nothing in this
package fetches anything, calls a model, or writes to ``data/``.

That last clause is the one worth stating, because it used to be false: the
wiki renderer also derived the concept records it drew, so rendering could
delete a record from the source of truth. Deriving entities now lives in
``enrich.concepts`` and this package is handed the result. The boundary is
checked by ``tests/test_layering.py`` rather than trusted, so a later change
cannot quietly cross it again.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

_PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


class TemplateError(Exception):
    """A template is missing, or a placeholder had no value."""


def load_template(templates_dir: Path, *parts: str) -> str:
    path = templates_dir.joinpath(*parts)
    if not path.exists():
        raise TemplateError(f"missing template: {path}")
    return path.read_text(encoding="utf-8")


def render_template(template: str, values: dict[str, str]) -> str:
    """Substitute ``{{NAME}}`` placeholders.

    Unknown placeholders raise rather than silently rendering as empty text,
    so a renamed template field fails loudly instead of producing a page with a
    hole in it.
    """
    missing: list[str] = []

    def replace(match: re.Match) -> str:
        key = match.group(1)
        if key not in values:
            missing.append(key)
            return ""
        return values[key]

    output = _PLACEHOLDER.sub(replace, template)
    if missing:
        raise TemplateError(
            "template placeholders with no value: " + ", ".join(sorted(set(missing)))
        )
    return output


def rel_link(from_file: Path, to_file: Path) -> str:
    """Relative link from one generated file to another, POSIX-style."""
    return os.path.relpath(to_file, from_file.parent).replace(os.sep, "/")
