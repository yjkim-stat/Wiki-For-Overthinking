# 0013 — A stored transcript is not a video record

| | |
| --- | --- |
| **Commit** | `fix(store): stop reading transcripts as video records` |
| **Scope** | `pipelines/common/store.py`, `tests/test_store.py` |
| **Kind** | fix |

## What changed

`RecordStore.iter_videos` skips `*.transcript.json` and ignores anything that is
not a JSON object.

Transcripts are written into the same directory as the video records, as
`<id>.transcript.json`, which matches the `*.json` glob `iter_videos` uses. A
transcript is a JSON *array* of segments, so `Video.from_dict` received a list
and raised `AttributeError: 'list' object has no attribute 'items'`.

Both `run_daily` and `render` call `rebuild_indexes`, which iterates videos.
There was no partial mode: with one transcript on disk, nothing could be
collected and nothing could be rendered.

## Why it is built this way

**The suffix is now a single constant** that both `transcript_path` and
`iter_videos` derive from. The bug was not that the two disagreed — they agreed
perfectly — but that the agreement was written down twice, in a literal in the
writer and a glob in the reader, with nothing tying them together. One constant
means the next person to change the naming cannot change only one end.

**The shape check is separate from the suffix check**, and deliberately kept
even though the suffix guard alone would fix the reported crash. `data/` is
tracked in git, gets edited by hand, and is the one directory this repository
tells people is the source of truth. A file that is not a record should cost the
run that file, not every entry point. The failure being fixed here is
disproportionate: one malformed file took down the whole pipeline.

**The optional dependency is the real lesson.** `youtube-transcript-api` is an
extra; without it `youtube.py` catches the `ImportError` and returns `[]`, so no
transcript is ever written and the glob never has anything to trip over. The bug
was dormant in exactly the configuration most people run, and detonated for
anyone who installed the dependency the README recommends. The more complete a
deployment made itself, the sooner it broke.

## Trade-offs and rejected alternatives

**Rejected: move transcripts to their own directory.** Cleaner — the ambiguity
would not exist rather than being guarded against — but it is a migration for
every deployed archive, and it would need a breaking-change note and a
relocation step. The suffix guard is sufficient and costs nobody a migration. If
upstream prefers the move later, this constant is the single place it touches.

**Rejected: fix only the suffix, and let a malformed record still raise.** The
crash radius is what makes this critical, not the specific bad file.

**Cost: `iter_videos` now silently skips a file it cannot read.** A record
corrupted into an array disappears from the archive instead of announcing
itself. That is the right trade for a rebuild path that must not stop, but it
does mean corruption is quieter than it was.

## What a reviewer should check

That the tests fail without the fix — they do, and it is worth seeing:

```bash
git stash push pipelines/common/store.py
python3 -m unittest tests.test_store    # 4 errors
git stash pop
```

`test_a_full_render_completes_with_a_transcript_on_disk` is the one that matters:
it is the end-to-end path that was broken, and a fix to `iter_videos` alone that
missed another glob over the same directory would still fail it.

Check also that `load_transcript` still round-trips — the guard must hide
transcripts from the record reader without hiding them from their own.

## Downstream impact

None for configuration. A deployment that installed `youtube-transcript-api` and
then found the pipeline broken should apply this and re-run; no data was lost,
because the crash happened after records were written.
