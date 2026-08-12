#!/usr/bin/env python3
"""One-off migration: move model names out of `datasets` and into `models`.

Summaries written before the `model` wiki kind existed had nowhere to put an
evaluated checkpoint, so readers put them in `datasets`. The result was a wiki
whose `datasets/` directory was half models.

This rewrites stored summaries in place. It is a pipeline operation on
`data/summaries/`, not a hand edit: the classification rule is in this file and
the run is idempotent, so it can be re-read and re-run.

The rule is a name pattern over known model families rather than a heuristic
about capitalisation, because the cost of a false positive (a benchmark filed as
a model) is higher than the cost of a miss (a model left in `datasets`, which is
the status quo). Anything the pattern does not match stays where it is; add a
family here and re-run rather than editing a summary by hand.

    python3 scripts/migrate_model_kind.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Model families seen in this deployment's summaries. Ordered roughly by how
# often they appear; the pattern is matched case-insensitively anywhere in the
# name, so "DeepSeek-R1-Distill-Qwen-7B" matches on the first alternative.
MODEL_PATTERN = re.compile(
    r"""(
        qwen | llama | mistral | mixtral | gemma | deepseek | pythia | phi[\s-]?\d
      | gpt-?2 | gpt-?3 | gpt-?4 | gpt-?5 | gpt-?j | gpt-oss | o\d-mini
      | qwq | claude | gemini | minimax | kimi | glm-\d | olmo | yi-\d
      | seed-think | openpangu | eurus | skywork | light-r1 | oat-zero
      | srpo | s1-\d*b | dapo-qwen | simplerl
    )""",
    re.IGNORECASE | re.VERBOSE,
)


def is_model(name: str) -> bool:
    return bool(MODEL_PATTERN.search(name))


def migrate_file(path: Path, dry_run: bool) -> tuple[int, list[str]]:
    record = json.loads(path.read_text(encoding="utf-8"))
    datasets = list(record.get("datasets") or [])
    models = list(record.get("models") or [])

    moved = [n for n in datasets if is_model(n)]
    if not moved:
        # Still normalise the field so every summary carries the new key.
        if "models" not in record and not dry_run:
            record["models"] = models
            path.write_text(
                json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        return 0, []

    record["datasets"] = [n for n in datasets if not is_model(n)]
    for name in moved:
        if name not in models:
            models.append(name)
    record["models"] = models

    if not dry_run:
        path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return len(moved), moved


# The definitions written while the misfiling was in force each carry a
# sentence explaining it. That explanation is now false, so it is removed here
# rather than left for a reader to trip over.
STALE_NOTE = re.compile(
    r"\s*Note that this entry is filed as a dataset because the archived "
    r"summaries listed evaluated models in the dataset field; it is a model, "
    r"not a corpus\.",
)


def strip_stale_notes(dry_run: bool) -> int:
    """Remove the misfiling explanation from stored concept definitions."""
    changed = 0
    for path in sorted((ROOT / "data" / "concepts").glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        definition = record.get("definition") or ""
        cleaned = STALE_NOTE.sub("", definition).rstrip()
        if cleaned != definition:
            changed += 1
            if not dry_run:
                record["definition"] = cleaned
                path.write_text(
                    json.dumps(record, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run", action="store_true", help="report what would move, change nothing"
    )
    args = parser.parse_args()

    targets = sorted(
        list((ROOT / "data" / "summaries" / "papers").glob("*.json"))
        + list((ROOT / "data" / "summaries" / "videos").glob("*.json"))
    )
    if not targets:
        print("no summaries found; nothing to migrate")
        return 0

    total_moved = 0
    touched = 0
    names: set[str] = set()
    for path in targets:
        count, moved = migrate_file(path, args.dry_run)
        if count:
            touched += 1
            total_moved += count
            names.update(moved)

    stale = strip_stale_notes(args.dry_run)

    verb = "would move" if args.dry_run else "moved"
    print(f"{verb} {total_moved} entries across {touched}/{len(targets)} summaries")
    print(f"{len(names)} distinct model names:")
    for name in sorted(names):
        print(f"  {name}")
    print(f"{'would clear' if args.dry_run else 'cleared'} the misfiling note "
          f"from {stale} definitions")
    if not args.dry_run:
        print("\nrun `python3 -m pipelines.render` to rebuild the wiki")
    return 0


if __name__ == "__main__":
    sys.exit(main())
