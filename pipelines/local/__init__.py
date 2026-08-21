"""Narrow extensions, each with a single call site.

Everything else under `pipelines/` is written to be general, and a general
module gets improved by being replaced outright. What lives here is the work
that is *not* general — a judgement about what this kind of archive should do —
kept in a package of its own so that replacing a general file leaves it alone
and only the one-line call site has to be re-checked.

A deployment that carries this repository as a template and takes updates from
it should keep its own additions here for the same reason, and should record any
change it cannot fit here — a schema change, or a fix inside a general-purpose
function — somewhere it will be read before a file is replaced wholesale. A
change nobody registered is a change that gets reverted silently.

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
