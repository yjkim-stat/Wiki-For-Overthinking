# Migration

**The procedure lives in [`migration/README.md`](../../migration/README.md), not
here.** That is deliberate: the environment that has to follow it is the one
that has just cloned and has nothing else to read, so every instruction it needs
is in the folder the bundle arrives in. This page is the harness — what proves
the move worked — and the one thing that is easy to get wrong.

## The one thing

**Push before you pack.** An archive travels along two channels and only one of
them is automatic:

- **git carries the knowledge** — every record, the wiki, the queue, the dedup
  state. `data/` is committed on purpose.
- **the bundle carries what git refuses** — PDFs, announced abstracts, raw
  responses, logs.

The expensive failure is not a dropped PDF. It is a container discarded while
`main` was still behind the working tree, which is silent at both ends: the
bundle looks complete and the clone looks healthy.

```bash
python3 -m pipelines.migrate status
```

Do not pack while that still prints a `WARNING` under `git`.

## The sequence

```bash
# on the old container
python3 -m pipelines.migrate status
python3 -m pipelines.migrate pack --dest migration
tar -czf migration.tar.gz -C <repo> migration

# on the new one
git clone <remote> && cd <repo> && pip install -r requirements.txt
tar -xzf migration.tar.gz -C .
python3 -m pipelines.migrate verify --src migration
python3 -m pipelines.migrate unpack --src migration
python3 -m pipelines.render
```

## Harness

| Guard | What it proves |
| --- | --- |
| `MANIFEST.json` | Every file under every source root appears in `files` or `skipped`, with a reason. No sampling, no cap — that is what makes "nothing was left behind" checkable rather than claimed |
| sha256 per file | The bytes that arrived are the bytes that left |
| `verify` | Runs at the far end **before** anything is restored. `missing`, `corrupt` and `unlisted` all fail it — a bundle that cannot account for what it carries has not been verified |
| `pack` refusing a used `--dest` | An earlier pack's files underneath would make the bundle ship what a narrowed `--tier` claims to have dropped. It refuses rather than clearing, because a previous `--move` left that payload as the only copy |
| `unpack` checksum gate | A file that fails is named and **not written** — whatever was at that path is left alone, so a re-transfer is safe |
| `check_documents` | The real question, answered from `data/` and the filesystem rather than from the bundle: does every record claiming a document have one. Still answerable after the bundle is deleted |
| `tests/test_migrate.py` | 39 tests. Pack and unpack are each checked against the filesystem rather than against their own report |

### Exit codes

| Command | `0` | `1` |
| --- | --- | --- |
| `status` | always | — |
| `pack` | git half clean and pushed | it was not (bundle still written), or the destination already held a payload (nothing written) |
| `verify` | everything present, intact, and nothing extra | anything missing, corrupt or unlisted |
| `unpack` | every file restored | anything missing from the bundle or failing its checksum |

## Tiers, and what dropping one costs

`--tier` is cumulative. The tier says what it costs to lose the file, not how
big it is.

| Tier | If you drop it |
| --- | --- |
| `irreplaceable` | **Gone permanently.** Hand-filed PDFs have no URL anywhere; the record survives pointing at nothing |
| `refetchable` | Network time. Abstracts are re-paid by the coverage ledger; **a PDF is not re-fetched automatically** once its record exists |
| `disposable` | Nothing downstream reads `data/raw/` or `data/logs/` |

## What nothing checks

- **That the clone is the right branch.** `records` in the manifest is a receipt
  re-counted after unpack, so a mismatch is reported — but it can only tell you
  the counts differ, not which branch you wanted.
- **That a document is the document its record describes.** Checksums prove
  transit, not identity.
- **That the bundle was ever transferred.** `pack` finishing means staged, not
  moved. Nothing on the old container knows whether the new one received it.
