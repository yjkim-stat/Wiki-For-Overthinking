"""Concept slugs that are probably the same entity.

    python -m pipelines.duplicates [--json] [--limit N]

The wiki grows itself. A term named in one reading as "world model" and in the
next as "world models" becomes two entities, each with its own evidence, its own
promotion threshold and eventually its own note — and neither is wrong about
anything, which is why nothing catches it. The archive ends up saying half of
what it knows about a term, twice.

**This report suggests. It merges nothing and it writes nothing at all.** No
record is saved, no alias is added, no file is created; running it over an
archive leaves every byte under ``data/`` where it was, and
``tests/test_duplicates.py`` asserts exactly that, by content and by
modification time, the way ``tests/test_layering.py`` asserts its own boundary.

That restraint is the design, not a missing feature. Merging two entities is
irreversible in the direction that matters: the evidence of the loser is folded
into the winner, and afterwards nothing can say the wiki ever held two terms or
which reading contributed what. It is also a judgement — "attention" and
"attentions" are the same thing, "GAN" and "GAN inversion" are not, and no
string rule knows the difference. So this produces the input to a decision and
stops there. The decision is a person's, and the way to act on it is the alias
field of a concept task, which goes through the validator like every other
answer.

**Tuned for recall.** A pair suggested wrongly costs somebody a glance; a pair
never suggested costs an entity that stays split for ever, and stays split
invisibly. Every rule here is therefore looser than it would be if something
downstream acted on it automatically — which is the other reason nothing does.

## The four rules

Each is a rule somebody can read and correct, which is what
``pipelines/common/text.py`` is for and what ``enrich/score.py`` established: a
transparent rule beats an opaque similarity nobody can argue with.

``variant``   the two slugs are the same once case and every separator is
              removed — ``worldmodel`` against ``world-model``.
``plural``    one is the regular English plural of the other, under the same
              matcher topic scoring uses, so the wiki and the scorer cannot
              disagree about what a plural is.
``suffix``    one is the other plus exactly one trailing word — ``world`` against
              ``world model``.
``near``      an edit distance of 1 or 2, for a typo or a transposition.

A pair matching several rules is reported once, under the most specific: the
order above is the precedence.
"""

from __future__ import annotations

import argparse
import json
import logging
from itertools import combinations
from pathlib import Path

from .common import config as config_mod
from .common import log
from .common import paths as P
from .common.config import Config
from .common.schema import Concept
from .common.store import RecordStore
from .common.text import matcher

_LOG = log.get(__name__)

#: Precedence, most specific first. A pair is reported once, under the first
#: rule that claims it.
REASONS = ("variant", "plural", "suffix", "near")

#: How far apart two slugs may be and still be suggested as a typo.
MAX_EDITS = 2

#: Below this length an edit distance of two is most of the alphabet: on a
#: four-character slug it relates almost everything to almost everything, and a
#: report that suggests every pair suggests nothing. Short slugs are still
#: compared by the other three rules, which do not degrade with length.
MIN_NEAR_LENGTH = 5


def _terms(slug: str) -> list[str]:
    """A slug read back as the words it was made from."""
    return [word for word in slug.split("-") if word]


def _squashed(slug: str) -> str:
    """The slug with case and every separator removed."""
    return "".join(c for c in slug.lower() if c.isalnum())


def _is_plural_of(a: str, b: str) -> bool:
    """Whether one slug is the regular plural of the other.

    Delegated to ``common.text.matcher`` rather than re-implemented, so the wiki
    and topic scoring cannot come to different conclusions about whether
    "policy" and "policies" are one word. ``fullmatch`` rather than a search:
    the matcher is built to find a term inside a document, and here the whole
    slug has to be the term, or "model" would be the plural of "world model".
    """
    left, right = " ".join(_terms(a)), " ".join(_terms(b))
    if not left or not right:
        return False
    return bool(
        matcher(left).fullmatch(right) or matcher(right).fullmatch(left)
    )


def _is_suffix_of(a: str, b: str) -> bool:
    """Whether one slug is the other plus exactly one trailing word.

    One word, not any number: two extra words is usually a different, narrower
    thing rather than the same thing named longer. The extra word is not checked
    against a list of permitted heads — "model", "method", "framework" would be
    the obvious list and it would miss whatever the group's own field calls the
    same idea, which is exactly the failure this report exists to catch.
    """
    short, long = sorted((_terms(a), _terms(b)), key=len)
    return len(long) == len(short) + 1 and long[: len(short)] == short


def _edit_distance(a: str, b: str, limit: int) -> int | None:
    """Levenshtein distance between two slugs, or ``None`` if it exceeds ``limit``.

    Bounded rather than exact: this is asked of every pair of concepts in the
    archive, and the answer is only ever compared against ``limit``. A row whose
    best cell already exceeds the bound cannot recover, so the pass stops there.
    """
    if abs(len(a) - len(b)) > limit:
        return None
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(
                min(
                    previous[j] + 1,
                    current[j - 1] + 1,
                    previous[j - 1] + (ca != cb),
                )
            )
        if min(current) > limit:
            return None
        previous = current
    return previous[-1] if previous[-1] <= limit else None


def reason_for(a: str, b: str) -> str:
    """Which rule, if any, says these two slugs are one entity. ``""`` if none."""
    if a == b:
        return ""
    if _squashed(a) == _squashed(b):
        return "variant"
    if _is_plural_of(a, b):
        return "plural"
    if _is_suffix_of(a, b):
        return "suffix"
    if min(len(a), len(b)) >= MIN_NEAR_LENGTH:
        distance = _edit_distance(a, b, MAX_EDITS)
        if distance is not None and distance >= 1:
            return "near"
    return ""


def _side(concept: Concept) -> dict:
    """What a person needs about one half of a pair in order to decide.

    The source count and whether a definition exists, because those are what the
    decision costs. Merging into the side that has been defined keeps written
    work; merging into the side with the evidence keeps the wiki's arithmetic.
    When those point in opposite directions the pair is worth a longer look,
    and both numbers are here so that is visible at a glance.
    """
    return {
        "slug": concept.slug,
        "name": concept.name,
        "sources": concept.mention_count,
        "defined": bool(concept.definition.strip()),
    }


def candidates(store: RecordStore) -> list[dict]:
    """Every pair of concept slugs a rule relates, strongest evidence first.

    Within a pair the side with more evidence comes first — it is the likelier
    survivor of a merge, and a report that put the arbitrary one first would
    make the list harder to skim than the wiki itself. Ties, both within a pair
    and between pairs, fall back to the slug, so two runs over an unchanged
    archive produce the same list in the same order.
    """
    concepts = list(store.iter_concepts())
    pairs: list[dict] = []
    for left, right in combinations(concepts, 2):
        reason = reason_for(left.slug, right.slug)
        if not reason:
            continue
        first, second = sorted(
            (left, right), key=lambda c: (-c.mention_count, c.slug)
        )
        pairs.append(
            {"reason": reason, "a": _side(first), "b": _side(second)}
        )
    pairs.sort(
        key=lambda p: (
            -(p["a"]["sources"] + p["b"]["sources"]),
            p["a"]["slug"],
            p["b"]["slug"],
        )
    )
    return pairs


def run(cfg: Config, *, limit: int = 0) -> dict:
    """Look for duplicate concepts. Reads the archive and returns a report.

    Writes nothing — not a record, not a log file entry in ``data/``, not a
    cached result. The return value is the whole output.
    """
    store = RecordStore(cfg.layout)
    pairs = candidates(store)
    report = {
        "concepts": sum(1 for _ in store.iter_concepts()),
        "candidates": len(pairs),
        "by_reason": {r: sum(1 for p in pairs if p["reason"] == r) for r in REASONS},
        "pairs": pairs[:limit] if limit else pairs,
    }
    return report


def format_report(report: dict) -> str:
    """The report as something a person reads, rather than JSON."""
    lines = [
        f"{report['concepts']} concept(s); "
        f"{report['candidates']} duplicate candidate(s)"
    ]
    if not report["candidates"]:
        lines.append("")
        lines.append("Nothing here suggests two names for one entity.")
        return "\n".join(lines)

    counted = ", ".join(
        f"{reason} {count}"
        for reason, count in report["by_reason"].items()
        if count
    )
    lines.append(f"  by rule: {counted}")
    lines.append("")
    for pair in report["pairs"]:
        lines.append(f"{pair['reason']:<8} {_describe(pair['a'])}")
        lines.append(f"{'':<8} {_describe(pair['b'])}")
        lines.append("")
    lines.append(
        "Nothing was merged and nothing was written. To act on a pair, decide "
        "which name survives and record the other as an alias when its "
        "definition task is answered."
    )
    return "\n".join(lines)


def _describe(side: dict) -> str:
    defined = "defined" if side["defined"] else "no definition"
    return f"{side['slug']:<40} {side['sources']:>3} source(s)  {defined}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m pipelines.duplicates",
        description="List concept slugs that are probably the same entity. "
        "Read-only: it suggests, merges nothing and writes nothing.",
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="how many pairs to show (0: all)"
    )
    parser.add_argument("--json", action="store_true", help="emit the raw report")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=f"deployment root: the tree the archive lives in (default: ${P.ROOT_ENV}, "
        "else this checkout)",
    )
    args = parser.parse_args(argv)

    cfg = config_mod.load(args.root)
    # Logging is configured to the console only. `log.setup` would create
    # `data/logs/`, and this command's whole claim is that it touches nothing.
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )

    report = run(cfg, limit=args.limit)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(format_report(report))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
