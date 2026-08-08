"""A throwaway repository checkout for tests.

Tests must never touch the real ``data/``, so each one builds a temporary root
with its own config and a copy of the real templates.
"""

from __future__ import annotations

import shutil
import tempfile
import textwrap
from pathlib import Path

from pipelines.common import config as config_mod
from pipelines.common.paths import REPO_ROOT

_SETTINGS = """
language: en
paths:
  data: data
  archive: archive
  wiki: wiki
  outputs: outputs
  templates: templates
collect:
  lookback_days: 2
  max_items_per_source: 10
  request_timeout_s: 5
  retries: 1
  user_agent: "test-agent/0.1"
score:
  title_weight: 3.0
  abstract_weight: 1.0
  author_bonus: 2.0
  default_min_score: 0.35
summarize:
  backend: queue
  max_pending_tasks: 50
wiki:
  promote_after_mentions: 2
  auto_block_begin: "<!-- auto:begin -->"
  auto_block_end: "<!-- auto:end -->"
"""

_SOURCES = """
arxiv:
  enabled: false
  categories: [cs.RO]
conferences:
  enabled: false
  venues: []
youtube:
  enabled: false
  channels: []
"""

_TOPIC = """
slug: {slug}
name: {name}
description: A topic used by the test suite.
keywords:
  any:
    - world model
    - latent action
  all: []
  none:
    - unrelated nonsense
authors: []
seed_papers: []
min_score: 0.3
sources:
  arxiv:
    enabled: true
  conferences:
    enabled: true
  youtube:
    enabled: true
outputs:
  lecture_note: true
  slides: true
  report: true
"""


class Sandbox:
    """Temporary repository root, cleaned up on ``close()``."""

    def __init__(self, topics: dict[str, str] | None = None) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="rwam-test-"))
        (self.root / "config" / "topics").mkdir(parents=True)

        (self.root / "config" / "settings.yaml").write_text(
            textwrap.dedent(_SETTINGS).strip() + "\n", encoding="utf-8"
        )
        (self.root / "config" / "sources.yaml").write_text(
            textwrap.dedent(_SOURCES).strip() + "\n", encoding="utf-8"
        )

        for slug, name in (topics or {"test-topic": "Test Topic"}).items():
            (self.root / "config" / "topics" / f"{slug}.yaml").write_text(
                _TOPIC.format(slug=slug, name=name), encoding="utf-8"
            )

        shutil.copytree(REPO_ROOT / "templates", self.root / "templates")

    def config(self):
        cfg = config_mod.load(self.root)
        cfg.layout.ensure()
        return cfg

    def close(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)

    def __enter__(self) -> "Sandbox":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
