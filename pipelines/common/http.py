"""HTTP access for collectors.

Standard library only. Adds the three things every collector needs and none of
them should reimplement: a per-host rate limit, bounded retries with
exponential backoff, and a real User-Agent (arXiv and DBLP throttle anonymous
clients hard).
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any

from . import log

_LOG = log.get(__name__)

DEFAULT_USER_AGENT = "recipe-for-research-team-management/0.1"

# host -> monotonic timestamp of the last request
_LAST_REQUEST: dict[str, float] = {}


class HTTPError(Exception):
    """A request failed after exhausting its retries."""


class Client:
    """A small, polite HTTP client."""

    def __init__(
        self,
        *,
        user_agent: str = DEFAULT_USER_AGENT,
        timeout_s: float = 30.0,
        retries: int = 3,
        backoff_s: float = 2.0,
        min_interval_s: float = 0.0,
    ) -> None:
        self.user_agent = user_agent
        self.timeout_s = timeout_s
        self.retries = max(1, int(retries))
        self.backoff_s = backoff_s
        self.min_interval_s = min_interval_s

    # -- internals ----------------------------------------------------------
    def _throttle(self, url: str) -> None:
        if self.min_interval_s <= 0:
            return
        host = urllib.parse.urlparse(url).netloc
        last = _LAST_REQUEST.get(host)
        if last is not None:
            wait = self.min_interval_s - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        _LAST_REQUEST[host] = time.monotonic()

    def get(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> bytes:
        """GET ``url``, retrying transient failures."""
        if params:
            query = urllib.parse.urlencode(
                {k: v for k, v in params.items() if v not in (None, "")},
                doseq=True,
            )
            url = f"{url}?{query}"

        request_headers = {"User-Agent": self.user_agent, "Accept": "*/*"}
        request_headers.update(headers or {})

        last_error: Exception | None = None
        for attempt in range(self.retries):
            self._throttle(url)
            request = urllib.request.Request(url, headers=request_headers)
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_s) as response:
                    return response.read()
            except urllib.error.HTTPError as exc:
                last_error = exc
                # 4xx other than rate limiting will not fix itself.
                if exc.code not in (408, 429) and 400 <= exc.code < 500:
                    raise HTTPError(f"GET {url} -> HTTP {exc.code}") from exc
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                last_error = exc

            if attempt < self.retries - 1:
                delay = self.backoff_s * (2**attempt)
                _LOG.warning(
                    "GET %s failed (%s); retrying in %.1fs", url, last_error, delay
                )
                time.sleep(delay)

        raise HTTPError(f"GET {url} failed after {self.retries} attempts: {last_error}")

    def get_json(self, url: str, params: dict[str, Any] | None = None, **kw) -> Any:
        raw = self.get(url, params, headers={"Accept": "application/json"}, **kw)
        try:
            return json.loads(raw.decode("utf-8", errors="replace"))
        except json.JSONDecodeError as exc:
            raise HTTPError(f"GET {url} returned invalid JSON: {exc}") from exc

    def get_xml(self, url: str, params: dict[str, Any] | None = None, **kw) -> ET.Element:
        raw = self.get(url, params, **kw)
        try:
            return ET.fromstring(raw)
        except ET.ParseError as exc:
            raise HTTPError(f"GET {url} returned invalid XML: {exc}") from exc


def from_settings(settings: dict, *, min_interval_s: float = 0.0) -> Client:
    """Build a client from the ``collect`` block of settings.yaml."""
    collect = settings.get("collect", {})
    return Client(
        user_agent=collect.get("user_agent", DEFAULT_USER_AGENT),
        timeout_s=float(collect.get("request_timeout_s", 30)),
        retries=int(collect.get("retries", 3)),
        backoff_s=float(collect.get("retry_backoff_s", 2)),
        min_interval_s=min_interval_s,
    )
