"""HTTP access for collectors.

Standard library only. Adds the three things every collector needs and none of
them should reimplement: a per-host rate limit, bounded retries with
exponential backoff, and a real User-Agent (arXiv and DBLP throttle anonymous
clients hard).
"""

from __future__ import annotations

import http.client
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

# A host that has failed this many whole requests in a row is dropped for the
# rest of the process. Each of those is already several retries, so the
# threshold means sustained failure, not a bad minute.
DEFAULT_GIVE_UP_AFTER_FAILURES = 5

# host -> monotonic timestamp of the last request
_LAST_REQUEST: dict[str, float] = {}
# host -> consecutive whole-request failures; and the hosts we have given up on.
_CONSECUTIVE_FAILURES: dict[str, int] = {}
_TRIPPED: set[str] = set()


class HTTPError(Exception):
    """A request failed after exhausting its retries."""


class HostUnavailable(HTTPError):
    """This host has failed all run, so no request was attempted.

    Subclasses ``HTTPError`` on purpose: every collector already treats that as
    "this source gave me nothing", which is exactly what happened. Giving up
    needs no new handling anywhere.
    """


def reset_circuit_breakers() -> None:
    """Forget every host's failure history. For tests and long-lived processes."""
    _CONSECUTIVE_FAILURES.clear()
    _TRIPPED.clear()


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
        give_up_after_failures: int = DEFAULT_GIVE_UP_AFTER_FAILURES,
    ) -> None:
        self.user_agent = user_agent
        self.timeout_s = timeout_s
        self.retries = max(1, int(retries))
        self.backoff_s = backoff_s
        self.min_interval_s = min_interval_s
        self.give_up_after_failures = max(0, int(give_up_after_failures))

    # -- internals ----------------------------------------------------------
    def _check_host(self, host: str) -> None:
        if self.give_up_after_failures and host in _TRIPPED:
            raise HostUnavailable(
                f"{host} has failed every request this run; not asking again"
            )

    def _record_success(self, host: str) -> None:
        # A host that merely blips never trips: the counter is consecutive.
        _CONSECUTIVE_FAILURES.pop(host, None)

    def _record_failure(self, host: str) -> None:
        if not self.give_up_after_failures:
            return
        count = _CONSECUTIVE_FAILURES.get(host, 0) + 1
        _CONSECUTIVE_FAILURES[host] = count
        if count >= self.give_up_after_failures and host not in _TRIPPED:
            _TRIPPED.add(host)
            _LOG.warning(
                "%s has failed %d consecutive requests; skipping it for the rest "
                "of this run",
                host,
                count,
            )

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

        host = urllib.parse.urlparse(url).netloc
        self._check_host(host)

        last_error: Exception | None = None
        for attempt in range(self.retries):
            self._throttle(url)
            request = urllib.request.Request(url, headers=request_headers)
            try:
                with urllib.request.urlopen(request, timeout=self.timeout_s) as response:
                    body = response.read()
                self._record_success(host)
                return body
            except urllib.error.HTTPError as exc:
                last_error = exc
                # 4xx other than rate limiting will not fix itself.
                if exc.code not in (408, 429) and 400 <= exc.code < 500:
                    # Counted toward the breaker, deliberately: a host answering
                    # 403 to every lookup is precisely the case worth stopping,
                    # and a 4xx is a stronger signal than a timeout, not weaker.
                    self._record_failure(host)
                    raise HTTPError(f"GET {url} -> HTTP {exc.code}") from exc
            except (
                urllib.error.URLError,
                TimeoutError,
                OSError,
                # A response that ends early raises IncompleteRead, which
                # descends from HTTPException and *not* from OSError. Without
                # this arm a truncated read — the transient condition the retry
                # loop exists for — escapes the loop uncaught.
                http.client.HTTPException,
            ) as exc:
                last_error = exc

            if attempt < self.retries - 1:
                delay = self.backoff_s * (2**attempt)
                _LOG.warning(
                    "GET %s failed (%s); retrying in %.1fs", url, last_error, delay
                )
                time.sleep(delay)

        self._record_failure(host)
        raise HTTPError(f"GET {url} failed after {self.retries} attempts: {last_error}")

    def get_json(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kw,
    ) -> Any:
        # `headers` is named rather than left to arrive through **kw: this
        # method supplies an Accept header of its own, so a caller passing one
        # through **kw would reach `get` as a duplicate keyword argument and
        # raise TypeError before a request was ever made.
        merged = {"Accept": "application/json"}
        merged.update(headers or {})
        raw = self.get(url, params, headers=merged, **kw)
        try:
            return json.loads(raw.decode("utf-8", errors="replace"))
        except json.JSONDecodeError as exc:
            raise HTTPError(f"GET {url} returned invalid JSON: {exc}") from exc

    def get_xml(
        self,
        url: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kw,
    ) -> ET.Element:
        raw = self.get(url, params, headers=headers, **kw)
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
        give_up_after_failures=int(
            collect.get("give_up_after_failures", DEFAULT_GIVE_UP_AFTER_FAILURES)
        ),
    )
