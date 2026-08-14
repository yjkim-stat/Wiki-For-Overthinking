"""Finding what the archive already says about something.

A pure read. Nothing here writes, fetches, or calls a model: it walks the
records the pipeline has already produced and reports which of them mention the
terms asked about, ranked. What comes back is what the archive wrote, verbatim
— a definition somebody wrote, a finding the group settled, a reading of a paper
— and never a sentence composed here.

That restraint is the whole design. This repository's pipeline never calls a
model, so a component that *answered* a question would have to either invent
prose or reach outside the process, and both are excluded by the contract the
rest of the code is built on. What a reader gets instead is the material and its
provenance, which is the thing they would have gone looking for anyway.

**Order matters more than the count.** A finding outranks a definition, which
outranks a reading, because that is the archive's own ordering of authority: the
group's settled position first, then what somebody wrote about a term over all
its sources, then what one paper said. A search that returned twelve papers
before the one sentence the group had already agreed on would be answering a
different question.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Iterable

from .config import Config
from .store import RecordStore
from .text import contains

# Kinds, in the order a reader should meet them. The number is a tie-breaker
# between kinds and nothing else — within a kind, matches rank by how many of
# the query's terms they carry.
_AUTHORITY = {"finding": 3.0, "concept": 2.0, "summary": 1.0, "paper": 0.5}

_STOPWORDS = frozenset(
    """
    a an and are as at be but by do does for from has have how in into is it its
    of on or that the their there these this to was were what when where which
    who why will with
    """.split()
)


@dataclass
class Hit:
    """One thing the archive says, and where it says it."""

    kind: str  # finding | concept | summary | paper
    id: str
    title: str
    body: str
    score: float = 0.0
    matched: list[str] = field(default_factory=list)
    # Where a reader can go and look: a wiki note, an archive page, a record.
    source: str = ""

    def to_dict(self) -> dict:
        return {
            "kind": self.kind,
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "score": round(self.score, 3),
            "matched": self.matched,
            "source": self.source,
        }


def terms(query: str) -> list[str]:
    """The phrases a query is asking about.

    A quoted run is one term, so `"world model"` is not two words that happen to
    co-occur. Everything else splits on whitespace, and the small words go —
    matching "the" against an archive returns the archive.
    """
    found: list[str] = []
    for quoted in re.findall(r'"([^"]+)"', query):
        cleaned = quoted.strip()
        if cleaned:
            found.append(cleaned)
    rest = re.sub(r'"[^"]*"', " ", query)
    for word in re.split(r"[^\w\-]+", rest):
        word = word.strip("-")
        if len(word) > 1 and word.lower() not in _STOPWORDS:
            found.append(word)
    # Dedupe, keeping order: a repeated term should not count twice.
    seen: set[str] = set()
    return [t for t in found if not (t.lower() in seen or seen.add(t.lower()))]


def _hit(kind: str, wanted: list[str], fields: Iterable[tuple[str, float]]) -> tuple[float, list[str]]:
    """Score one record: which terms it carries, weighted by where.

    Presence, not frequency. A paper that says "world model" nine times is not
    nine times the answer, and counting would rank a long document above a
    definition written precisely about the term.
    """
    matched: list[str] = []
    score = 0.0
    for term in wanted:
        best = 0.0
        for text, weight in fields:
            if contains(term, text):
                best = max(best, weight)
        if best:
            matched.append(term)
            score += best
    return score * _AUTHORITY.get(kind, 1.0), matched


def search(cfg: Config, query: str, limit: int = 20) -> dict:
    """Everything the archive says about ``query``, best first.

    Returns the hits with the terms that were searched for, so a caller can say
    what was asked as well as what came back — a search that found nothing is
    only useful if you can see what it looked for.
    """
    wanted = terms(query)
    if not wanted:
        return {"query": query, "terms": [], "hits": [], "total": 0}

    store = RecordStore(cfg.layout)
    hits: list[Hit] = []

    for finding in store.iter_findings():
        if not finding.live:
            continue
        score, matched = _hit(
            "finding",
            wanted,
            ((finding.statement, 1.0), (finding.rationale, 0.6),
             (" ".join(finding.concepts), 0.8)),
        )
        if score:
            hits.append(Hit("finding", finding.id, finding.statement,
                            finding.rationale, score, matched, "wiki/findings.md"))

    for concept in store.iter_concepts():
        if not concept.definition:
            continue
        score, matched = _hit(
            "concept",
            wanted,
            ((concept.name, 1.0), (" ".join(concept.aliases), 0.9),
             (concept.definition, 0.7)),
        )
        if score:
            hits.append(Hit("concept", concept.slug, concept.name,
                            concept.definition, score, matched,
                            f"wiki/{concept.kind}s/{concept.slug}.md"))

    for paper in store.iter_papers():
        summary = store.load_paper_summary(paper.id)
        if summary is not None:
            score, matched = _hit(
                "summary",
                wanted,
                ((paper.title, 1.0), (summary.one_liner, 0.9),
                 (summary.problem, 0.6), (summary.method, 0.6),
                 (summary.results, 0.6)),
            )
            if score:
                hits.append(Hit("summary", paper.id, paper.title,
                                summary.one_liner, score, matched, paper.url))
            continue
        # No reading yet: the archive holds the paper and has not read it, which
        # is worth saying rather than hiding. Ranked below everything read.
        score, matched = _hit(
            "paper", wanted, ((paper.title, 1.0), (paper.abstract, 0.4))
        )
        if score:
            hits.append(Hit("paper", paper.id, paper.title, "", score, matched,
                            paper.url))

    hits.sort(key=lambda h: (-h.score, h.kind, h.id))
    return {
        "query": query,
        "terms": wanted,
        "total": len(hits),
        "hits": [h.to_dict() for h in hits[:limit]],
    }
