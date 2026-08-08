"""Run logging.

Logs go to stderr so that a command's real output can still be piped, and to
a dated file under ``data/logs/`` so a Routine run leaves a trace.
"""

from __future__ import annotations

import logging
import sys
from datetime import date
from pathlib import Path

_CONFIGURED = False


def setup(log_dir: Path | None = None, level: int = logging.INFO) -> None:
    """Configure the root logger once per process."""
    global _CONFIGURED
    if _CONFIGURED:
        return

    root = logging.getLogger()
    root.setLevel(level)

    fmt = logging.Formatter(
        "%(asctime)s %(levelname)-7s %(name)-28s %(message)s",
        datefmt="%H:%M:%S",
    )

    stream = logging.StreamHandler(sys.stderr)
    stream.setFormatter(fmt)
    root.addHandler(stream)

    if log_dir is not None:
        log_dir.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(
            log_dir / f"{date.today().isoformat()}.log", encoding="utf-8"
        )
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)-7s %(name)-28s %(message)s"
            )
        )
        root.addHandler(handler)

    _CONFIGURED = True


def get(name: str) -> logging.Logger:
    return logging.getLogger(name)
