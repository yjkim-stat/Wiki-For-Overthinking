# Inbox

Drop a PDF here. The next run ingests it.

```bash
cp ~/Downloads/some-paper.pdf inbox/
python3 -m pipelines.run_daily --source local
```

What happens to it:

1. The file is hashed and moved to `data/pdfs/<id>.pdf`. The inbox drains, so
   nothing is ingested twice, and identity is the file's *content* — dropping
   the same paper twice under two names produces one record.
2. A reading task is filed in `data/queue/pending/`.
3. Whoever drains the queue opens the PDF, reads it — figures and tables
   included — and returns the summary **and** the bibliography, because the
   collector never opens the file and knows nothing but the filename.
4. `python3 -m pipelines.render` folds that into the archive, the wiki and the
   topic outputs, exactly as for a paper that arrived from arXiv.

Two things worth knowing:

- **A PDF filed here is never rejected by keyword scoring.** Putting it in the
  inbox is the editorial decision that scoring exists to approximate. Which
  tracked topics it belongs to is decided by the reader, not by its keywords.
- **PDFs are not tracked by git** — neither here nor in `data/pdfs/`. They are
  heavy, usually redistributable only to you, and always reproducible from
  wherever you got them. The *record* is committed; the bytes are yours.

`python3 -m pipelines.run_daily --dry-run` reports what would be ingested and
leaves the folder untouched.
