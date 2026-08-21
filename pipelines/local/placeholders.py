"""Reject an entity entry that describes a set of things instead of naming one.

`publish/wiki.py` keys wiki entities by their string. So when a reader who
cannot establish which benchmark a paper used writes "three reasoning
benchmarks (unnamed in abstract)" rather than leaving `datasets` empty, and a
second unrelated paper phrases its placeholder the same way, the two merge into
one entity, count each other as independent evidence, and cross the promotion
threshold as a concept that does not exist. The threshold is there to require
corroboration; a generic phrase manufactures it.

That is not hypothetical: "five reasoning benchmarks (unnamed in abstract)"
reached two sources here — from FoE and SeLaR, different benchmark sets,
neither named — and was queued for a definition.

An empty field is a true statement about what the reader knows. A placeholder
is a false entity.

See `docs/commit-local/0020-a-placeholder-is-not-a-name.md`.
"""

from __future__ import annotations

import re
from typing import Any

# The fields `publish/wiki.py` harvests into wiki entities. An entry in one of
# these becomes a note once enough sources mention it, so what goes in has to be
# a name and not a description of one.
ENTITY_FIELDS = {
    "paper": ("concepts", "methods", "datasets", "models"),
    "video": ("concepts", "methods", "datasets", "models"),
    "concept": (),
}

_PLACEHOLDER = re.compile(
    r"""
      unnamed
    | not \s+ (?: named | specified | given | stated | reported )
    | unspecified
    | \b n/?a \b
    | ^ \s* (?: unknown | none | tbd ) \s* $
    """,
    re.IGNORECASE | re.VERBOSE,
)

# The second signal, for a reader who omits the disclaimer and writes only
# "several math benchmarks". Both halves are required: a bare leading quantifier
# *and* a word for a collection of things. Demanding both is what keeps real
# names — "ten-fold cross-validation", "two-phase reasoning structure",
# "Mixture-of-Experts" — out of the net; note the quantifier must be a whole
# word followed by a space, because a hyphenated one is an adjective, not a
# count.
_QUANTIFIED = re.compile(
    r"""
    ^ \s*
    (?: two | three | four | five | six | seven | eight | nine | ten
      | multiple | several | various | diverse | numerous | many
      | approximately | roughly | about | over )
    \s
    """,
    re.IGNORECASE | re.VERBOSE,
)

_COLLECTION_NOUN = re.compile(
    r"""\b (?: benchmarks | datasets | models | checkpoints | tasks | samples
             | corpora | corpuses | suites | environments | simulators
             | backbones | baselines | domains | sets | families | variants )
    \b""",
    re.IGNORECASE | re.VERBOSE,
)


def looks_like_placeholder(value: str) -> bool:
    """True if this names no specific entity, only a set of them or an absence.

    Public because `scripts/strip_placeholder_entities.py` cleans stored
    summaries with the same rule; the two must not drift apart.
    """
    if _PLACEHOLDER.search(value):
        return True
    return bool(_QUANTIFIED.search(value) and _COLLECTION_NOUN.search(value))


def check(kind: str, result: Any) -> list[str]:
    """Validation errors for every placeholder in a submitted result.

    Shaped to return a list so `enrich/queue.validate_result` needs one line.
    Prose fields are deliberately not checked: "evaluated on three benchmarks
    (unnamed in the abstract)" is a true and useful sentence in `results`, and
    only becomes a problem when it is offered as a name.
    """
    if not isinstance(result, dict):
        return []
    errors: list[str] = []
    for name in ENTITY_FIELDS.get(kind, ()):
        value = result.get(name)
        if not isinstance(value, list):
            continue
        for entry in value:
            if isinstance(entry, str) and looks_like_placeholder(entry):
                errors.append(
                    f"field `{name}` entry {entry!r} describes a set of things "
                    "rather than naming one; leave the field empty instead"
                )
    return errors
