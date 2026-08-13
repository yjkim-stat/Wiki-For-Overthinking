# 0049 — A citation rather than a rumour

| | |
| --- | --- |
| **Commit** | `feat(enrich): record what was checked outside the archive` |
| **Scope** | `pipelines/common/schema.py`, `pipelines/common/paths.py`, `pipelines/common/store.py`, `pipelines/enrich/references.py`, `pipelines/enrich/findings.py`, `tests/test_references.py`, `CLAUDE.md`, `README.md`, `migration/README.md` |
| **Kind** | feature |

## What changed

A new record type in `data/references/`, and `Finding.references[]` to cite it.

```bash
python3 -m pipelines.enrich.references add --file reference.json
python3 -m pipelines.enrich.references list | show <id> | stats
```

The archive answers questions about itself and nothing about what is not in it,
so sessions go and look things up — a published implementation, a model card, a
venue's own listing. What they learned survived only inside a finding's prose,
where `Finding.papers` could not hold a URL and the next person had to repeat the
search to confirm a sentence. This is requirement R3 of the dream-mode
specification.

## Why it is built this way

**A separate record type, not a `Paper` with `source: "web"`.** The
specification's option A2 is much less code and its cost arrives later and
unattributably: every paper count, every archive page, every topic rollup would
include things nobody collected, and by the time a number looks wrong there is
no way to say which numbers were affected. `data/references/` is a sibling of
`data/findings/` because neither arrived from a collector — that is the property
they share, and it is the one that matters.

**`retrieved_at` and `quoted` are both required, and that friction is the
feature.** The web changes; an undated claim about a page cannot be checked
against anything. And a URL records that a page was visited, not what it was
found to say — when the page moves, the quotation is the only surviving
evidence. A record with either missing looks like a citation and is not one, so
the validator refuses it rather than storing something that will be trusted.

**URL normalisation is deliberately timid.** The two failure directions are not
symmetric. Under-normalising leaves two records for one page: visible, and fixed
by citing the other. Over-normalising fuses two pages into one record, and the
citation then points at something the reader never read — the same shape as a
wrong alias, which this repository already treats as the expensive kind precisely
because the fused record looks healthy. So case folds on the scheme and host, a
default port and a fragment go, one trailing slash goes, and **the query string
is left exactly alone**, because on a great many sites it is what selects the
page.

**Content-addressed, like a finding.** The same page cited twice is one record. A
second visit updates the quotation and the date — that is what `retrieved_at` is
for — while `first_seen` is kept, because when this archive first consulted a
page is a fact about the archive rather than about the page.

### The line this record must never cross

> **An external reference never contributes to entity promotion.**

`Concept.evidence` counts papers and talks the archive has read, and that count
promotes an entity to a note of its own. If a blog post could raise it, nothing
afterwards could say what the wiki had grown from — and unlike a bad link or a
wrong definition, deleting the post would not undo it, because the notes it
promoted are already there and look like all the others.

Three things hold the line, and the third is the one that will still hold in a
year:

1. The records live outside `data/papers/`, so nothing that walks papers sees
   them.
2. `PromotionIsSealedOffTests` renders an archive, adds a reference and a finding
   citing it, renders again, and asserts the mention count and the set of notes
   are unchanged — and that an entity named only by a finding gets no note however
   many references back it.
3. A static test asserts that `pipelines/enrich/concepts.py` does not contain the
   string `reference` at all. The behavioural tests prove today's code is clean;
   this one is what fails when somebody adds a plausible line to the harvest on a
   path no fixture reaches.

## Trade-offs and rejected alternatives

**Option A3 — a URL string inside the finding — was rejected** as the cheapest
and least useful: no deduplication, no validation, no date, and no way to ask
what this archive has been checking itself against.

**Snapshots are not taken.** The specification's B2 (quotation required) is
implemented and B3 (a local copy under `data/snapshots/`) is not. `Reference` has
a `snapshot` field so a deployment that starts taking them has somewhere to say
so without a schema change, and nothing writes it today. The honest consequence:
a finding can cite a page that has since vanished, and the quotation is all that
is left.

**Nothing renders a reference yet.** `wiki/findings.md` and the concept notes
draw findings without their citations. That is the next commit rather than this
one — and when it comes, references belong under a heading of their own
(`## Checked against`) rather than mixed into `## Appears in`, for the same
reason they are a separate record.

**`kind` is a closed set** — `code`, `model-card`, `docs`, `blog`,
`proceedings-page`, `dataset`, `other`. A free string would make "what has this
archive been checking itself against" unanswerable, which is half of why the
record exists.

## What a reviewer should check

- The seal, by mutation: add any mention of `reference` to
  `pipelines/enrich/concepts.py` and the static test fails; that is the only
  guard that survives a change nobody writes a fixture for.
- That the two required fields are separately enforced. An earlier version of
  these tests asserted only that the error mentioned `retrieved_at`, and passed
  with the requirement removed — the malformed-value branch caught the empty
  string and reported it as a different problem. Each branch is now pinned by its
  own message.
- Normalisation, in `IdentityTests`: five spellings of one page collapse, and a
  differing query string does not. Dropping the query from `normalize_url` fuses
  two pages and fails exactly one test.
- That `Finding` still loads without the new field
  (`test_an_older_finding_without_the_field_still_loads`).

## Downstream impact

**Adding both fields is safe** — `from_dict` defaults them, so existing findings
load with `references: []` and nothing regenerates differently.

`data/references/` is a new directory under `data/`, created by
`Layout.ensure()`, **committed like every other record** and carried by git in a
migration. It is not in `.gitignore` and should not be: a reference is knowledge,
and it is small.
