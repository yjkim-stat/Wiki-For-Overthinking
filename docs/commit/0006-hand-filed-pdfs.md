# 0006 — Hand-filed PDFs

| | |
| --- | --- |
| **Commit** | `feat(collect): ingest PDFs filed by hand into inbox/` |
| **Scope** | `pipelines/collect/local_pdf.py`, `pipelines/common/`, `pipelines/enrich/queue.py`, `pipelines/render.py`, `pipelines/run_daily.py`, `config/sources.yaml`, `inbox/`, `.gitignore`, docs, tests |
| **Kind** | feature |

## What changed

Not everything a group reads is on arXiv. A PDF dropped into `inbox/` is now
ingested on the next run and ends up in the archive, the wiki and the topic
outputs like any other paper.

```bash
cp ~/Downloads/some-paper.pdf inbox/
python3 -m pipelines.run_daily --source local
```

The collector hashes the file, moves it to `data/pdfs/<id>.pdf`, and files a
reading task carrying the file's path. Whoever drains the queue opens the
document and returns the summary *plus* a `bibliography` and a `topics` list.
Render folds all three into the record.

New pieces: `collect/local_pdf.py`; `Paper.local_path` and `Paper.is_local`;
`PDF_EXTRA_SCHEMA` and `local_pdf_instructions()` in `common/llm.py`;
`Layout.inbox` and `Layout.pdfs`; validation for the two new result fields; and
`_apply_bibliography()` in `render.py`.

## Why it is built this way

**A collector, not a side door.** The repository's rule is that everything in
the archive arrived from a collector, and hand-editing a record is forbidden
because the next render overwrites it — a hand-written wiki note about a PDF
would survive only in the manual tail, which is not where a paper belongs. So
the inbox is a source like any other, and everything downstream of collection is
untouched by this feature.

**Nothing in the pipeline opens the PDF.** Extracting a title, an abstract or a
year from a PDF in pure Python means shipping a parser that is wrong often
enough to poison the archive quietly, and wrong in a way nobody audits. The
repository already has a reader that is good at documents — the session that
drains the queue — and a seam designed for exactly this handoff. So the
collector records only what the filesystem can tell it, and the task asks for
the rest. This also keeps the one-dependency floor intact.

**Identity is the file's content.** A filename is whatever somebody typed while
saving. Hashing the bytes means the same paper filed twice under two names is
one record, and renaming a file before dropping it changes nothing.

**The inbox drains.** The file is *moved*, not copied. A collector that leaves
its input in place re-ingests it on every run, and a folder that only grows
stops being an inbox. The consequence is that `--dry-run` had to learn to leave
the folder alone — this is the only collector for which a dry run means more
than "do not store", because it is the only one that touches something a person
still expects to find where they put it.

**A hand-filed PDF is never rejected by scoring.** Putting it in the inbox *is*
the editorial decision that keyword scoring exists to approximate. Scoring still
runs, because the topics it happens to match are worth recording, but rejection
is skipped and the reader assigns the topics afterwards. This is the same
principle as "topics are the group's editorial decision", applied one level
down.

**Whether a reading may overwrite metadata depends on what else knows the
paper.** While the inbox is the record's only source, everything it holds is a
guess from a filename — including the title — so the reading replaces it
outright. Once the same work has also arrived from an index, that metadata is
better evidence than a reading, and the reading may only fill blanks. One rule,
stated in `_apply_bibliography`, covering both directions.

**PDFs are not tracked, records are.** They are heavy, rarely ours to
redistribute, and always obtainable again from wherever they came from. A fresh
clone gets the whole archive — summaries, wiki, outputs — without the bytes.
This is the same reasoning that already ignores `data/raw/`.

## Trade-offs and rejected alternatives

- *Parsing the PDF in Python (`pypdf`, `pdfminer`).* Rejected: a second
  dependency, and a class of silent extraction errors that would land in the
  archive as facts. The reading step is better at this and already exists.
- *Copying instead of moving.* Rejected — see above. The cost is that a person
  who drops a file and then looks for it will not find it; the inbox README and
  `--dry-run` are the mitigation.
- *Requiring a topic match before accepting a dropped PDF.* Rejected: it would
  make the system argue with the person who filed it.
- *A separate task kind (`pdf`).* Rejected: it is a paper. Reusing `kind:
  "paper"` means the appliers, the archive page, the wiki harvest and the
  outputs need no change at all — only the prompt, two optional result fields
  and an attachment differ.
- *Letting `topics` in a result apply to any paper.* Rejected: for a collected
  paper the scorer already answered that question, and a reading that could
  overrule it would make topic assignment unauditable. The field is honoured
  only for a local record, and unknown slugs are logged and dropped rather than
  silently vanishing from every output.

## What a reviewer should check

- `run_daily.run()` — that `--dry-run` reaches `local_pdf.collect(dry_run=True)`
  before anything moves. The regression this guards is somebody's file
  disappearing from a command documented as writing nothing.
- `_apply_bibliography()` — the `guessed = paper.source == "local"` rule. If
  that comparison ever becomes `paper.is_local`, a merged record would let a
  misreading overwrite arXiv's metadata.
- `local_pdf._ingest()` — `shutil.move` onto an existing target. It is only safe
  because the target name is the content hash, so the bytes are identical by
  construction.
- Run `python3 -m unittest discover -s tests -t .` — 149 tests, of which
  `tests/test_local_pdf.py` covers ingestion, identity, the dry run, the
  overwrite rule and topic assignment.

## Also fixed here

`Paper.citation()` no longer falls back to "arXiv" as the venue for a paper that
never came from arXiv. Harmless until now, because everything in the archive did
come from an index; a hand-filed PDF with no venue would have been cited as an
arXiv paper it has nothing to do with.

This feature is also what made [0005](0005-rebuild-archive-from-scratch.md)
worth fixing first: a hand-filed PDF has no year until it has been read, so a
page written under `unknown/` and corrected afterwards went from a rare
deduplication edge case to the normal path.

## Downstream impact

New folders appear on the next run: `inbox/` (tracked, holds only its README)
and `data/pdfs/` (ignored). Existing records are untouched — `local_path` is an
additive field and old records load with it empty.

Disable the whole thing with `local.enabled: false` in `config/sources.yaml`; the
folder is then never looked at. Deployments that keep their PDFs elsewhere can
point `paths.inbox` in `config/settings.yaml` at that directory instead.
