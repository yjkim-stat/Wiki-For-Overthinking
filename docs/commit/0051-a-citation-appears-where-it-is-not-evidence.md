# 0051 — A citation appears, where it is not evidence

| | |
| --- | --- |
| **Commit** | `feat(publish): draw a finding's citations, apart from its sources` |
| **Scope** | `pipelines/publish/wiki.py`, `tests/test_references.py` |
| **Kind** | feature |

## What changed

[Note 0049](0049-a-citation-rather-than-a-rumour.md) added reference records and
`Finding.references[]`, and nothing drew them. A concept note now carries a
`## Checked against` section listing the pages cited by the findings that bear
on it, with the passage each was relied on for, and `wiki/findings.md` names a
finding's citations on a line of their own.

## Why it is built this way

**A heading of its own, below `## Appears in`.** The evidence list is what the
archive read: papers and talks whose summaries put this name in a list, which is
also what promotes the entity to a note at all. A reference did none of that. Put
in the same list it would make the note claim a source it does not have — and the
count underneath would go on disagreeing with the list above it, which is a
worse failure than an absent citation because both halves look right on their
own.

The order says the same thing: the literature first, then what was checked
against it. `## What we have settled` stays above both, because a position the
group reached outranks the evidence for it when a reader is deciding what a note
says.

**The quotation is carried into the note, not left in the record.** A reader
deciding whether to trust a settled position should not have to open a JSON file
to see what a page was found to say. And when the page moves — which is the
whole reason `retrieved_at` exists — the words in the note are the only place
they still are.

**Deduplicated across findings.** Two findings that consulted one page must not
make a note read as though two things were checked. The reference list is a
property of the entity, not a per-finding footnote, so it collapses.

**`Checked against:` on the findings page is a separate line from `From:`.**
Same reasoning one level down: `From:` lists papers the archive holds and can
re-read, and a page somebody looked at once does not belong in that sentence.

## Trade-offs and rejected alternatives

**Notes get longer**, by two lines per cited page. That is the cost of carrying
the quotation, and it is the part that makes a citation checkable rather than
decorative. A note with many citations and few sources would read oddly, and if
that happens it is worth knowing.

**Considered: a citation marker inline in the settled statement**, footnote
style. Rejected as more machinery than the content justifies at seven findings,
and it would put a URL in the middle of the sentence a reader is there to read.

**References are listed alphabetically by title.** Retrieval order would be more
informative — what was checked most recently — and is not stable across
re-records, which would make the section churn under `render` for no change in
`data/`.

**A finding citing a reference that has been deleted is skipped silently.** The
validator refuses such a finding at submission, so this only arises if somebody
removes a record from `data/` by hand, and a renderer is the wrong place to
complain about that.

## What a reviewer should check

- `test_the_citation_is_not_in_the_evidence_list` splits the note on its two
  headings and asserts the URL is in the second and not the first. Moving the
  lines into `## Appears in` fails it and one other.
- That the quotation survives: dropping the sub-bullet fails
  `test_the_note_carries_the_citation_and_its_quotation`. It is the field that
  makes the record worth having.
- `test_one_page_cited_twice_is_listed_once`, against removing the `seen` guard.
- On the findings page, that `Checked against:` is not folded into `From:`.
- That a note with no citations gains no empty heading.

## Downstream impact

Concept notes and `wiki/findings.md` are regenerated with the new sections. Both
are inside the auto block, so anything written after `<!-- auto:end -->` is
untouched, and an archive with no references renders exactly as before.
