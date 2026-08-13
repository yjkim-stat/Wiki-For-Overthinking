#!/usr/bin/env python3
"""One-off: fill `models` on nine summaries whose reader left the field empty.

The `model` wiki kind is a local delta (docs/LOCAL-DELTAS.md) and the field it
feeds is optional with no validator, so a reading that omits `models` entirely
is accepted, applied and archived without a warning anywhere. That is what
happened on 2026-08-13 to the first nine paper readings of a session, and
`reopen` refuses a task once render has consumed it — so the field cannot be
corrected through the queue. `CLAUDE.md` names the remaining options for that
case as fixing the record or re-collecting the item; this is the first.

**Why a table and not a rule.** The obvious approach — extract checkpoint names
from the summary's own prose — was written and discarded, because it produces
names that do not exist. A reading legitimately abbreviates ("Qwen2.5-3B-Instruct
and 7B-Instruct"), and a pattern over that text yields `Qwen2.5-Instruct`, which
is in no paper. Writing that into `data/` would create a phantom entity, and a
phantom entity that later receives a definition is frozen, because a stored
definition stops the harvest re-deriving an entity's kind. An empty field is a
true statement; an invented model name is not.

So the mapping below is **transcribed from each paper's own setup section**, not
inferred. Every name appears in the document. Where a document names a model the
summary does not mention, the document wins; where the transcription was
uncertain the entry is left short, since a miss costs the status quo and a false
positive costs a wrong entity.

Idempotent, and it refuses any summary whose `models` is already populated — a
reader's answer is never second-guessed. Re-running after a fresh reading of the
same paper therefore changes nothing.

    python3 scripts/backfill_summary_models.py            # report, change nothing
    python3 scripts/backfill_summary_models.py --apply

This file has no reason to be run twice and is kept for the same reason
`migrate_model_kind.py` is: so the edit that was made to `data/` is auditable
after the fact.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

#: summary stem -> models named in that paper's experimental setup.
#: Retrievers, reward models and judges are included: the output contract says
#: `models` covers what the work "trains, evaluates or analyses", and names a
#: judge as an example.
MODELS: dict[str, list[str]] = {
    # Cloud-ScPO. "Base Models" paragraph, plus ArmoRM as the IRPO-RM baseline's
    # reward model.
    "arxiv-2608-01014": [
        "Llama-3-8B",
        "Mistral-7B-v0.3",
        "Qwen3-8B",
        "Qwen3-4B-Instruct-2507",
        "ArmoRM-Llama3-8B",
    ],
    # ScaleQ-1.58 / AYOT. Scaling table spans 1.7B to 235B; BitNet is the
    # trained-from-scratch comparison and DeepSeek-R1-671B the rejected teacher.
    "arxiv-2608-01078": [
        "Qwen3-1.7B",
        "Qwen3-4B",
        "Qwen3-30B-A3B",
        "Qwen3-32B",
        "Qwen3-235B-A22B",
        "BitNet b1.58 2B4T",
        "DeepSeek-R1-671B",
    ],
    # PGS audit. Two open vision-language backbones.
    "arxiv-2608-01207": [
        "Qwen2.5-VL-7B-Instruct",
        "LLaVA-OneVision-7B",
    ],
    # BiCAA. Two backbones, the retriever, and the step-level classifier.
    "arxiv-2608-01321": [
        "Qwen2.5-7B-Instruct",
        "Qwen3-8B",
        "E5-base-v2",
        "GPT-5.5",
    ],
    # EviSD. Three backbones and the same retrieval environment.
    "arxiv-2608-01359": [
        "Qwen2.5-7B-Instruct",
        "Qwen2.5-3B-Instruct",
        "Qwen3-1.7B",
        "E5-base-v2",
    ],
    # Latent Thought Credit.
    "arxiv-2608-01593": [
        "Qwen2.5-3B-Instruct",
        "Qwen2.5-7B-Instruct",
    ],
    # Does Accuracy Equal Evidence. Headline backbone plus two checks. The two
    # judge models are named in the paper but not transcribed here.
    "arxiv-2608-01631": [
        "Qwen3-8B",
        "DeepSeek-R1-Distill-Llama-8B",
        "Qwen3-30B-A3B",
    ],
    # Observability ladder. Five target models plus the stronger-reader judge.
    "arxiv-2608-02089": [
        "Qwen3-4B",
        "Qwen3-8B",
        "Qwen3-14B",
        "gpt-oss-20b",
        "gpt-oss-120b",
        "GPT-5-mini",
    ],
    # SPEE. Three base checkpoints.
    "arxiv-2608-02139": [
        "Qwen3-1.7B-Base",
        "Qwen3-4B-Base",
        "Qwen3-8B-Base",
    ],
}


def backfill(path: Path, names: list[str], apply: bool) -> list[str]:
    """Fill an empty `models`. Returns what was written, or nothing."""
    record = json.loads(path.read_text(encoding="utf-8"))
    if record.get("models"):
        return []
    if apply:
        record["models"] = list(names)
        path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return list(names)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help="write; without it, only report"
    )
    args = parser.parse_args()

    papers = ROOT / "data" / "summaries" / "papers"
    touched = skipped = missing = 0
    for stem, names in sorted(MODELS.items()):
        path = papers / f"{stem}.json"
        if not path.exists():
            print(f"{stem}: no such summary", file=sys.stderr)
            missing += 1
            continue
        written = backfill(path, names, args.apply)
        if written:
            touched += 1
            print(f"{stem}: {', '.join(written)}")
        else:
            skipped += 1
            print(f"{stem}: already populated, left alone")

    verb = "filled" if args.apply else "would fill"
    print(f"\n{verb} {touched}, skipped {skipped}, missing {missing}")
    if not args.apply and touched:
        print("re-run with --apply to write")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
