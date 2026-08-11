# 0036 — A render is not an edit

| | |
| --- | --- |
| **Commit** | `fix(enrich): a concept's last_seen moves only when the concept does` |
| **Scope** | `pipelines/enrich/concepts.py`, `tests/test_layering.py` |
| **Kind** | fix |

## What changed

`harvest` used to stamp `last_seen = utcnow()` on every entity on every pass and
save all of them. An archive that had not changed at all still produced a diff
across every file in `data/concepts/` — one per entity, every render, for ever.

Now the derived record is compared with the stored one, ignoring `last_seen`,
and only a record that actually differs is written. The log says how many
changed:

```
harvested 212 entities from summaries; 3 record(s) changed
```

## Why it is built this way

**`last_seen` is a claim about the evidence, not about the clock.** The name
says when this entity was last seen in a source. Stamping it whenever `harvest`
ran made it mean "when the code last executed", which is already in the run log
and is not worth a field. Comparing the derived record against the stored one is
what turns *the harvest ran* into *something changed*, and the comparison has to
exclude `last_seen` itself or it is circular — hence `_same`.

**Churn is the failure mode this repository is most exposed to.** `data/` is
committed on purpose so a fresh clone is a working archive. A deployment
tracking 200 entities and rendering daily was writing 200 modified files a day
carrying no information, which buries the handful of real changes in every
`git diff`, inflates every commit, and makes "what did today actually change?"
unanswerable from the history. The archive is supposed to accumulate as it is
used; running the code is not using it.

**Skip the write, do not write identical bytes.** Either would leave git clean,
but skipping also leaves the file's mtime alone, which matters to anything that
watches the tree, and it makes the count in the log a true statement about work
done rather than about files touched.

## Trade-offs and rejected alternatives

**A stable entity's `last_seen` now stops advancing**, and that is the intended
reading: it was not seen again, it was merely still there. Anyone who wants
"when did we last confirm this entity still has evidence" is asking a different
question and should ask it of the run log. The field is not a heartbeat.

**Cost: one full record comparison per entity per render.** Two dict
constructions and an equality check against something already in memory — the
records were being serialized and written anyway, so this is strictly cheaper
than what it replaces.

**Rejected: dropping `last_seen` from the schema.** It carries real information
when an entity genuinely gains or loses evidence, and it is the natural field
for a future "what moved this week" report. The bug was in how it was set, not
in its existing.

**Rejected: comparing only `evidence`.** A change to an entity's kind, aliases,
topics or links is also a change worth recording. Comparing the whole record
minus the timestamp needs no list of which fields count, and cannot fall behind
a field added later.

## What a reviewer should check

- **The two tests are a pair, and both are needed.**
  `test_a_full_render_over_an_unchanged_archive_changes_no_record` deletes every
  generated tree, sleeps past a second boundary, renders, and asserts `data/` is
  byte-identical. `test_a_new_mention_does_move_the_record` adds a paper and
  asserts the entity's record *does* change — a quiet render must not become a
  deaf one.
- **The sleep is deliberate.** `utcnow()` has second resolution, so without it
  the first test passes whether or not the bug is present. That is exactly how
  it passed when it was first written, before this fix existed.
- **Mutation-checked:** replacing the `_same` guard with `if False:` (stamp
  every pass) fails the first test.

## Downstream impact

The first render after pulling this rewrites nothing extra; subsequent renders
stop rewriting concept records that have not changed. Expect daily digest
commits to shrink — an archive that used to touch every concept file now touches
only the ones that moved.

No schema change, no migration, no difference in any generated artifact. Records
already on disk keep whatever `last_seen` they were last written with; it simply
stops advancing until the entity's evidence does.
