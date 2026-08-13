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
| 0049 | [A model is not a dataset](0049-a-model-is-not-a-dataset.md) | feature · breaking | A checkpoint and a corpus answer different questions; a schema change has no seam to hide behind |
| 0050 | [Local extensions in a package of their own](0050-local-extensions-in-a-package-of-their-own.md) | feature | A placeholder is a false entity, a record with no abstract cannot be scored, and one cap starved the wiki |
| 0051 | [Three fixes that only made collection quieter](0051-three-fixes-that-only-made-collection-quieter.md) | fix | Under-collecting looks exactly like a quiet day, and a test inside a replaceable file cannot guard it |
| 0052 | [The archive this repository keeps](0052-the-archive-this-repository-keeps.md) | feature · breaking | Both roots are one tree here; `data/` is committed because a scheduled run starts from a fresh clone |
| 0053 | [Everything the archive needs is in the repository](0053-everything-the-archive-needs-is-in-the-repository.md) | docs | Knowledge that lives only outside the repository is knowledge the next session does not have |
| 0054 | [A kind that is accepted is offered](0054-a-kind-that-is-accepted-is-offered.md) | fix | The validator took four kinds and the reader was shown three, and a stored definition freezes the kind |
| 0055 | [A field with no validator is a field that goes missing](0055-a-field-with-no-validator-is-a-field-that-goes-missing.md) | fix | `models` was accepted, applied and never checked, so nine readings lost it without a word |
| 0056 | [Taking the update, and giving up our numbers](0056-taking-the-update-and-giving-up-our-numbers.md) | chore | Two sessions numbered from the same stale index; the one that had not pushed is the one that moves |
