"""Summarizer interface.

The pipeline never calls a model directly. It asks a ``Summarizer`` for a
structured reading of a paper or a video, and a backend decides how that gets
produced.

The default backend, ``queue``, produces nothing itself: it writes a task file
describing exactly what is needed and returns ``None``. The daily Claude Code
session drains that queue, and ``pipelines/render.py`` picks the results up.
That is what makes the system work with no API key while leaving a single,
narrow seam where a direct API backend can be dropped in later.

The prompt text and the output schema live here rather than in a backend, so
every backend is held to the same contract and summaries stay comparable no
matter what produced them.
"""

from __future__ import annotations

from typing import Any, Callable, Protocol

from .paths import WIKI_KINDS  # the `model` kind
from .schema import Paper, PaperSummary, Video, VideoSummary


class SummarizerNotConfigured(RuntimeError):
    """A backend was selected but has no working implementation yet."""


# ---------------------------------------------------------------------------
# The contract every backend fulfils
# ---------------------------------------------------------------------------

PAPER_OUTPUT_SCHEMA: dict[str, Any] = {
    "one_liner": "string - what the paper does, in one sentence, no hype",
    "problem": "string - the problem it addresses and why it is open",
    "contributions": ["string - one concrete claimed contribution"],
    "method": "string - how it works, enough for a reader to explain it",
    "results": "string - headline numbers, on which benchmarks, against what",
    "limitations": "string - stated limits plus any the reader should notice",
    "relevance": {
        "<topic-slug>": "string - why this matters for that specific topic"
    },
    "concepts": ["string - reusable ideas this paper relies on or introduces"],
    "methods": ["string - named methods, architectures or algorithms"],
    # `models` — a checkpoint is not a corpus.
    "datasets": [
        "string - datasets, benchmarks, corpora or simulators used. Not models:"
        " a checkpoint that was evaluated or fine-tuned belongs in `models`."
    ],
    "models": [
        "string - models the work trains, evaluates or analyses, as named in"
        " the paper (e.g. a base checkpoint, a released reasoning model, a judge)"
    ],
    "tags": ["string - short lowercase keywords"],
}

VIDEO_OUTPUT_SCHEMA: dict[str, Any] = {
    "one_liner": "string - what the talk is about, in one sentence",
    "abstract": "string - a paragraph covering the argument of the talk",
    "chapters": [
        {
            "start_s": "integer - required, start time in seconds",
            "title": "string - short chapter title",
            "summary": "string - what is covered in this stretch",
        }
    ],
    "key_points": ["string - a claim or takeaway worth remembering"],
    "referenced_papers": ["string - paper titles or arXiv ids mentioned"],
    "concepts": ["string"],
    "methods": ["string"],
    "datasets": ["string"],
    "models": ["string"],  # LOCAL
    "tags": ["string - short lowercase keywords"],
}

# Added to a paper task only when a document is attached to it. Where none is,
# there is nothing to ask — the abstract was the only thing there was to read,
# and the applier records that without troubling the reader for it.
READ_FROM_SCHEMA: dict[str, Any] = {
    "read_from": (
        "string - required: 'document' if you opened the attached PDF and read "
        "it, 'abstract' if you worked from the payload alone. Answer for what "
        "you did, not for what you were asked to do"
    ),
}

# A hand-filed PDF arrives with no metadata at all — the collector only knows a
# filename and a hash. Whoever reads the document supplies the bibliography and
# says which tracked topics it belongs to, so these fields extend, rather than
# replace, the ordinary paper contract.
PDF_EXTRA_SCHEMA: dict[str, Any] = {
    "bibliography": {
        "title": "string - the paper's own title, exactly as printed",
        "authors": ["string - author name, in the order printed"],
        "year": "integer - publication year, 0 if the document does not say",
        "venue": "string - journal, conference or 'preprint'; empty if unclear",
        "doi": "string - DOI if printed on the document, else empty",
        "arxiv_id": "string - arXiv id if printed on the document, else empty",
        "abstract": "string - the paper's own abstract, verbatim",
    },
    "topics": [
        "string - slug of a tracked topic this paper belongs to; omit any that "
        "do not genuinely apply"
    ],
}

def _paper_schema(*, local: bool, has_document: bool) -> dict[str, Any]:
    """The output contract for one paper task.

    Three fragments, each earned by something about the task rather than by the
    kind: the ordinary paper contract, the bibliography a hand-filed PDF has
    nobody else to get its metadata from, and the reading basis a task can only
    ask about when it handed over a document to begin with.
    """
    schema = dict(PAPER_OUTPUT_SCHEMA)
    if local:
        schema.update(PDF_EXTRA_SCHEMA)
    if has_document:
        schema.update(READ_FROM_SCHEMA)
    return schema


CONCEPT_OUTPUT_SCHEMA: dict[str, Any] = {
    "definition": (
        "string - two to four sentences defining the entity as the cited "
        "sources use it, not as a textbook would"
    ),
    # enumerated from WIKI_KINDS rather than written out, so a fifth
    # kind cannot reach the validator without reaching the reader. Spelling
    # this list by hand is how `model` came to be accepted but never offered.
    "kind": f"string - one of: {', '.join(WIKI_KINDS)}",
    "aliases": ["string - other names the sources use for the same thing"],
    "related": [
        "string - name of a neighbouring entity worth linking to. Kept as you "
        "give it and never derived away, so name what a reader should turn to "
        "next rather than what happens to appear alongside this. Answering "
        "again replaces the whole list; an empty list retracts"
    ],
}

_SHARED_RULES = """
Rules:
- Write in {language}.
- Ground every statement in the supplied material. If something is not stated,
  leave the field empty rather than inferring it.
- No marketing language. Prefer the specific number over the adjective.
- Return one JSON object matching the schema exactly. No prose around it.
""".strip()


# `models`
_MODELS_RULE = (
    "Answer `models` explicitly, even when the answer is `[]`. List the "
    "checkpoints the work trains, evaluates or analyses, named as the paper "
    "names them — a base model, a released model, a judge. A paper that "
    "evaluates none returns an empty list, and that is a real answer: the "
    "archive holds several. Leaving it out looks identical to that in the "
    "record, and nothing afterwards can tell the two apart."
)


_READ_FROM_RULE = (
    "Then set `read_from`: 'document' if you opened the file, 'abstract' if you "
    "did not and worked from the payload. Say which you actually did. A reading "
    "that is honest about being abstract-only can be redone later; one that "
    "claims a document it never opened cannot be found at all."
)


def _contested_warning(paper_id: str, other: str) -> str:
    """Said on the task, because that is where somebody is about to act.

    Two records claiming one identifier is reported by every render, to whoever
    ran it. The person who then drains the queue is often not that person and is
    always looking somewhere else — and reading this paper can be exactly the
    wrong move, because the archive would gain a second summary of one paper and
    count it twice in every entity that cites it.

    A warning rather than a refusal, because the reading is not always wrong. If
    neither record has been read, reading either is fine: a merge carries the
    summary to whichever record survives. It is wrong only when the other record
    has one already, and the reader can check that from here.
    """
    if not other:
        return ""
    return (
        "\n\n---\n\n"
        f"**Stop and check before reading this.** `{paper_id}` and `{other}` "
        "claim the same identifier: they are probably one paper held as two "
        "records.\n\n"
        f"If `{other}` has already been read, **do not read this one** — the "
        "archive would gain a second summary of one paper and count it twice in "
        "every entity that cites it. Leave the task and say so.\n\n"
        "Either way somebody has to decide which record survives:\n\n"
        "    python3 -m pipelines.enrich.dedupe merge <survivor> <absorbed> --dry-run\n"
    )


def paper_instructions(
    topics: list[dict], language: str = "en", *, has_pdf: bool = False
) -> str:
    """Prompt for reading a paper through the lens of the matched topics.

    When the document itself was fetched, the prompt says so and points at the
    experiments rather than the abstract. An abstract is a claim about a paper:
    it reports the headline and rarely the conditions under which the headline
    fails, and often carries no numbers at all.
    """
    lens = "\n".join(
        f"- {t['slug']}: {t['name']} — {t.get('description', '') or 'no description'}"
        for t in topics
    ) or "- (no topic context)"
    document = (
        "The full document is attached at `attachments.pdf_path`. Open it and "
        "read it — the payload's abstract is a summary of the paper's claims, "
        "not of its findings.\n\n"
        "Read it as a document, not as text: the result tables and figures "
        "settle what was actually achieved faster than the prose does. Take "
        "`results` and `limitations` from the experiments section rather than "
        "from the abstract's framing, and say which numbers come from "
        "simulation and which from hardware or real data where the paper "
        "distinguishes them. If a headline holds only under a condition — a "
        "scale, a threshold, a subset of tasks — that condition belongs in "
        "`results`.\n\n"
        f"{_READ_FROM_RULE}\n\n"
        if has_pdf
        else ""
    )
    return (
        "Read the paper below and produce a structured summary.\n\n"
        f"{document}"
        "It matched these tracked topics; `relevance` must contain one entry "
        "per slug, stating what this paper changes for that topic:\n"
        f"{lens}\n\n" + _MODELS_RULE + "\n\n"
        + _SHARED_RULES.format(language=language)
    )


def local_pdf_instructions(topics: list[dict], language: str = "en") -> str:
    """Prompt for reading a PDF that was filed by hand.

    Differs from ``paper_instructions`` in three ways, all forced by the fact
    that nothing has read the document yet: the source material is a file
    rather than an abstract, the bibliography has to be recovered from the
    document itself, and the topics are a question rather than an answer.
    """
    lens = "\n".join(
        f"- {t['slug']}: {t['name']} — {t.get('description', '') or 'no description'}"
        for t in topics
    ) or "- (no topics are defined)"
    return (
        "A PDF was filed by hand. Open the file at `attachments.pdf_path` and "
        "read it, then produce a structured summary.\n\n"
        "Read it as a document, not as text: look at the figures, tables and "
        "plots. A result table usually settles what the paper actually "
        "achieved faster than the prose does, and a figure often carries the "
        "method. If the document is long, read the abstract, introduction, "
        "method and results sections in full and skim the rest.\n\n"
        "`bibliography` must come from the document itself — its title page, "
        "header or footer. The filename is not evidence; it is whatever the "
        "person who saved the file happened to type.\n\n"
        "`topics` is your judgement. These are the topics this archive tracks; "
        "list the slugs this paper genuinely belongs to, and leave the list "
        "empty rather than forcing a fit:\n"
        f"{lens}\n\n"
        "`relevance` must have one entry per slug you listed in `topics`.\n\n"
        f"{_MODELS_RULE}\n\n"
        f"{_READ_FROM_RULE}\n\n" + _SHARED_RULES.format(language=language)
    )


def video_instructions(topics: list[dict], language: str = "en") -> str:
    """Prompt for reading a seminar recording."""
    lens = "\n".join(
        f"- {t['slug']}: {t['name']} — {t.get('description', '') or 'no description'}"
        for t in topics
    ) or "- (no topic context)"
    return (
        "Summarize the seminar recording below.\n\n"
        "Derive `chapters` from the transcript timestamps so a reader can jump "
        "to the part they need; if no transcript is supplied, return an empty "
        "chapters list and work from the title and description only. Every "
        "chapter needs a real `start_s` taken from the transcript — omit the "
        "chapter rather than guess, because a wrong timestamp is worse than a "
        "missing one.\n\n"
        "It matched these tracked topics:\n"
        f"{lens}\n\n" + _SHARED_RULES.format(language=language)
    )


def concept_instructions(
    name: str, language: str = "en", *, previous: str = ""
) -> str:
    """Prompt for defining a wiki entity from the sources that mention it.

    ``previous`` turns it into a revision. A definition whose evidence has
    outgrown it is not a blank page: somebody read the sources and ruled, and
    most of that ruling is usually still right. Asking for a rewrite would throw
    away the judgement along with the staleness, so the old text is handed back
    with the question "what has changed" rather than "what is this".
    """
    if previous:
        return (
            f"Revise the wiki definition for '{name}'.\n\n"
            "It was written against fewer sources than the archive now holds. "
            "The sources below are all of them, including the ones that have "
            "arrived since.\n\n"
            "This is the definition as it stands:\n\n"
            f"    {previous}\n\n"
            "**Keep what still holds.** Change it where a later source "
            "contradicts it, narrows it, or shows the term being used in a way "
            "the old text does not cover — and say so plainly rather than "
            "hedging the original into something vaguer. If the new sources "
            "change nothing, return it unchanged; that is a real answer and it "
            "records that somebody checked.\n\n"
            "A definition that enumerates its sources by name is the one most "
            "likely to be quietly wrong now. Prefer stating what the term means "
            "to counting where it appears.\n\n"
            + _SHARED_RULES.format(language=language)
        )
    return (
        f"Write the wiki definition for '{name}'.\n\n"
        "The sources below are every archived paper and talk that mentions it. "
        "Define it as they use it: if they disagree, say so; if the term is "
        "used loosely, say that too.\n\n"
        "`related` is the one part of the note nothing can work out on its own. "
        "The wiki already links entities that turn up in the same summary; what "
        "it cannot see is the neighbour a reader would actually want next — the "
        "generation before this one, the benchmark it was built to beat, the "
        "method it replaces. Name those. Leave the list empty rather than "
        "repeating what the sources already put side by side.\n\n"
        + _SHARED_RULES.format(language=language)
    )


# ---------------------------------------------------------------------------
# Backends
# ---------------------------------------------------------------------------


class Summarizer(Protocol):
    """Produces a structured reading, or defers it.

    Returning ``None`` means "not available now, it has been queued" — not
    "failed". Callers must treat it as a normal outcome.
    """

    name: str

    def summarize_paper(
        self,
        paper: Paper,
        topics: list[dict],
        language: str,
        contested_with: str = "",
    ) -> PaperSummary | None: ...

    def summarize_video(
        self,
        video: Video,
        transcript: list[dict],
        topics: list[dict],
        language: str,
    ) -> VideoSummary | None: ...

    def define_concept(
        self, name: str, sources: list[dict], language: str, previous: str = ""
    ) -> dict | None: ...


EnqueueFn = Callable[..., str]


class QueueSummarizer:
    """Defers every summary to the daily agent session.

    ``enqueue`` is injected rather than imported so that this module stays free
    of any dependency on the queue implementation.
    """

    name = "queue"

    def __init__(self, enqueue: EnqueueFn) -> None:
        self._enqueue = enqueue

    def summarize_paper(
        self,
        paper: Paper,
        topics: list[dict],
        language: str,
        contested_with: str = "",
    ) -> PaperSummary | None:
        # A hand-filed PDF is still a paper task — same kind, same appliers,
        # same archive page. Only the prompt, the extra schema fields and the
        # attached file differ, because the record has no abstract to read.
        local = paper.is_local
        has_document = bool(paper.local_path)
        self._enqueue(
            kind="paper",
            item_id=paper.id,
            topics=[t["slug"] for t in topics],
            language=language,
            instructions=(
                local_pdf_instructions(topics, language)
                if local
                else paper_instructions(topics, language, has_pdf=has_document)
            ) + _contested_warning(paper.id, contested_with),
            output_schema=_paper_schema(local=local, has_document=has_document),
            # Whatever a paper's provenance, if a document is on disk the
            # reader is told where it is. A fetched PDF and a hand-filed one
            # are the same thing to whoever has to read it.
            attachments=(
                {"pdf_path": paper.local_path} if paper.local_path else None
            ),
            payload={
                "contested_with": contested_with,
                "title": paper.title,
                "authors": paper.authors,
                "abstract": paper.abstract,
                "venue": paper.venue,
                "published": paper.published,
                "categories": paper.categories,
                "url": paper.url,
                "pdf_url": paper.pdf_url,
                "matched_keywords": paper.matched_keywords,
                "scores": paper.scores,
            },
        )
        return None

    def summarize_video(
        self,
        video: Video,
        transcript: list[dict],
        topics: list[dict],
        language: str,
    ) -> VideoSummary | None:
        self._enqueue(
            kind="video",
            item_id=video.id,
            topics=[t["slug"] for t in topics],
            language=language,
            instructions=video_instructions(topics, language),
            output_schema=VIDEO_OUTPUT_SCHEMA,
            payload={
                "title": video.title,
                "channel": video.channel,
                "published": video.published,
                "duration_s": video.duration_s,
                "description": video.description,
                "url": video.url,
                "transcript_available": video.transcript_available,
                "matched_keywords": video.matched_keywords,
                "scores": video.scores,
            },
            attachments={"transcript": transcript} if transcript else None,
        )
        return None

    def define_concept(
        self, name: str, sources: list[dict], language: str, previous: str = ""
    ) -> dict | None:
        payload = {"name": name, "source_count": len(sources)}
        if previous:
            # Carried in the payload as well as the prompt, so that what the
            # reviser was working from is recoverable from the archived task
            # after the fact. `source_count` is the count this answer will be
            # recorded as written against, which is what makes the next
            # staleness check measure growth since *this* revision.
            payload["previous_definition"] = previous
        self._enqueue(
            kind="concept",
            item_id=name,
            topics=sorted({t for s in sources for t in s.get("topics", [])}),
            language=language,
            instructions=concept_instructions(name, language, previous=previous),
            output_schema=CONCEPT_OUTPUT_SCHEMA,
            payload=payload,
            attachments={"sources": sources},
        )
        return None


class AnthropicSummarizer:
    """Direct Claude API backend.

    Deliberately unimplemented: the interface, the prompts and the output
    schema above are the contract. To enable it, implement the two methods so
    they send ``*_instructions(...)`` plus the record as the user message and
    parse the JSON response into the dataclass.
    """

    name = "anthropic"

    def __init__(self, options: dict[str, Any] | None = None) -> None:
        self.options = options or {}

    def _unavailable(self) -> None:
        raise SummarizerNotConfigured(
            "the `anthropic` summarizer backend is an interface only. "
            "Implement AnthropicSummarizer in pipelines/common/llm.py, or set "
            "`summarize.backend: queue` in config/settings.yaml."
        )

    def summarize_paper(self, paper, topics, language, contested_with=""):  # noqa: D102
        self._unavailable()

    def summarize_video(self, video, transcript, topics, language):  # noqa: D102
        self._unavailable()

    def define_concept(self, name, sources, language):  # noqa: D102
        self._unavailable()


class OllamaSummarizer:
    """Local model backend. Same contract, same deliberate gap."""

    name = "ollama"

    def __init__(self, options: dict[str, Any] | None = None) -> None:
        self.options = options or {}

    def _unavailable(self) -> None:
        raise SummarizerNotConfigured(
            "the `ollama` summarizer backend is an interface only. "
            "Implement OllamaSummarizer in pipelines/common/llm.py, or set "
            "`summarize.backend: queue` in config/settings.yaml."
        )

    def summarize_paper(self, paper, topics, language, contested_with=""):  # noqa: D102
        self._unavailable()

    def summarize_video(self, video, transcript, topics, language):  # noqa: D102
        self._unavailable()

    def define_concept(self, name, sources, language):  # noqa: D102
        self._unavailable()


def get_summarizer(settings: dict, *, enqueue: EnqueueFn) -> Summarizer:
    """Build the backend named in ``summarize.backend``."""
    block = settings.get("summarize", {}) or {}
    backend = str(block.get("backend", "queue")).lower()
    if backend == "queue":
        return QueueSummarizer(enqueue)
    if backend == "anthropic":
        return AnthropicSummarizer(block.get("anthropic"))
    if backend == "ollama":
        return OllamaSummarizer(block.get("ollama"))
    raise SummarizerNotConfigured(
        f"unknown summarize.backend '{backend}'; expected queue, anthropic or ollama"
    )
