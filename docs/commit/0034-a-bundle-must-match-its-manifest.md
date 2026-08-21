# 0034 — A bundle must match its manifest

| | |
| --- | --- |
| **Commit** | `fix(migrate): a bundle that carries more than its manifest is not verified` |
| **Scope** | `pipelines/migrate.py`, `tests/test_migrate.py`, `migration/README.md` |
| **Kind** | fix |

## What changed

Eighteen tests that check pack and unpack against the filesystem rather than
against their own report, and the two defects that writing them exposed.

**`verify` no longer passes a bundle carrying files its manifest does not
describe.** `unlisted` was reported and then ignored when computing `ok`.

**`pack` refuses a destination that already holds a payload.** It used to write
into it, leaving the earlier pack's files underneath.

Together those were one concrete failure. Pack everything, then re-pack the
same folder as `--tier irreplaceable`, and the result was a manifest listing 1
file over a payload holding 4 — a bundle that shipped the very documents the
narrowed tier claimed to have dropped, while `verify` said `ok`. Reproduced
before either fix; both are now asserted.

## Why it is built this way

**A bundle's only real claim is its inventory.** It travels over a channel
nobody controls, and every other guarantee — nothing missing, nothing corrupt,
nothing left behind by a narrower tier — is read off the manifest. A file that
nothing describes breaks no restore, and that is exactly why it was easy to wave
through; but a bundle that cannot account for what it carries has not been
verified, it has only been partially checked. So `unlisted` fails.

**Refusing to re-pack, rather than clearing the folder.** Clearing is the
obvious fix and it can destroy an archive: a previous run with `--move` left the
payload as the *only* copy of those documents, and `pack` cannot tell that run
apart from a harmless one. So it stops, says how many files are in the way, and
names the `--move` risk. `--replace` deletes them, and the choice is the
caller's — which is the right place for it, because only the caller knows how
the earlier bundle was made.

**The new tests check the work, not the report.** `pack` returning a manifest
that says four files were written is not evidence that four files were written.
So the assertions read the payload back: every packed file byte-identical to its
original, every recorded sha256 recomputed independently, totals matched against
`stat()`, and `files ∪ skipped` covering every file under the source roots. The
same on the other side — restored bytes compared with the originals, not with
the manifest.

**The cost of `--no-checksum` is asserted rather than described.** One test
shows it still catches a size change and *misses* a same-size edit. A flag whose
downside lives only in prose tends to be read as a free speed-up.

## Trade-offs and rejected alternatives

**`unlisted` is now fatal, and some of them are harmless.** Someone who drops a
note into `payload/` gets a failure. That is the intended trade: the payload is
tool-owned, the folder above it is not, and `verify` only scans the payload.
Anything a human wants to add travels beside `MANIFEST.json`, not under it.

**Rejected: pruning stale payload files automatically.** The tempting middle
path — delete only files the new manifest does not list — has the same
`--move` failure mode as clearing, and it is worse for being quiet about it.

**Rejected: making `pack` exit non-zero but continue when the destination is
dirty.** It already exits 1 for git warnings while writing a usable bundle,
because a container about to be reclaimed makes a partial rescue worth having.
A dirty destination is different: there is no rescue to salvage, and continuing
produces the misleading bundle this note is about. Nothing is written.

## What a reviewer should check

- **That the tests bite.** Each fix was mutation-checked:

  | Mutation | Result |
  | --- | --- |
  | `if not replace:` → `if False:` | 1 failure |
  | `ok` drops `and not extra` | 1 failure |
  | unpack writes a file that failed its checksum | 1 failure |

- **The corrupt-file path, which had no test before.** `unpack` must refuse the
  file, name it in `checksum_failed`, and leave whatever was already at that
  path untouched — that last part is what makes a re-transfer safe.
- **`test_files_and_skipped_together_account_for_every_source_file`.** It walks
  the source roots itself rather than trusting `build_plan`, so it fails if a
  new root is ever added to the packer without being covered.
- **The refusal message**, which has to be actionable enough that somebody who
  has just been stopped knows whether `--replace` is safe for them.

## Downstream impact

`verify` is stricter: a bundle that passed before and carried unlisted files now
fails, with the paths named. Re-pack with `--replace` or transfer a fresh
bundle; restoring from the old one still works, it is the inventory that cannot
be trusted.

`pack` gains `--replace`. Scripts that repeatedly pack into a fixed `--dest`
must pass it, or they now stop with exit 1 and write nothing.
