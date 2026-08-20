# Requests

Ask this archive for a change by leaving a markdown file here, in `pending/`.

```markdown
---
kind: paper | correction | topic | question | other
from: your name or address
subject: one line
---

What you are asking for, and why.
```

**Nothing here happens on its own.** A person reads every file and decides;
there is no category that is approved automatically, however harmless it looks.
Until somebody approves it, a request is a file in a folder and nothing else.

The archive's own side of this is `python3 -m pipelines.requests`.

## Why this is not the port

`python3 -m pipelines.serve` answers questions on `127.0.0.1` and refuses every
write. Reading and changing are different acts with different risks, so they are
different channels: one you can hit a thousand times a second and change
nothing, one that goes through a person.

## What happens to your file

| | |
| --- | --- |
| `pending/` | Waiting to be read. Yours to write, nobody else's. |
| `approved/` | Somebody said yes. The next maintenance session acts on it. |
| `rejected/` | Somebody said no, and the file records why. Declined is not deleted. |
| `done/` | Acted on. |

A malformed request is **listed with its problem** rather than ignored — a
submitter who is silently dropped cannot tell that from one not yet read. It
cannot be approved until the problem is fixed.
