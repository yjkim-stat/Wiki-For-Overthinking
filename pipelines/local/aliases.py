"""One entity, many names: the authored map that decides which name wins.

The harvest keys a concept by ``slugify(name)``, so two summaries writing
*AIME24* and *AIME 2024* build two records. Each accumulates its own share of
the evidence, each crosses the promotion threshold separately, and each is
handed to a reader as a definition task that sees a fraction of the sources.
Nothing reports this: both records look complete, and the wiki grows two notes
about one benchmark.

It is not rare here. `AIME 2024` is spread over three slugs holding 9, 28 and 2
sources; `MATH-500` over two holding 27 and 12.

**Why the `aliases` field cannot do this job.** A ``Concept`` already carries
one, and it is already populated -- `aime-2024` lists *AIME24* as an alias while
`aime24` exists as a separate record with three times the evidence. But that
field is filled from whatever a reader wrote in a summary, and readers use it
for two different relations. Some entries are the same entity under another
spelling (*IF-Eval* / *IFEval*). Others are a neighbour, a parent or a subset:
*GPQA* is listed as an alias of `gpqa-diamond`, which is a subset of it;
*MATH* as an alias of `math500`, which is 500 problems drawn from it;
*causal tracing* as an alias of `activation-patching`, which this archive's own
note argues measures a different quantity. Merging on that field would silently
collapse distinctions the archive is here to keep.

So the map is **authored**, in `config/concept-aliases.yaml`, one line per
decision. `scripts/merge_concept_aliases.py` prints the candidate list; a person
rules on it.

**What this module does and does not do.** It redirects a slug, and that is all.
It does not touch records already on disk -- a record written under a name that
has since become an alias keeps its definition and would be resurrected by the
harvest's carry-over rule. Retiring those is a one-off with its own audit trail,
because it destroys authored text and must not happen as a side effect of a
render. See `scripts/merge_concept_aliases.py`. See docs/commit/0063.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from ..common.log import get
from ..common.paths import slugify

_LOG = get(__name__)

#: Basename under the deployment's `config/`. Absent is the normal case for a
#: fresh deployment and means "no name has needed a ruling yet".
FILENAME = "concept-aliases.yaml"

_MAP: dict[str, str] = {}
#: canonical slug -> the name written in the file. Redirecting the slug alone is
#: not enough: the harvest titles a record with whichever spelling it reached
#: first, so `aime24` seen before `AIME 2024` would fold correctly and still
#: produce a note called *AIME24*. The map has to decide the name as well.
_NAMES: dict[str, str] = {}
_SOURCE: Path | None = None


class AliasError(Exception):
    """The alias map says something that cannot be honoured."""


def _parse(data: dict[str, Any], path: Path) -> tuple[dict[str, str], dict[str, str]]:
    """``{canonical: [alias, ...]}`` -> redirects, and the canonical names.

    Both sides are slugified, so an entry may be written as a name (*AIME 2024*)
    or as a slug (`aime-2024`) -- whichever the person ruling had in front of
    them. The key's text is kept as written, because it is what the wiki note
    ends up titled.
    """
    block = data.get("merge") or {}
    if not isinstance(block, dict):
        raise AliasError(f"{path}: `merge` must be a mapping of canonical -> [alias]")

    mapping: dict[str, str] = {}
    names_by_slug: dict[str, str] = {}
    owner: dict[str, str] = {}
    for canonical, names in block.items():
        target = slugify(str(canonical))
        names_by_slug[target] = str(canonical)
        if isinstance(names, str):
            names = [names]
        if not isinstance(names, list):
            raise AliasError(f"{path}: {canonical!r} must map to a list of names")
        for name in names:
            alias = slugify(str(name))
            if alias == target:
                # Harmless on its own, but it always means the entry was
                # written against the wrong spelling of one of the two.
                raise AliasError(
                    f"{path}: {name!r} and {canonical!r} slugify to the same "
                    f"thing ({alias}); one of them is not the name you meant"
                )
            if alias in owner and owner[alias] != target:
                raise AliasError(
                    f"{path}: {name!r} is claimed by both {owner[alias]!r} and "
                    f"{target!r}; an alias belongs to one entity"
                )
            owner[alias] = target
            mapping[alias] = target

    # A chain would make the result depend on iteration order, and the fix is
    # always to write the entry against the end of the chain instead.
    for alias, target in mapping.items():
        if target in mapping:
            raise AliasError(
                f"{path}: {target!r} is both a canonical name and an alias of "
                f"{mapping[target]!r}; point {alias!r} at the end of the chain"
            )
    return mapping, names_by_slug


def load(path: Path) -> dict[str, str]:
    """Read one alias file. A missing file is an empty map, not an error."""
    return _load(path)[0]


def _load(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    if not path.exists():
        return {}, {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:  # pragma: no cover - depends on user edits
        raise AliasError(f"{path}: {exc}") from exc
    if data is None:
        return {}, {}
    if not isinstance(data, dict):
        raise AliasError(f"{path}: expected a mapping at the top level")
    return _parse(data, path)


def install(layout) -> dict[str, str]:
    """Point this module at a deployment's config. Called from `config.load`.

    Installed at config-load time rather than resolved lazily inside
    `slug_for`, because that function is called from four modules and has no
    config to hand -- and because `--root` is an argument rather than an
    environment variable, so a lazy resolver would read the wrong tree exactly
    when the two trees differ.
    """
    global _MAP, _NAMES, _SOURCE
    path = layout.root / "config" / FILENAME
    _MAP, _NAMES = _load(path)
    _SOURCE = path if _MAP else None
    if _MAP:
        _LOG.debug("concept aliases: %d name(s) redirected from %s", len(_MAP), path)
    return _MAP


def canonical(slug: str) -> str:
    """The slug this one belongs to, or itself."""
    return _MAP.get(slug, slug)


def canonical_name(slug: str) -> str | None:
    """The name a ruled entity should be titled with, or None if none is ruled.

    Only ever consulted for a slug that the map names as canonical, so an
    entity nobody has ruled on keeps taking its name from its evidence.
    """
    return _NAMES.get(slug)


def mapping() -> dict[str, str]:
    """The installed map, for scripts and tests."""
    return dict(_MAP)


def source() -> Path | None:
    """Where the installed map came from, or None if there is none."""
    return _SOURCE


def reset() -> None:
    """Forget the installed map. For tests, which build several layouts."""
    global _MAP, _NAMES, _SOURCE
    _MAP = {}
    _NAMES = {}
    _SOURCE = None
