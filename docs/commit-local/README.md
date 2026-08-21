# Commit notes — local

> **Reopened by this deployment at 0033.** Everything from 0009 to 0032 below
> is the upstream archive's history and is closed, exactly as its own preamble
> says. This checkout is a *deployment* of that repository — it has a `src`
> remote and pulls version updates from it — so it is in the position 0009-0032
> were written from, and it needs a sequence `src` will not also advance.
> `docs/commit/` is the template's and this deployment never writes there;
> notes 0033 on are this deployment's own. See
> [`0036`](0036-taking-the-template-back-in-a-second-time.md) for why three of
> them carry numbers they were not first pushed with.

> **The paragraphs below are upstream's, and describe 0009-0032 only.**
>
> **This directory is history, and it is closed.** It holds the notes the
> archive wrote while it lived in a repository of its own, alongside a checkout
> of the template it was built from. Since 2026-08-12 there is one repository:
> `docs/commit/` is this repository's own sequence and **every new note goes
> there**. Nothing is added here. The `src` remote these notes describe does not
> exist in this checkout, so a command quoted inside one is a record of what was
> run at the time, not an instruction. The current procedure is in
> [`../LOCAL-DELTAS.md`](../LOCAL-DELTAS.md).
>
> They are kept because a note explains why a decision was taken, and most of
> the code under `pipelines/local/` and every `# LOCAL` mark in the tree is only
> arguable from what is written here.

These notes are kept apart from `docs/commit/` because both histories number
from 0000 and both reached 0009 with entirely different content, so a shared
directory would collide — and a bare cross-reference by number silently resolves
to the wrong note.

Numbering starts at 0009 rather than 0001 on purpose. Notes 0000-0008 are
shared with the template and still live in `docs/commit/`; these notes carry the
numbers they were pushed with, and several cross-reference each other by number
(0018 corrects 0014, and 0014 carries the matching correction section). The rule
that a pushed note is never rewritten outranks tidy numbering.

See `docs/LOCAL-DELTAS.md` for what this deployment changes in the template.

| # | Note | Kind | Why |
| --- | --- | --- | --- |
| 0009 | [Point the source lists at the LLM reasoning literature](0009-sources-for-llm-reasoning.md) | config · breaking | A topic can only match what is collected, so `cs.CL` decides everything |
| 0010 | [Track LLM reasoning as four topics](0010-four-reasoning-topics.md) | config | Split by where the reasoning comes from, not by what it is applied to |
| 0011 | [A model is not a dataset: the wiki gains a `model` kind](0011-a-model-is-not-a-dataset.md) | feature · breaking | The schema decides what readers can record; a checkpoint is not a corpus |
| 0012 | [Applying a topic change to what is already stored](0012-retopic-stored-records.md) | feature | Topics match at collection time; editing one has to be applicable afterwards |
| 0013 | [A fifth topic, because two papers had no home](0013-a-fifth-topic-for-interpretability.md) | config | A topic created by evidence that accumulated, not by prediction |
| 0014 | [Plurals belong in the matcher, not in every keyword list](0014-plurals-in-the-keyword-matcher.md) | fix · breaking | A silent miss is worse than a loud one; fix the mechanism, not the list |
| 0015 | [Cover the model kind and the two maintenance scripts](0015-tests-for-the-model-kind-and-the-scripts.md) | test | The rank rule and the classification asymmetry are what a test protects |
| 0016 | [Turn off OpenReview: it now demands a bot challenge](0016-turn-off-openreview.md) | config | A collector that cannot succeed should not be asked to try on every run |
| 0017 | [`get_json` was refusing every caller that sent a header](0017-get-json-header-collision.md) | fix | A fail-soft pipeline turned a TypeError into a log line nobody read |
| 0018 | [Duplicate keywords double-count: a regression from 0014](0018-duplicate-keywords-double-count.md) | fix | The matcher owns pluralisation; the lists must not share the job |
| 0019 | [A way to say "this was collected in error"](0019-a-way-to-say-this-was-collected-in-error.md) | feature · destructive | The archive had no way to be wrong; dry run is the default here |
| 0020 | [A placeholder is not a name](0020-a-placeholder-is-not-a-name.md) | fix · breaking | The wiki keys entities by string, so a generic phrase manufactures its own corroboration |
| 0021 | [The model kind reached half the pipeline](0021-the-model-kind-reached-half-the-pipeline.md) | fix | A field with a default looks empty by design; only the applier can lose it silently |
| 0022 | [A reading backlog starved the wiki](0022-a-reading-backlog-starved-the-wiki.md) | fix | Two kinds of work, one cap: reserve rather than reorder |
| 0023 | [A title is not enough to score a paper](0023-a-title-is-not-enough-to-score-a-paper.md) | feature · scoring | DBLP carries no abstracts, so which index found a paper decided how it was judged |
| 0024 | [Take the template update, and put our work somewhere it survives the next one](0024-take-the-template-update-and-separate-our-work.md) | feature · breaking layout | The template wins; make that cheap instead of painful |
| 0025 | [Re-queue what the evidence outgrew](0025-re-queue-what-the-evidence-outgrew.md) | feature | Growth, not staleness, is the thing to threshold on |
| 0026 | [A correlate is not a mechanism](0026-a-correlate-is-not-a-mechanism.md) | docs | Three footnotes in three papers that only mean something together |
| 0027 | [The directory split reached the docs but not the skill](0027-the-split-reached-the-docs-but-not-the-skill.md) | fix · docs | A procedure is executed; a layout table is consulted. The procedure wins silently |
| 0028 | [The ledger waited for the part that never finished](0028-the-ledger-waited-for-the-part-that-never-finished.md) | fix | The cheap half produced the irreplaceable number and was held hostage by the expensive half |
| 0029 | [A listing record with no date is second-class](0029-a-listing-record-with-no-date-is-second-class.md) | fix | Which collector found a paper decided where it was filed |
| 0030 | [One topic with results hid the others](0030-one-topic-with-results-hid-the-others.md) | fix | The fallback gate was inverted against its own purpose: whoever needed it most never got it |
| 0031 | [The migration payload must never be committed](0031-the-migration-payload-must-never-be-committed.md) | chore · safety | The routine runs `git add -A` unattended; one line is the whole defence |
| 0032 | [Two passes over one backlog reported it twice](0032-two-passes-over-one-backlog-reported-it-twice.md) | fix · reporting | A render that filed nothing said it filed 74 |
| 0033 | [A benchmark sitting is one entity, however it was spelled](0033-a-benchmark-sitting-is-one-entity-however-spelled.md) | fix · superseded | AIME split across eight spellings; the code is dropped in 0036 and the ruling moved to the alias map |
| 0034 | [Taking the template back in](0034-taking-the-template-back-in.md) | chore | The first merge from `src`, and the first note-number collision |
| 0035 | [A source that answers 403 to everything](0035-a-source-that-answers-403-to-everything.md) | chore | OpenReview refused every request from two hosts on the same day |
| 0036 | [Taking the template back in, a second time](0036-taking-the-template-back-in-a-second-time.md) | chore · breaking | A plain merge would have deleted 4,418 archive files; and this deployment stops writing in `docs/commit/` |
| 0037 | [A ruling takes the question with it](0037-a-ruling-takes-the-question-with-it.md) | fix | A fifth of the queue was definition tasks for entities an alias ruling had already retired |
| 0038 | [Collection moves to local cron](0038-collection-moves-to-local-cron.md) | docs · operational | The cloud routine cannot reach arXiv; a day the listing never browsed is a day lost for good |
| 0039 | [A URL the identifier already implies](0039-a-url-the-identifier-already-implies.md) | fix | A bibliographic index carries no document, but the arXiv id it resolved to says where one is |
| 0040 | [The cloud routine is turned off](0040-the-cloud-routine-is-turned-off.md) | docs · operational · breaking | Collection is automated, reading is not; the steady state is a growing backlog, and that is deliberate |
| 0041 | [ACL is reached through DBLP, or not at all](0041-acl-is-reached-through-dblp-or-not-at-all.md) | config · editorial | The one venue with no programme page and no OpenReview, so its abstracts come from the Anthology or nowhere |
| 0042 | [The noise was inside the top tier](0042-the-noise-was-inside-the-top-tier.md) | chore · editorial · breaking | 72 of the 90 discarded readings were ICLR/ICML/NeurIPS papers; venue was never the axis |
| 0043 | [The upstream that is behind us](0043-the-upstream-that-is-behind-us.md) | chore · merge · breaking | `src` was repointed to a repository that is this pipeline with the LOCAL marks stripped; the wholesale-checkout recipe would have reverted 0039 and deleted the `model` kind |
