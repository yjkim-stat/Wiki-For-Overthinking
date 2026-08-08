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
    "datasets": ["string - datasets, benchmarks, corpora or simulators used"],
    "tags": ["string - short lowercase keywords"],
}

VIDEO_OUTPUT_SCHEMA: dict[str, Any] = {
    "one_liner": "string - what the talk is about, in one sentence",
    "abstract": "string - a paragraph covering the argument of the talk",
    "chapters": [
        {
            "start_s": "integer - start time in seconds",
            "title": "string - short chapter title",
            "summary": "string - what is covered in this stretch",
        }
    ],
    "key_points": ["string - a claim or takeaway worth remembering"],
    "referenced_papers": ["string - paper titles or arXiv ids mentioned"],
    "concepts": ["string"],
    "methods": ["string"],
    "datasets": ["string"],
    "tags": ["string - short lowercase keywords"],
}

CONCEPT_OUTPUT_SCHEMA: dict[str, Any] = {
    "definition": (
        "string - two to four sentences defining the entity as the cited "
        "sources use it, not as a textbook would"
    ),
    "kind": "string - one of: concept, method, dataset",
    "aliases": ["string - other names the sources use for the same thing"],
    "related": ["string - names of neighbouring entities worth linking"],
}

_SHARED_RULES = """
Rules:
- Write in {language}.
- Ground every statement in the supplied material. If something is not stated,
  leave the field empty rather than inferring it.
- No marketing language. Prefer the specific number over the adjective.
- Return one JSON object matching the schema exactly. No prose around it.
""".strip()


def paper_instructions(topics: list[dict], language: str = "en") -> str:
    """Prompt for reading a paper through the lens of the matched topics."""
    lens = "\n".join(
        f"- {t['slug']}: {t['name']} — {t.get('description', '') or 'no description'}"
        for t in topics
    ) or "- (no topic context)"
    return (
        "Read the paper below and produce a structured summary.\n\n"
        "It matched these tracked topics; `relevance` must contain one entry "
        "per slug, stating what this paper changes for that topic:\n"
        f"{lens}\n\n" + _SHARED_RULES.format(language=language)
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
        "chapters list and work from the title and description only.\n\n"
        "It matched these tracked topics:\n"
        f"{lens}\n\n" + _SHARED_RULES.format(language=language)
    )


def concept_instructions(name: str, language: str = "en") -> str:
    """Prompt for defining a wiki entity from the sources that mention it."""
    return (
        f"Write the wiki definition for '{name}'.\n\n"
        "The sources below are every archived paper and talk that mentions it. "
        "Define it as they use it: if they disagree, say so; if the term is "
        "used loosely, say that too.\n\n" + _SHARED_RULES.format(language=language)
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
        self, paper: Paper, topics: list[dict], language: str
    ) -> PaperSummary | None: ...

    def summarize_video(
        self,
        video: Video,
        transcript: list[dict],
        topics: list[dict],
        language: str,
    ) -> VideoSummary | None: ...

    def define_concept(
        self, name: str, sources: list[dict], language: str
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
        self, paper: Paper, topics: list[dict], language: str
    ) -> PaperSummary | None:
        self._enqueue(
            kind="paper",
            item_id=paper.id,
            topics=[t["slug"] for t in topics],
            language=language,
            instructions=paper_instructions(topics, language),
            output_schema=PAPER_OUTPUT_SCHEMA,
            payload={
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
        self, name: str, sources: list[dict], language: str
    ) -> dict | None:
        self._enqueue(
            kind="concept",
            item_id=name,
            topics=sorted({t for s in sources for t in s.get("topics", [])}),
            language=language,
            instructions=concept_instructions(name, language),
            output_schema=CONCEPT_OUTPUT_SCHEMA,
            payload={"name": name, "source_count": len(sources)},
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

    def summarize_paper(self, paper, topics, language):  # noqa: D102
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

    def summarize_paper(self, paper, topics, language):  # noqa: D102
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
