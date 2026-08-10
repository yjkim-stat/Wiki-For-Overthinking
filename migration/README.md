# Moving an archive to a new environment

Everything you need in order to carry this archive — the papers, the readings,
the wiki, the findings and the documents behind them — into a fresh container
running the same repository. Read it end to end before you start: the step that
loses an archive is the first one, and it is not the one about files.

---

## 1. The archive travels along two channels

They are not the same channel, only one of them is automatic, and confusing
them is how a migration silently loses half of itself.

| | **git carries it** | **this bundle carries it** |
| --- | --- | --- |
| Papers, seminars, readings | ✅ `data/papers/`, `data/videos/`, `data/summaries/` | — |
| Wiki entities and evidence | ✅ `data/concepts/` | — |
| What the group settled | ✅ `data/findings/` | — |
| The work queue | ✅ `data/queue/` | — |
| Dedup state, coverage ledger | ✅ `data/index/` incl. `seen.sqlite` | — |
| The wiki, and your analysis after `<!-- auto:end -->` | ✅ `wiki/` | — |
| Daily digests, archive pages, outputs | ✅ `archive/`, `outputs/` | — |
| Config, topics, code | ✅ | — |
| **Documents (PDFs)** | ❌ gitignored | ✅ `data/pdfs/`, `data/pdfs/read/`, `inbox/*.pdf` |
| **Announced-paper abstracts** | ❌ gitignored | ✅ `data/abstracts/` |
| **Raw collector responses, run logs** | ❌ gitignored | ✅ `data/raw/`, `data/logs/` |

**The knowledge is in git.** `data/` is the source of truth and it is committed
on purpose, precisely so a scheduled run can start from a fresh clone. If your
work is pushed, the new environment inherits the archive by cloning — before
this bundle is unpacked at all.

**This bundle carries only what git refuses to.** Heavy, re-fetchable in
principle, and in the case of documents not ours to redistribute.

> **The expensive failure is not a dropped PDF.** It is a container discarded
> while `main` was still behind the working tree. That one is silent at both
> ends: the bundle looks complete, the clone looks healthy, and the readings
> nobody pushed are simply gone. Step 2 exists for that reason alone.

---

## 2. Before you pack: push everything

```bash
cd <this repository>
git status --short          # must be empty
git fetch origin main
git log --oneline origin/main..HEAD    # must be empty
```

If either is non-empty, commit and push before going further. A change to code,
config, templates or docs also needs a note under `docs/commit/` — see
[CLAUDE.md](../CLAUDE.md).

```bash
git add -A && git commit -m "archive: <date> digest"
git push -u origin main
```

Then confirm what each channel is about to carry:

```bash
python3 -m pipelines.migrate status
```

```
git
  branch     main @ a6465a8f3c8f
  upstream   origin/main
  clean and pushed -- git will carry the knowledge

records carried by git
  papers                   1284
  videos                     37
  concepts                  212
  findings                   19
  queue_pending             143
  papers_with_document     1140
  topics                      5

files carried by the bundle
  irreplaceable          31 file(s)  74.2 MB
  refetchable          1109 file(s)  3.1 GB
  disposable            402 file(s)  86.0 MB

documents: 1140 record(s) claim one, 0 missing on disk
```

`status` exits without writing anything. **Do not pack while it still prints a
`WARNING` under `git`** — everything below assumes the knowledge is safely on
the remote.

---

## 3. Pack

```bash
python3 -m pipelines.migrate pack --dest migration
```

Every file under every source root is inventoried. Nothing is sampled and
nothing is capped; whatever is deliberately left out is listed in the manifest
under `skipped`, with a reason.

You get:

```
migration/
├── README.md          ← this file (tracked in git)
├── MANIFEST.json      ← the inventory: every file, its size, its sha256, its tier
└── payload/
    ├── data/pdfs/…    ← original paths, so restoring is a straight copy back
    ├── data/abstracts/…
    ├── data/raw/…
    ├── data/logs/…
    └── inbox/…
```

Files are **hard-linked** where the filesystem allows, so packing costs no disk
— these containers have a fixed allowance and a second copy of a PDF store is
exactly the thing that fills it. Originals are left in place. Use `--move` only
if you are certain, because a transfer that fails after a move has destroyed
the only copy.

### Packing less than everything

Every file has a tier, and the tier says **what it costs you to lose it** —
not how big it is.

| Tier | What is in it | If you drop it |
| --- | --- | --- |
| `irreplaceable` | Hand-filed PDFs, undrained `inbox/`, and any document no record claims | **Gone permanently.** Somebody chose these and put them in the inbox; no URL was ever recorded. The record describing the document survives and points at nothing, which is worse than an obvious gap. |
| `refetchable` | Fetched PDFs (they have a `pdf_url`) and `data/abstracts/` | Costs network time, not evidence. The coverage ledger re-pays the abstracts automatically, worst day first. **Nothing re-fetches a PDF on its own** once its record exists — that becomes a human's job. |
| `disposable` | `data/raw/`, `data/logs/` | Diagnostics for replaying a parsing bug. Nothing downstream reads them. |

```bash
python3 -m pipelines.migrate pack --tier irreplaceable   # the smallest honest bundle
python3 -m pipelines.migrate pack --tier refetchable      # + PDFs and abstracts
python3 -m pipelines.migrate pack                         # everything (default)
```

`--tier` is cumulative: `refetchable` includes `irreplaceable`. Whatever a
narrower tier leaves behind is named in `MANIFEST.json` under `skipped`, so the
new environment can see the gap rather than discover it later.

---

## 4. Move the folder

The tool stages the bundle; moving it is yours. Anything that preserves bytes
works — the manifest is what proves it arrived intact.

```bash
tar -czf migration.tar.gz -C <repo> migration
# …transfer migration.tar.gz…
tar -xzf migration.tar.gz -C <new repo>
```

For a large `refetchable` tier this is measured in gigabytes. If the channel
has a size limit, pack `--tier irreplaceable`, move that, and let the new
environment re-fetch the rest.

---

## 5. On the new environment

**Clone first.** The knowledge arrives here, not in the bundle.

```bash
git clone <remote> && cd <repo>
pip install -r requirements.txt
```

Put the `migration/` folder at the repository root, then check it before
trusting it:

```bash
python3 -m pipelines.migrate verify --src migration
```

This reads only the bundle — every file's size and sha256 against the manifest
— and reports `missing`, `corrupt` and `unlisted`. A truncated upload shows up
here, not three weeks later as an unreadable paper.

Restore:

```bash
python3 -m pipelines.migrate unpack --src migration --dry-run   # look first
python3 -m pipelines.migrate unpack --src migration
```

Unpack re-verifies each file's checksum before writing it, puts it back at the
path recorded in the manifest, and then answers the question the whole
migration is really asking:

```
restored 1542 file(s)
documents: 1140 claimed, 0 missing
```

**`documents: … 0 missing` is the test that matters.** It is answered from
`data/` and the filesystem, not from the bundle: the records say which papers
hold a document, and the disk says which are there. Any number other than zero
is a real gap — see step 7.

The same check runs on its own at any time:

```bash
python3 -m pipelines.migrate status
```

---

## 6. Carry on

```bash
python3 -m pipelines.render
python3 -m pipelines.enrich.queue stats
python3 -m pipelines.enrich.findings list
python3 -m unittest discover -s tests -t .
```

`render` rebuilds `archive/`, `wiki/` and `outputs/` from `data/`, so anything
derived is correct here by construction even if the transfer was imperfect.
Read its `stale` block: a definition written against three sources when there
are now nine reads as complete while describing a third of its evidence.

Then the ordinary routine resumes — [CLAUDE.md](../CLAUDE.md) step 0 onward.
Nothing about the archive is in a special state after a migration.

`data/index/seen.sqlite` came through git, so the first run does **not**
re-collect everything it has already seen.

---

## 7. When something is missing

| Symptom | What it means | What to do |
| --- | --- | --- |
| `verify` reports `missing` | The transfer was truncated | Re-transfer. The manifest names every file, so you can move only the gap. |
| `verify` reports `corrupt` | Bytes changed in transit | Re-transfer those files. Never unpack over a corrupt payload — unpack refuses each file whose checksum fails, and says which. |
| `documents: N missing` after unpack, and the bundle was `--tier irreplaceable` | Expected. Fetched PDFs were deliberately left behind | Nothing automatic re-fetches them. Re-collect the paper, or fetch its `pdf_url` and drop the file in `inbox/`. |
| `documents: N missing` after a full unpack | A real loss | Check `MANIFEST.json` → `skipped`. If the document is not listed there either, it was already missing before the migration. |
| `record count differs: papers 1284 -> 1190` | **A git problem, never a bundle problem** | The bundle cannot carry records. Something was not pushed, or you cloned the wrong branch. Go back to step 2 on the old container if it still exists. |
| Queue tasks have no `attachments.pdf_path` | Their documents did not arrive | Answer them from the abstract, or restore the documents and re-file. Do not invent content — an empty field is a true statement about what you know. |
| The old container is gone and something was unpushed | Unrecoverable | Re-collect the items. `data/index/rejected.jsonl` and the coverage ledger tell you what the archive knew about. |

---

## 8. Reference

```bash
python3 -m pipelines.migrate status                     # what each channel carries
python3 -m pipelines.migrate pack   [--dest migration] [--tier all] [--move]
python3 -m pipelines.migrate verify [--src  migration]
python3 -m pipelines.migrate unpack [--src  migration] [--dry-run]
```

Global: `--root <path>` to point at another checkout, `--no-checksum` to skip
sha256 (faster, and gives up the completeness guarantee — the manifest still
records sizes).

Exit codes, so a script can rely on them:

| Command | `0` | `1` |
| --- | --- | --- |
| `status` | always | — |
| `pack` | the git half was clean and pushed | it was not — the bundle was still written, and `git_warnings` says why |
| `verify` | every listed file present and intact | anything missing or corrupt |
| `unpack` | every file restored | anything missing from the bundle or failing its checksum |

A file that fails its checksum is **not** written: unpack names it and leaves
whatever was already at that path alone.

### `MANIFEST.json`

| Field | What it is |
| --- | --- |
| `created_at` | When the bundle was packed |
| `tier` | Which tiers were requested |
| `repo` | Remote, branch, HEAD, upstream, unpushed count, and every dirty path at pack time |
| `git_warnings` | What was wrong with the git half when it was packed — empty is what you want |
| `records` | Counts of papers, videos, concepts, findings, pending tasks, topics. The receipt for the git half, re-counted after unpack |
| `totals` | Files and bytes per tier |
| `files` | Every carried file: `path`, `size`, `tier`, `sha256` |
| `skipped` | Every file deliberately not carried, with a reason |

`files` and `skipped` together account for **every** file under the source
roots. That is the guarantee: a bundle is either complete or it says exactly
where it is not.

### What is deliberately *not* in the bundle

- Anything git already carries. Duplicating `data/papers/` here would create a
  second source of truth, and the two would disagree the moment one moved.
- `.venv/`, `__pycache__/`, and other build artefacts. Reinstall instead.
- Credentials and environment variables. The new environment configures its
  own; nothing in this repository stores any.
