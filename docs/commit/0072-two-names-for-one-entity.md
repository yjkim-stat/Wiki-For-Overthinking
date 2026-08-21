# 0072 — Two names for one entity

| | |
| --- | --- |
| **Commit** | `feat(duplicates): report concept slugs that are probably the same entity` |
| **Scope** | `pipelines/duplicates.py`, `tests/test_duplicates.py`, `README.md`, `CLAUDE.md`, `workflows/knowledge-and-wiki/README.md` |
| **Kind** | feature |

> Numbered from a block — 0070 onward — reserved for work done in parallel with
> another session holding 0058 onward. The gap is deliberate.

## What changed

```bash
python3 -m pipelines.duplicates
python3 -m pipelines.duplicates --json --limit 20
```

Lists pairs of concept slugs that are probably one entity, with both source
counts and whether each side has a definition. Four rules: separator variants
(`worldmodel` / `world-model`), regular plurals, an `X` / `X model` suffix pair,
and an edit distance of one or two.

It merges nothing and **writes nothing at all**.

## Why it is built this way

**The failure it looks for has no symptom.** The wiki keys entities by the
string a reading wrote, so "world model" in one summary and "world models" in
the next become two records. Each accumulates its own evidence, each crosses the
promotion threshold on its own schedule, each gets its own note — and neither is
wrong about anything, which is why nothing in the pipeline objects. The archive
ends up saying half of what it knows about a term, twice, and the only way to
notice is to read the wiki index looking for it.

`workflows/knowledge-and-wiki/` already warned about the opposite failure — a
generic entity name merging two unrelated things. This is the same key rule in
the other direction, and it had nothing pointed at it.

**It suggests and stops, and that is the design.** Merging is irreversible in
the direction that matters: the loser's evidence is folded into the winner and
afterwards nothing can say the wiki ever held two terms or which reading
contributed what. It is also a judgement no string rule can make — "attention"
and "attentions" are one thing, "GAN" and "GAN inversion" are not, and they are
the same shape. So this produces the input to a person's decision, and the way
to act on it is the alias field of a concept task, which goes through the
validator like every other answer. `CLAUDE.md` already says why: an alias filed
by hand does not merely mislabel, it silently merges two entities.

**Read-only is asserted, not asserted-to.** Two tests, the shape
`tests/test_layering.py` established. The behavioural one snapshots every file
under the sandbox root by content **and modification time**, runs every code
path including the command line, and requires the snapshot unchanged — content
alone would miss a rewrite that produced identical bytes. The static one refuses
to let the module so much as mention a write, which catches one that has merely
been written down on a path no fixture reaches. That is the plausible failure
here: a report naming duplicate entities is one small refactor away from also
merging them.

**Its logging goes to the console and nowhere else.** `common.log.setup` would
create `data/logs/` and a run log inside it. A read-only report has nothing to
say that is worth a file, and "writes nothing" should mean nothing.

**A top-level module, beside `backfill.py` and `serve.py`.** The layering rule
is that only `collect/` and `enrich/` write to `data/` and `publish/` is a pure
function of it. This writes nothing at all, so it belongs to neither half — it
is a command a person runs against the archive, which is what the other two
top-level modules are. Putting it under `enrich/` would file a read among the
writers.

**Tuned for recall.** A pair suggested wrongly costs a glance; a pair never
suggested costs an entity that stays split for ever and stays split invisibly.
Hence: no curated list of permitted suffix words, and an edit bound of two
rather than one. It is affordable precisely because nothing downstream acts on
the output — which is the same argument, from the other end, for why nothing
should.

**One rule per line, all four readable.** `enrich/score.py` established that a
rule somebody can read and correct beats a score nobody can argue with, and this
inherits it. The plural rule in particular is `common/text.py`'s matcher and not
a second copy, so the wiki and topic scoring cannot reach different conclusions
about whether "policy" and "policies" are one word — the argument
[note 0055](0055-one-rule-for-what-counts-as-a-mention.md) makes.

**`fullmatch`, not `search`.** `common/text.py` is built to find a term inside a
document. Asked whether one slug is the plural of another, a search says yes to
"world" inside "world-model" — and then a genuine suffix pair is reported as a
plural, and "world" against "world-model-search" is reported at all. Two tests
fail on exactly that mutation.

**Two bounds that are judgement calls**, both named as constants with the
reasoning beside them:

- `MAX_EDITS = 2`. Three starts relating terms that merely rhyme.
- `MIN_NEAR_LENGTH = 5`. On a four-character slug an edit distance of two
  relates almost everything to almost everything, and a report that suggests
  every pair suggests nothing. The guard is on edit distance only — `gan` and
  `gans` are still paired, by the plural rule, and that is one of the likeliest
  real duplicates in any archive.

**The better-evidenced side is named first**, because it is the likelier
survivor of a merge. Both source counts and both definition flags are shown
because they can point in opposite directions: merging into the defined side
keeps written work, merging into the evidenced side keeps the wiki's
arithmetic, and a pair where those disagree deserves a longer look. Pairs are
ordered by the evidence at stake, so the list is skimmed from the top.

**Deterministic throughout.** Every tie falls back to the slug, so two runs over
an unchanged archive print the same list in the same order — otherwise `--limit`
would show a different twenty each time.

## Trade-offs and rejected alternatives

**It compares slugs, not aliases.** A concept whose alias already equals another
concept's name is a strong duplicate signal and is not used. That is a genuine
gap, deliberately left: it is a different question — "has somebody already
decided these are the same and only half-applied it" — and folding it in would
mix a suggestion with a record of a decision.

**Quadratic in the number of concepts.** Every pair is compared. A length
prefilter and an early exit inside the distance keep the constant small, and a
wiki with thousands of entities is one where this report is worth several
seconds. If it ever is not, the fix is bucketing by first letter, which would
lose exactly the typos in the first letter.

**Considered: a curated list of suffix words** — model, method, framework,
network. Rejected. It reads well and it would miss whatever the group's own
field calls the same idea, which is the failure the report exists to catch. Any
single trailing word is the looser and more honest rule; two trailing words is
where it stops, because two extra words is usually a narrower thing rather than
the same thing named longer.

**Considered: an `--apply` or `--merge` flag** behind a confirmation. Rejected
outright, and not as a later feature either. It would give an automated path to
the one edit `CLAUDE.md` singles out as silently destructive, and the report's
recall tuning is only defensible while nothing acts on it.

**Considered: emitting findings for the pairs it suggests.** Rejected: a
finding is what the group settled, and a string rule has settled nothing. It
would also be a write.

**Discoverability is thin in `CLAUDE.md` on purpose.** It appears in the common
commands list, and the full explanation lives in
`workflows/knowledge-and-wiki/`, next to the generic-name failure it mirrors.
This is not a daily command — it is worth running when the wiki has grown — and
the daily routine is long enough.

## What a reviewer should check

Nine mutations, each against the full suite:

- `variant` rule disabled → `test_a_separator_that_is_not_there_is_a_variant`.
- `fullmatch` → `search` in the plural rule → two tests:
  `test_one_extra_trailing_word_is_a_suffix_pair` (a suffix pair reported as a
  plural) and `test_two_extra_words_are_not` (an unrelated pair reported at all).
- Suffix rule accepting any number of extra words → `test_two_extra_words_are_not`.
- `MIN_NEAR_LENGTH` 5 → 0 → `test_short_slugs_are_not_compared_by_edit_distance`.
- `MAX_EDITS` 2 → 3 → `test_three_edits_apart_is_not`.
- Within-pair order reversed → `test_the_better_evidenced_side_is_named_first`
  and `test_a_pair_carries_both_source_counts_and_both_definitions`.
- Identity guard removed → `test_a_slug_is_not_a_duplicate_of_itself`. Nothing
  else catches it: `combinations` never yields a slug against itself, so only
  the unit test reaches that line.
- **`run()` made to actually merge** — alias the loser onto the winner and save
  → three tests, one static and two behavioural. This is the mutation the whole
  file exists for.
- **`logging.basicConfig` → `common.log.setup(cfg.layout.logs, ...)`** → both
  write tests. Worth reading the second one's docstring: `log.setup` configures
  the root logger *once per process*, so on the first attempt this mutation was
  caught only by whichever test ran first, and the other passed against exactly
  the mutation it exists to catch. It now clears and restores the flag, and both
  bite.

## Downstream impact

New command; nothing existing changes. No record, no config, no template, no
scheduled job runs it. A deployment that never runs it is exactly as it was —
and one that does should expect a first run to be the noisiest, since it reports
against every concept the wiki has ever grown.
