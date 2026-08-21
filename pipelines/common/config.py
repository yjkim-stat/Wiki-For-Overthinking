"""Configuration loading and validation.

Topics are data, not code: adding ``config/topics/<slug>.yaml`` is the only
step needed to start tracking a new subject.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from . import paths as P


class ConfigError(Exception):
    """Raised when a config file is missing or malformed."""


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"missing config file: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:  # pragma: no cover - depends on user edits
        raise ConfigError(f"{path}: {exc}") from exc
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ConfigError(f"{path}: expected a mapping at the top level")
    return data


@dataclass
class Topic:
    """One research subject and everything that scopes its collection."""

    slug: str
    name: str
    description: str = ""
    keywords_any: list[str] = field(default_factory=list)
    keywords_all: list[str] = field(default_factory=list)
    keywords_none: list[str] = field(default_factory=list)
    authors: list[str] = field(default_factory=list)
    seed_papers: list[str] = field(default_factory=list)
    min_score: float | None = None
    sources: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, bool] = field(default_factory=dict)
    path: Path | None = None

    def source_enabled(self, name: str) -> bool:
        block = self.sources.get(name)
        if block is None:
            return True
        if isinstance(block, bool):
            return block
        return bool(block.get("enabled", True))

    def source_option(self, name: str, key: str, default: Any = None) -> Any:
        block = self.sources.get(name)
        if not isinstance(block, dict):
            return default
        value = block.get(key, default)
        # An empty list in a topic means "do not narrow", not "match nothing".
        if isinstance(value, list) and not value:
            return default
        return value

    def wants(self, output: str) -> bool:
        return bool(self.outputs.get(output, True))

    def threshold(self, settings: dict) -> float:
        if self.min_score is not None:
            return float(self.min_score)
        return float(settings.get("score", {}).get("default_min_score", 0.35))


@dataclass
class Config:
    """Everything the pipeline needs to run, loaded once per process."""

    settings: dict[str, Any]
    sources: dict[str, Any]
    topics: list[Topic]
    layout: P.Layout

    @property
    def language(self) -> str:
        return self.settings.get("language", "en")

    def topic(self, slug: str) -> Topic:
        for topic in self.topics:
            if topic.slug == slug:
                return topic
        raise KeyError(f"unknown topic: {slug}")

    def topic_context(self, slugs: list[str]) -> list[dict[str, str]]:
        """Topic descriptors handed to a summarizer as reading context.

        Unknown slugs are dropped rather than raising: a record may carry a
        topic that has since been deleted, and that is not a reason to fail.
        """
        context = []
        for slug in slugs:
            try:
                topic = self.topic(slug)
            except KeyError:
                continue
            context.append(
                {
                    "slug": topic.slug,
                    "name": topic.name,
                    "description": topic.description,
                }
            )
        return context


def _parse_topic(data: dict[str, Any], path: Path) -> Topic:
    slug = str(data.get("slug") or path.stem).strip()
    if not slug:
        raise ConfigError(f"{path}: topic needs a `slug`")
    if slug != path.stem:
        raise ConfigError(
            f"{path}: slug '{slug}' must match the filename '{path.stem}'"
        )

    keywords = data.get("keywords") or {}
    if not isinstance(keywords, dict):
        raise ConfigError(f"{path}: `keywords` must be a mapping")

    any_kw = [str(k) for k in (keywords.get("any") or [])]
    if not any_kw:
        raise ConfigError(
            f"{path}: `keywords.any` must list at least one term, otherwise "
            "the topic matches nothing"
        )

    return Topic(
        slug=slug,
        name=str(data.get("name") or slug),
        description=str(data.get("description") or "").strip(),
        keywords_any=any_kw,
        keywords_all=[str(k) for k in (keywords.get("all") or [])],
        keywords_none=[str(k) for k in (keywords.get("none") or [])],
        authors=[str(a) for a in (data.get("authors") or [])],
        seed_papers=[str(s) for s in (data.get("seed_papers") or [])],
        min_score=(
            float(data["min_score"]) if data.get("min_score") is not None else None
        ),
        sources=data.get("sources") or {},
        outputs=data.get("outputs") or {},
        path=path,
    )


def load_topics(topics_dir: Path | None = None) -> list[Topic]:
    """Load every topic file, skipping ``_``-prefixed templates."""
    topics_dir = topics_dir or P.TOPICS_DIR
    if not topics_dir.exists():
        return []
    topics: list[Topic] = []
    for path in sorted(topics_dir.glob("*.yaml")):
        if path.name.startswith("_"):
            continue
        topics.append(_parse_topic(_read_yaml(path), path))
    return topics


def overlapping_keywords(topics: list[Topic]) -> list[tuple[str, str, str]]:
    """Keyword pairs where one term occurs inside another, per topic.

    A single occurrence then matches both and adds to the score twice.
    `enrich/score.py` loops over the terms with no notion that two of them might
    be the same words, which is a deliberate property — a rule you can read and
    correct beats an opaque score — and its cost is that redundancy in the list
    is the author's problem. This is what tells the author they have one.

    Uses the same matcher as scoring rather than a substring test, for the
    reason `common/text.py` exists: a check that disagreed with the scorer about
    what counts as an occurrence would report pairs that do not double-count and
    miss pairs that do.

    Returns ``(topic slug, contained, containing)``, which is the order a person
    needs to decide: the short term has the broader recall and the long one is
    presumably there to weight a specific phrase higher, so neither is
    obviously the one to drop.
    """
    from .text import contains

    found: list[tuple[str, str, str]] = []
    for topic in topics:
        terms = [t for t in topic.keywords_any if t]
        for short in terms:
            for long in terms:
                if short != long and contains(short, long):
                    found.append((topic.slug, short, long))
    return sorted(found)


def load(root: Path | None = None) -> Config:
    """Load settings, sources and topics from the deployment root.

    ``root`` is the tree the archive lives in, which is this checkout unless a
    caller or ``RA_WM_ROOT`` says otherwise. Every entry point loads its config
    through here, so pointing one at another tree points all of them.
    """
    root = P.resolve_root(root)
    settings_file = (root / "config" / "settings.yaml") if root else P.SETTINGS_FILE
    sources_file = (root / "config" / "sources.yaml") if root else P.SOURCES_FILE
    topics_dir = (root / "config" / "topics") if root else P.TOPICS_DIR

    settings = _read_yaml(settings_file)
    sources = _read_yaml(sources_file)
    layout = P.Layout(settings.get("paths"), root=root)
    # LOCAL: the authored concept-alias map, installed here because `slug_for`
    # is called from four modules with no config to hand. Imported inside the
    # function so `common` keeps no import-time edge on `local`.
    from ..local import aliases as _aliases  # LOCAL

    _aliases.install(layout)  # LOCAL
    return Config(
        settings=settings,
        sources=sources,
        topics=load_topics(topics_dir),
        layout=layout,
    )
