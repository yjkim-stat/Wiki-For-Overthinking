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
