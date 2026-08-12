"""Local extensions — this archive's own work, kept apart from the general code.

Everything under `pipelines/` except this package is written as a general
template for running a literature archive, and a general template gets improved
by replacing a file wholesale. Keeping our additions in a package of their own is
what makes that cheap: the file is replaced and only its one-line call site here
has to be re-checked.

Anything of ours that *cannot* live here — because it is a schema change, or a
fix inside a general-purpose function — is listed in `docs/LOCAL-DELTAS.md` with
the reason, and marked `# LOCAL` at the site. Read that file before replacing
anything under `pipelines/`: a delta that is not in the register is one that gets
removed silently, which has happened.

What is here:

* `placeholders` — rejects a wiki entity that names a set instead of a thing.
* `abstracts`    — fetches an abstract for a record whose index carried none.
* `queue_share`  — stops a reading backlog from starving the wiki's own queue.

What is *not* here, and cannot be: the `model` wiki kind. A fourth entity kind
is a schema change, and a schema change is cross-cutting by construction — it
touches the record, the harvest, the validator, the applier and the directory
layout at once. There is no seam to hide it behind, so it stays in the template
files as a marked delta.
"""
