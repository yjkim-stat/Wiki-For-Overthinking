# 0033 — Carrying an archive between environments

| | |
| --- | --- |
| **Commit** | `feat(migrate): carry the untracked half of an archive between environments` |
| **Scope** | `pipelines/migrate.py`, `migration/README.md`, `tests/test_migrate.py`, `.gitignore`, `CLAUDE.md`, `README.md` |
| **Kind** | feature |

## What changed

`python3 -m pipelines.migrate` and a `migration/` folder, for moving an archive
into a fresh container running the same repository.

```bash
python3 -m pipelines.migrate status    # what each channel carries, and whether it can
python3 -m pipelines.migrate pack      # → migration/payload/ + MANIFEST.json
python3 -m pipelines.migrate verify    # payload against its manifest
python3 -m pipelines.migrate unpack    # restore, then check against the records
```

`migration/README.md` is the procedure, and it is deliberately the whole of it:
the environment that has to follow those instructions is the one that has just
cloned and has nothing else to read. It is the only tracked file in the folder;
the payload is gitignored.

## Why it is built this way

**Two channels, and only one of them is automatic.** `data/` is committed on
purpose — a scheduled run starts from a fresh clone — so the knowledge already
travels by git. What does not travel is what git is told to ignore: documents,
announced abstracts, raw responses, logs. The bundle carries that and nothing
else. Copying `data/papers/` in as well would create a second source of truth,
and the two would disagree the moment either moved.

**The expensive failure is not a dropped PDF.** It is a container discarded
while `main` was still behind the working tree, which is silent at both ends:
the bundle looks complete and the clone looks healthy. So `pack` inspects the
git half first — dirty tree, missing upstream, unpushed commits — writes the
findings into the manifest, prints them, and exits non-zero. It still writes the
bundle: refusing outright would be the wrong answer when a container is about to
be reclaimed and a partial rescue beats none.

**Tiers say what it costs to lose a file, not how big it is.** A hand-filed PDF
has no URL anywhere; when it goes, the record that describes it stays behind
pointing at nothing, which is worse than an obvious gap. A fetched PDF has a
`pdf_url`. Abstracts are re-paid by the coverage ledger automatically. Raw
responses and logs are diagnostics. Hence `irreplaceable` / `refetchable` /
`disposable`, cumulative, so a transfer with a size limit can carry the first
tier and *know* what it gave up rather than discover it later.

A document on disk that no record claims is filed as `irreplaceable`. Its
provenance cannot be established, so it cannot be shown to be re-fetchable, and
the safe reading of "unknown" is the one that does not throw the file away.

**The completeness guarantee is the manifest, not the copy loop.** Every file
under every source root appears in either `files` or `skipped`, with a reason —
no sampling, no cap. That is what makes "nothing was left behind" checkable
instead of merely claimed, and it is why `verify` can run at the far end before
anything is restored: a truncated upload should surface then, not three weeks
later as an unreadable paper.

**The success criterion is answered from `data/`, not from the bundle.** After
unpack, `check_documents` walks the paper records, and for each one that claims
a `local_path` asks whether the file is there. That is the question a migration
is actually asking, and it stays answerable long after the bundle is deleted —
`status` reports it too.

**Hard links, and `--move` is opt-in.** Packing a PDF store by copy can be the
thing that exhausts a container's fixed disk allowance. The files are
content-addressed and never rewritten in place, so two names for one inode is
safe; a copy is the fallback across filesystems. `--move` destroys the original,
which is unrecoverable if the transfer then fails, so it is never the default.

## Trade-offs and rejected alternatives

**The transfer itself is not automated, and should not be.** The tool stages a
folder; moving it is `tar`, an upload, `scp` — whatever the environments share.
Building a transport in would mean choosing a service, holding credentials, and
owning a failure mode that has nothing to do with archives. The manifest is what
makes an untrusted channel safe.

**Rejected: committing the payload, or git-lfs.** Both defeat every reason the
files are ignored — repository weight, and documents that are not ours to
redistribute. `.gitignore` gained `/migration/*` with `!README.md` precisely so
a pack cannot accidentally be committed.

**Rejected: reading `.gitignore` to decide what to pack.** Tempting, and wrong:
the question is what the *archive* needs, and a deployment that edits its ignore
rules should not silently change what a migration carries. The roots are named
in `_UNTRACKED_ROOTS` instead, next to the tier logic that interprets them.

**Checksums are on by default and cost a full read of the payload.** For a
multi-gigabyte PDF store that is minutes. `--no-checksum` exists and the
manifest still records sizes, but it gives up the guarantee, and the doc says
so rather than presenting it as a free speed-up.

**A migration does not carry credentials or environment variables.** Nothing in
this repository stores any; the new environment configures its own.

## What a reviewer should check

- **A round trip, which the tests do end to end.** `tests/test_migrate.py`
  builds two checkouts: one packs, the other receives only `data/` (what a clone
  delivers) and then the bundle. It asserts the fresh clone starts with two
  records pointing at documents it lacks, and that after unpack `missing` is 0
  and the bytes match.
- **That a narrow tier's gap stays visible.** Packing `--tier irreplaceable` and
  unpacking leaves exactly the fetched document missing, and the test names it.
- **The tier rules against a real record.** A hand-filed paper (`source: local`,
  no `pdf_url`) must be `irreplaceable`; an arXiv paper with a `pdf_url` must be
  `refetchable`. Both are asserted; break `_hand_filed` and they fail.
- **The failure paths, by hand:**

  ```bash
  python3 -m pipelines.migrate --root <old> pack --dest migration
  tar -czf b.tgz -C <old> migration && tar -xzf b.tgz -C <new>
  printf tampered > <new>/migration/payload/<some file>
  python3 -m pipelines.migrate --root <new> verify --src migration   # exit 1, names it
  python3 -m pipelines.migrate --root <new> unpack --src migration   # refuses that file
  ```

  Verified in exactly this form, including that a checksum failure leaves
  whatever was already at the destination path alone.
- **Exit codes**, which `migration/README.md` documents as a table because
  scripts will depend on them.

## Downstream impact

Additive. No existing command changes, no record changes, nothing is
regenerated differently. A deployed copy gains the `migration/` folder and its
README on the next pull; the folder stays empty until somebody packs into it.

Deployments that already have a `migration/` directory for something else should
rename it — `.gitignore` now claims that path.

This repository is a template with no archive of its own, so the mechanism was
exercised against constructed checkouts rather than a real deployment's PDF
store. The tier logic reads real record fields (`source`, `pdf_url`,
`local_path`), so a deployment should run `status` first and confirm the tier
counts look like its archive before trusting a narrow `--tier`.
