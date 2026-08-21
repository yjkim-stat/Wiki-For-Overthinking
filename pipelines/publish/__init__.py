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
from collections.abc import Sequence
from pathlib import Path

_PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


class TemplateError(Exception):
    """A template is missing, or a placeholder had no value."""


def load_template(where: Path | Sequence[Path], *parts: str) -> str:
    """Read a template from the first directory that holds it.

    ``where`` is one directory or a search order — see ``Layout.template_dirs``,
    which puts a deployment's own templates in front of the ones the code ships.
    A file is resolved individually, so overriding one template does not mean
    inheriting a whole directory frozen at the version it was copied from.
    """
    dirs = [where] if isinstance(where, Path) else list(where)
    for directory in dirs:
        path = directory.joinpath(*parts)
        if path.exists():
            return path.read_text(encoding="utf-8")
    looked = " or ".join(str(d.joinpath(*parts)) for d in dirs)
    raise TemplateError(f"missing template: {looked}")


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


def unchanged_but_for(existing: str, fresh: str, volatile: re.Pattern) -> bool:
    """Whether two renderings differ only in a field that restamps itself.

    `render` regenerates every artifact from `data/` on every pass, and two of
    them carry the time they were generated. Rewriting a file whose only change
    is that stamp puts it in every diff for ever, which is how a real change
    stops being visible — the failure note 0036 fixed for records, in a tracked
    generated file.

    Comparing with the stamp masked out lets the stamp go on meaning something:
    written only when the drawing actually moved, it says when the graph last
    changed rather than when somebody last ran a command.
    """
    return volatile.sub("", existing) == volatile.sub("", fresh)


def rel_link(from_file: Path, to_file: Path) -> str:
    """Relative link from one generated file to another, POSIX-style."""
    return os.path.relpath(to_file, from_file.parent).replace(os.sep, "/")
