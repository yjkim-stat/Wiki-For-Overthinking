# Deployment

Keeping an archive in a repository of its own, so that pulling a new version of
the code can never collide with a month of readings. Authority is
[`CLAUDE.md` § First: which tree is the archive in?](../../CLAUDE.md#first-which-tree-is-the-archive-in);
this is the procedure. The harness is in [`harness.md`](harness.md).

## Why the tree splits

Run in place, one repository holds two things with opposite lifetimes: code that
gets replaced, and an archive that accumulates. Git makes you merge them anyway,
and the collisions land in the files least able to survive one:

| What collides | Why |
| --- | --- |
| `data/index/seen.sqlite` | Binary. Unmergeable. Resolving it by taking a side discards deduplication state, and the next run re-collects everything. |
| `wiki/graph.html`, `wiki/_meta/graph.json` | Regenerated every render. Both sides always differ. |
| `data/index/*.jsonl`, `archive/index.md`, `wiki/index.md` | The code ships these empty; every run rewrites them. |
| `config/settings.yaml`, `config/sources.yaml` | The deployment must edit them — categories, venues, channels — and the code goes on evolving them. |
| `docs/commit/NNNN` | Numbered against `origin/main`. A deployment writing notes advances a sequence the code repository is also advancing. |

Split the roots and every row disappears. Nothing is shared to conflict over.

## Setting one up

**1. Make the archive's repository.** It holds config and what the pipeline
writes — nothing else.

```bash
mkdir ~/research-archive && cd ~/research-archive && git init
mkdir -p config/topics
cp ~/research-framework/config/settings.yaml ~/research-framework/config/sources.yaml config/
cp ~/research-framework/.gitignore .gitignore          # keeps PDFs, logs and raw responses out
```

`templates/` is deliberately **not** copied. A template is resolved per file
against the deployment first and the code second, so an archive with no
`templates/` directory renders with the shipped ones and keeps receiving
improvements. Copy a single file into `templates/<kind>/<name>` only when you
want to change that one.

**2. Name the topics.** The one editorial act nothing can do for you.

```bash
cd ~/research-framework && scripts/new_topic.sh "Causal Inference"    # writes into this checkout
mv config/topics/causal-inference.yaml ~/research-archive/config/topics/
$EDITOR ~/research-archive/config/topics/causal-inference.yaml
```

Then edit `config/sources.yaml` in the archive: the arXiv categories and venue
list shipped as defaults are a starting point, and collecting from the wrong
indexes is the most common reason a topic stays empty.

**3. Point the code at it and check before running anything.**

```bash
cd ~/research-framework
export RA_WM_ROOT=~/research-archive
python3 -m pipelines.migrate status
```

```
roots
  deployment /home/you/research-archive
  code       /home/you/research-framework
```

Two different paths is the whole point of the step. One path means the variable
did not take, and everything below would write into the code checkout.

**4. Record which version of the code built it.**

```bash
git -C ~/research-framework rev-parse HEAD > ~/research-archive/FRAMEWORK.txt
```

The archive is the only thing that knows this. Nothing in git relates the two
repositories, so a record that reads oddly a year from now has no way back to
the code that wrote it unless this file exists.

**5. Run.**

```bash
scripts/daily.sh                 # or: python3 -m pipelines.run_daily && python3 -m pipelines.render
cd ~/research-archive && git add -A && git commit -m "archive: initial"
```

From here the ordinary routine applies unchanged —
[knowledge-and-wiki](../knowledge-and-wiki/). Commits go to the archive.

## Updating the code underneath a running archive

```bash
cd ~/research-framework
git fetch origin main
git log --oneline HEAD..origin/main         # what is about to change
git merge --ff-only origin/main
python3 -m unittest discover -s tests -t .
```

Then, against the archive rather than in place:

```bash
export RA_WM_ROOT=~/research-archive
python3 -m pipelines.migrate status         # roots still right? records still there?
python3 -m pipelines.render                 # derived is rebuilt by the new code
cd ~/research-archive && git status --short
```

**Read that last diff before committing it.** It is the whole visible effect of
the new version on your archive, and it is the only place a regression in a
renderer shows up. A render over an unchanged archive must not change a record
under `data/` — if it does, the version you just pulled has a bug, and the
archive is the evidence.

```bash
git -C ~/research-framework rev-parse HEAD > FRAMEWORK.txt
git add -A && git commit -m "archive: render under <short-sha>"
```

Record the new version in the same commit as the diff it produced. That way the
archive's history answers "what changed, and under which code" in one place.

## What the split does not give you

- **No pinning.** Nothing stops a `git pull` in the code checkout from moving
  under an archive mid-session. `FRAMEWORK.txt` records what ran; it does not
  enforce it. Use a submodule if you need the version fixed by git rather than
  by discipline.
- **No second opinion on config.** `config/` moved to the deployment, so an
  improvement the code makes to `settings.yaml` or `sources.yaml` never reaches
  an existing archive. Read the release's commit notes for config changes; there
  is no merge to remind you.
- **Nothing shared but templates.** Deployments do not see each other. Two
  archives on the same checkout are independent, which is the point, and also
  means a fix to one topic file helps only that one.
