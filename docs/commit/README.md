# Commit notes

One note per commit, in commit order. Each explains what changed, why it is
built that way, what it costs, and what a reviewer should check.

This repository is meant to be deployed into other projects. These notes are
how someone decides what to keep and what to replace without having to
reconstruct the reasoning from the code.

The practice is enforced by the `commit-notes` skill in
[`.claude/skills/commit-notes/`](../../.claude/skills/commit-notes/SKILL.md):
before any commit, the pending work is split into commits that each carry one
idea, and each gets a note here, staged in the same commit. Routine archive
digest commits are exempt — they change data, not the system.

Note 0000 is the exception to "one note per commit": it is a retroactive
reference for everything built before the practice existed.

## Index

| # | Note | Kind | What it establishes |
| --- | --- | --- | --- |
| 0000 | [Baseline: the pipeline as inherited](0000-baseline-the-inherited-pipeline.md) | reference | The load-bearing decisions of the original system, written down after the fact |
| 0001 | [Adopt the commit-note practice](0001-adopt-commit-notes.md) | chore | No change to the system lands without a note |
| 0002 | [Retire the subject-specific defaults and identifiers](0002-field-neutral-defaults.md) | refactor | Defaults are what people run; none of them name a field any more |
| 0003 | [Field-neutral fixtures and examples](0003-field-neutral-fixtures.md) | refactor | A test should be readable by someone who does not know the field |
| 0004 | [Reframe as a recipe for research team management](0004-reframe-as-a-team-recipe.md) | docs | The repository states the job it does, not the subject it was first used on |
| 0005 | [Make `rebuild_archive` actually rebuild](0005-rebuild-archive-from-scratch.md) | fix | `archive/` really is a pure function of `data/`, stale pages and all |
| 0006 | [Hand-filed PDFs](0006-hand-filed-pdfs.md) | feature | A person is a source too: drop a PDF in `inbox/` and it becomes an ordinary paper |
| 0007 | [A map of the repository in the README](0007-readme-layout.md) | docs | Three kinds of directory: yours, the source of truth, and derived |
| 0008 | [The layout table in `CLAUDE.md`, rewritten as write permissions](0008-claude-md-layout.md) | docs | An agent asks "may I write here", not "where do I look" |
| 0009 | [Collect from the venues' own programme pages](0009-venue-programme-pages.md) | feature | The venue is the authority on what it accepted; a title is scored before an abstract is fetched |
| 0010 | [Retry a truncated response](0010-retry-truncated-responses.md) | fix | A transient truncation costs a retry, not a topic's results |
| 0011 | [`get_json` collided with its own Accept header](0011-get-json-header-collision.md) | fix | A collector that had never sent a request; and the stub that hid it |
| 0012 | [The Semantic Scholar venue filter is opt-in](0012-venue-filter-is-opt-in.md) | fix · breaking | A default whose failure mode is silent absence is not a safe default |
| 0013 | [A stored transcript is not a video record](0013-transcripts-are-not-records.md) | fix | One unreadable file cost every entry point; an optional dependency hid it |
| 0014 | [A chapter timestamp is required, not defaulted](0014-chapter-timestamps-are-required.md) | fix · breaking | A missing value that renders as a plausible 0:00 is worse than a rejection |
| 0015 | [A ruled `kind` defends itself against the next harvest](0015-a-ruled-kind-defends-itself.md) | fix | A deliberate judgement outranks a majority vote over field placement |
| 0016 | [A paper's `relevance` is checked against the topics it has](0016-relevance-keys-are-checked.md) | fix · breaking | The validator could not see the one thing that made the record wrong |
| 0017 | [Keywords match regular plurals](0017-keywords-match-regular-plurals.md) | feature | A rule one letter off looks exactly like a quiet week |
| 0018 | [Stop asking a host that has failed all run](0018-give-up-on-a-dead-host.md) | feature | Retry is per request; a dead source is per run |
| 0019 | [A submitted result can be corrected](0019-reopen-a-submitted-task.md) | feature | A path back through the validator, so nobody edits `data/` by hand |
| 0020 | [Read the programme out of the `<noscript>` block](0020-programme-listings-read-the-noscript-block.md) | fix | The navbar's login link points at a poster path; only the fallback holds papers |
| 0021 | [Report what has gone stale](0021-report-what-has-gone-stale.md) | feature | An empty queue means nothing is unwritten, not that nothing is out of date |
| 0022 | [Fetch the document before asking anyone to read it](0022-fetch-the-document-before-reading-it.md) | feature | An abstract is a claim about a paper; the experiments section is a record of it |
| 0023 | [One place for reading a page nobody gave us an API for](0023-shared-html-reading.md) | refactor | Two collectors ask a page for the same three things |
| 0024 | [Read arXiv's listing pages when the API will not answer](0024-arxiv-listing-fallback.md) | feature | The API and the website are different hosts; a block on one is not a block on both |
| 0025 | [Know what a day held, not just what we found](0025-coverage-ledger-and-the-sweep.md) | feature | The source's own count is the only number we did not compute |
| 0026 | [Keep the ledger, not the abstracts](0026-abstracts-are-not-committed.md) | chore | The audit survives a fresh clone; the text it audits is re-fetched against it |
| 0027 | [A reference for every external request the pipeline makes](0027-external-source-reference.md) | docs | Each source says what it cannot tell you, not only what it can |
| 0028 | [The backlog is what is left in `data/pdfs/`](0028-shelve-documents-once-read.md) | feature | A read document moves on, so the directory answers what is still owed |
| 0029 | [The wiki, drawn](0029-the-wiki-drawn.md) | feature | Colour computed, not chosen — and the computation changed the encoding |
| 0030 | [What the group settled](0030-what-the-group-settled.md) | feature | The one record the group authors itself — filed where it cannot be mistaken for evidence |
| 0031 | [Fetch before you start](0031-fetch-before-you-start.md) | docs | A long-lived session holds a `main` that has moved underneath it |
| 0032 | [Following somebody else's reading](0032-following-somebody-elses-reading.md) | feature | A curated list gives pointers, never metadata — a nickname is not a title |
| 0033 | [Carrying an archive between environments](0033-carrying-an-archive-between-environments.md) | feature | Git carries the knowledge; the bundle carries what git refuses, tiered by what losing it costs |
| 0034 | [A bundle must match its manifest](0034-a-bundle-must-match-its-manifest.md) | fix | A narrowed re-pack shipped what it claimed to have dropped, and `verify` said ok |
| 0035 | [Rendering does not write to `data/`](0035-rendering-does-not-write-to-data.md) | refactor · breaking | The renderer derived the records it drew; the code is replaced, the archive is not |
| 0036 | [A render is not an edit](0036-a-render-is-not-an-edit.md) | fix | Every pass restamped every entity, so an unchanged archive still produced a diff |
| 0037 | [The rules a deployment lives under](0037-the-rules-a-deployment-lives-under.md) | docs | One premise — the code is replaced, the archive is not — and what follows from it |
| 0038 | [One folder per task, and its harness](0038-one-folder-per-task-and-its-harness.md) | docs | Procedures were scattered; what checks them, and what checks nothing, was nowhere |
| 0039 | [Name the deployment root once, and mean it everywhere](0039-name-the-deployment-root.md) | feature | The archive can live in a repository of its own; a root named but missing is refused, never fallen back from |
| 0040 | [A template is resolved against the deployment, then against the code](0040-a-template-is-resolved-per-file.md) | feature | Override one template and go on receiving every other; copying a directory is how a deployment stops getting improvements |
| 0041 | [`daily.sh` hands the root to every stage](0041-daily-sh-hands-the-root-to-every-stage.md) | fix | It collected into the deployment and rendered the code checkout, exiting 0 both times |
| 0042 | [Two roots, and the workflow that keeps them apart](0042-two-roots-and-the-workflow-between-them.md) | docs | The archive can live in a repository of its own; the reason is the list of files that collide |
| 0043 | [`generated_by` names the backend, not the task kind](0043-generated-by-names-the-backend.md) | fix | A fallback through `task["kind"]` stamped 242 consecutive readings `"paper"`, and nothing reads the field |
| 0044 | [A reading says what it was based on](0044-a-reading-says-what-it-was-based-on.md) | feature | The document being available is not the document being read, and only the reader can tell you which |
| 0045 | [A ruled link is not derived away](0045-a-ruled-link-is-not-derived-away.md) | feature | The task asked for `related`, the same render rebuilt the record without it, and every step reported success |
| 0046 | [The PDF cap bounds a run, not a call](0046-the-pdf-cap-bounds-a-run.md) | fix | Collection fetches one paper at a time, so `max_per_run` restarted on every paper and bounded nothing |
| 0047 | [A filed document survives its merge](0047-a-filed-document-survives-its-merge.md) | fix | `source` merged and `local_path` did not, so the archive knew it held a hand-filed paper and not where |
| 0048 | [A second chance at a document](0048-a-second-chance-at-a-document.md) | feature | Collection fetches only for papers arriving that run, so a backlog keeps its abstracts for ever |
| 0049 | [A citation rather than a rumour](0049-a-citation-rather-than-a-rumour.md) | feature | What a session checked on the web lived in a finding's prose; a reference has a date, a quotation, and no vote on promotion |
| 0050 | [Three claims, three weights](0050-three-claims-three-weights.md) | fix | The edge literal outlived the field it named, so a person's link was drawn as the faintest thing on the page |
| 0051 | [A citation appears, where it is not evidence](0051-a-citation-appears-where-it-is-not-evidence.md) | feature | `## Checked against`, below the sources and never among them — the visible half of the record split |
| 0052 | [A task is a function of its record](0052-a-task-is-a-function-of-its-record.md) | fix | The correct task was rebuilt on every render and discarded on every render, so a fetched document never reached its reader |
| 0053 | [The other direction of the same question](0053-the-other-direction-of-the-same-question.md) | feature | A document no record claims was invisible, and silently sized every migration bundle |
| 0054 | [The queue reports what it wrote](0054-the-queue-reports-what-it-wrote.md) | fix | `summaries_queued` counted the backlog, so it read the same on every render — which is how 0052 stayed hidden |
| 0055 | [One rule for what counts as a mention](0055-one-rule-for-what-counts-as-a-mention.md) | refactor | Search and scoring must not disagree about what a mention is, and a second copy is how they would |
| 0056 | [A read-only window onto the archive](0056-a-read-only-window-onto-the-archive.md) | feature | Colleagues on the same host can ask what it knows; it answers only from what it has read, and writes nothing |
| 0057 | [A change is asked for through a person](0057-a-change-is-asked-for-through-a-person.md) | feature | The write lane: no auto-approved category, a hostile drop folder, and a decision that keeps its reason |
| 0058 | [A stale definition is asked for again](0058-a-stale-definition-is-asked-for-again.md) | feature | Reporting staleness never fixed it, and the manual route discarded the ruling along with the rot |
| 0059 | [An identifier learned late is still registered](0059-an-identifier-learned-late-is-still-registered.md) | fix | A hand-filed paper's arXiv id arrived after collection and was never indexed, so the collector forked instead of folding |
| 0060 | [A question larger than one reading](0060-a-question-larger-than-one-reading.md) | feature | Cross-cutting work had no place in the queue; a settled answer is a finding, and an open one is still an answer |
| 0061 | [A look outside that has to cite what it saw](0061-a-look-outside-that-has-to-cite-what-it-saw.md) | feature | Requiring a reference is the only mechanical difference between looking something up and remembering it |
| 0070 | [One leverage, beside the scores it sums](0070-one-leverage-beside-the-scores-it-sums.md) | refactor | Two callers wanted the same number; two copies would be free to disagree |
| 0071 | [Which end of the backlog to drain](0071-which-end-of-the-backlog-to-drain.md) | feature | Filename order is alphabetical order, so a partial drain was reading the archive by arXiv number |
| 0072 | [Two names for one entity](0072-two-names-for-one-entity.md) | feature | A term spelled two ways splits into two records, and neither is wrong about anything — so the report suggests and writes nothing |
| 0073 | [A model is not a dataset](0073-a-model-is-not-a-dataset.md) | feature · breaking | A checkpoint and a corpus answer different questions; a schema change has no seam to hide behind |
| 0074 | [Local extensions in a package of their own](0074-local-extensions-in-a-package-of-their-own.md) | feature | A placeholder is a false entity, a record with no abstract cannot be scored, and one cap starved the wiki |
| 0075 | [Three fixes that only made collection quieter](0075-three-fixes-that-only-made-collection-quieter.md) | fix | Under-collecting looks exactly like a quiet day, and a test inside a replaceable file cannot guard it |
| 0076 | [The archive this repository keeps](0076-the-archive-this-repository-keeps.md) | feature · breaking | Both roots are one tree here; `data/` is committed because a scheduled run starts from a fresh clone |
| 0077 | [Everything the archive needs is in the repository](0077-everything-the-archive-needs-is-in-the-repository.md) | docs | Knowledge that lives only outside the repository is knowledge the next session does not have |
| 0078 | [A kind that is accepted is offered](0078-a-kind-that-is-accepted-is-offered.md) | fix | The validator took four kinds and the reader was shown three, and a stored definition freezes the kind |
| 0079 | [A field with no validator is a field that goes missing](0079-a-field-with-no-validator-is-a-field-that-goes-missing.md) | fix | `models` was accepted, applied and never checked, so nine readings lost it without a word |
| 0080 | [Taking the update, and giving up our numbers](0080-taking-the-update-and-giving-up-our-numbers.md) | chore | Two sessions numbered from the same stale index; the one that had not pushed is the one that moves |
| 0081 | [One entity, many names](0081-one-entity-many-names.md) | feature | AIME 2024 was three records holding 9, 28 and 2 sources, each defined against its own fraction |
| 0082 | [A condition that its own effect falsifies](0082-a-condition-that-its-own-effect-falsifies.md) | feature | The write condition re-tested what the line above had just emptied, so five records were cleared and never written |
| 0083 | [Twenty-seven names ruled, and eleven refused](0083-twenty-seven-names-ruled-and-eleven-refused.md) | feature | Base and instruct are different weights; the largest ruling in the file is a refusal to merge |
| 0084 | [A counter that counts attempts](0084-a-counter-that-counts-attempts.md) | fix · superseded | Ours; `origin/main` reached the same defect independently and better in 0054 |
| 0085 | [The log line said seventy-six](0085-the-log-line-said-seventy-six.md) | fix · superseded | The result dict was already honest; the line a person reads during a run was not |
| 0086 | [The same collision, and the same bug](0086-the-same-collision-and-the-same-bug.md) | chore | Two sessions renumbered from one stale index again, and independently fixed one counter |
| 0087 | [A map of what the archive knows](0087-a-map-of-what-the-archive-knows.md) | docs | The wiki is organised by entity and states no order; this is the order, and what the archive does not hold |
| 0088 | [The cap bounds a run, not a decision](0088-the-cap-bounds-a-run-not-a-decision.md) | fix | A hand-filed PDF was archived, its document written, and no task filed — one WARNING among two dozen |
