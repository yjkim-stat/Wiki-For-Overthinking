"""Tests for the shared HTTP client.

These drive the real ``Client`` rather than a stub. That is the point: the
collectors are tested through a stub whose signature is more permissive than
the real thing, so anything about the client's own contract has to be checked
here or it is not checked at all.
"""

from __future__ import annotations

import http.client
import unittest
import urllib.error
from unittest import mock

from pipelines.common.http import (
    Client,
    HostUnavailable,
    HTTPError,
    reset_circuit_breakers,
)


class _Response:
    """The slice of an ``http.client.HTTPResponse`` that ``get`` touches."""

    def __init__(self, body: bytes) -> None:
        self.body = body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self) -> bytes:
        return self.body


class RetryTests(unittest.TestCase):
    """A truncated response is transient, and must be retried like one."""

    def _client(self, retries: int = 3) -> Client:
        return Client(retries=retries, backoff_s=0)

    def test_a_response_that_truncates_once_succeeds_on_the_retry(self):
        attempts: list[int] = []

        def flaky(request, timeout=None):
            attempts.append(1)
            if len(attempts) == 1:
                raise http.client.IncompleteRead(b"partial")
            return _Response(b"whole")

        with mock.patch("urllib.request.urlopen", flaky):
            self.assertEqual(self._client().get("https://example.org"), b"whole")
        self.assertEqual(len(attempts), 2)

    def test_a_permanently_truncating_host_gives_up(self):
        """The retry arm must not turn a hard failure into an unbounded loop."""
        attempts: list[int] = []

        def always_truncated(request, timeout=None):
            attempts.append(1)
            raise http.client.IncompleteRead(b"partial")

        with mock.patch("urllib.request.urlopen", always_truncated):
            with self.assertRaises(HTTPError):
                self._client(retries=3).get("https://example.org")
        self.assertEqual(len(attempts), 3)

    def test_other_http_exceptions_are_retried_too(self):
        """IncompleteRead is the one that was seen; the family is the fix."""
        attempts: list[int] = []

        def flaky(request, timeout=None):
            attempts.append(1)
            if len(attempts) == 1:
                raise http.client.BadStatusLine("garbage")
            return _Response(b"ok")

        with mock.patch("urllib.request.urlopen", flaky):
            self.assertEqual(self._client().get("https://example.org"), b"ok")
        self.assertEqual(len(attempts), 2)


class HeaderTests(unittest.TestCase):
    """``get_json`` supplies an Accept header and must still accept the caller's."""

    def _capture(self):
        """Run the real client against a recorded request."""
        seen: dict = {}

        def urlopen(request, timeout=None):
            seen["url"] = request.full_url
            seen["headers"] = dict(request.header_items())
            return _Response(b'{"ok": true}')

        return seen, urlopen

    def test_caller_headers_are_merged_with_accept(self):
        seen, urlopen = self._capture()
        with mock.patch("urllib.request.urlopen", urlopen):
            Client().get_json("https://example.org", {}, headers={"x-api-key": "k"})
        # urllib title-cases header names on the way in.
        lowered = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(lowered["accept"], "application/json")
        self.assertEqual(lowered["x-api-key"], "k")

    def test_empty_headers_do_not_raise(self):
        """The no-API-key path: `headers={}` was enough to trigger the collision."""
        seen, urlopen = self._capture()
        with mock.patch("urllib.request.urlopen", urlopen):
            result = Client().get_json("https://example.org", {}, headers={})
        self.assertEqual(result, {"ok": True})
        lowered = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(lowered["accept"], "application/json")

    def test_a_caller_may_override_accept(self):
        seen, urlopen = self._capture()
        with mock.patch("urllib.request.urlopen", urlopen):
            Client().get_json("https://x.org", {}, headers={"Accept": "text/plain"})
        lowered = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(lowered["accept"], "text/plain")

    def test_get_xml_takes_headers_too(self):
        seen = {}

        def urlopen(request, timeout=None):
            seen["headers"] = dict(request.header_items())
            return _Response(b"<feed/>")

        with mock.patch("urllib.request.urlopen", urlopen):
            Client().get_xml("https://example.org", {}, headers={"x-token": "t"})
        lowered = {k.lower(): v for k, v in seen["headers"].items()}
        self.assertEqual(lowered["x-token"], "t")



class CircuitBreakerTests(unittest.TestCase):
    """A host that is down for the whole run stops being asked.

    Retries are correctly scoped to one request, but a run makes hundreds. When
    a host is down for all of them, per-request retry turns one dead source into
    the run's dominant cost and still returns nothing.
    """

    def setUp(self):
        reset_circuit_breakers()

    def tearDown(self):
        reset_circuit_breakers()

    def _dead(self, calls: list):
        def urlopen(request, timeout=None):
            calls.append(request.full_url)
            raise urllib.error.URLError("down")

        return urlopen

    def test_the_breaker_stops_calling_after_the_threshold(self):
        calls: list = []
        client = Client(retries=1, backoff_s=0, give_up_after_failures=3)
        with mock.patch("urllib.request.urlopen", self._dead(calls)):
            for _ in range(3):
                with self.assertRaises(HTTPError):
                    client.get("https://dead.test/a")
            self.assertEqual(len(calls), 3)
            with self.assertRaises(HostUnavailable):
                client.get("https://dead.test/b")
        self.assertEqual(len(calls), 3, "no request should have been attempted")

    def test_host_unavailable_is_an_http_error(self):
        """Collectors already catch HTTPError; giving up needs no new handling."""
        self.assertTrue(issubclass(HostUnavailable, HTTPError))

    def test_a_success_resets_the_counter(self):
        calls: list = []
        client = Client(retries=1, backoff_s=0, give_up_after_failures=2)
        state = {"fail": True}

        def flaky(request, timeout=None):
            calls.append(request.full_url)
            if state["fail"]:
                raise urllib.error.URLError("down")
            return _Response(b"ok")

        with mock.patch("urllib.request.urlopen", flaky):
            for _ in range(5):
                with self.assertRaises(HTTPError):
                    client.get("https://flaky.test/x")
                state["fail"] = False
                self.assertEqual(client.get("https://flaky.test/y"), b"ok")
                state["fail"] = True
        # Alternating failure and success must never trip the breaker.

    def test_one_host_tripping_does_not_affect_another(self):
        client = Client(retries=1, backoff_s=0, give_up_after_failures=2)

        def selective(request, timeout=None):
            if "dead.test" in request.full_url:
                raise urllib.error.URLError("down")
            return _Response(b"alive")

        with mock.patch("urllib.request.urlopen", selective):
            for _ in range(2):
                with self.assertRaises(HTTPError):
                    client.get("https://dead.test/a")
            with self.assertRaises(HostUnavailable):
                client.get("https://dead.test/b")
            self.assertEqual(client.get("https://alive.test/a"), b"alive")

    def test_a_hard_4xx_counts_toward_the_breaker(self):
        """OpenReview answering 403 to every venue is the case worth stopping."""
        client = Client(retries=1, backoff_s=0, give_up_after_failures=2)

        def forbidden(request, timeout=None):
            raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, None)

        with mock.patch("urllib.request.urlopen", forbidden):
            for _ in range(2):
                with self.assertRaises(HTTPError):
                    client.get("https://blocked.test/a")
            with self.assertRaises(HostUnavailable):
                client.get("https://blocked.test/b")

    def test_zero_disables_the_breaker(self):
        calls: list = []
        client = Client(retries=1, backoff_s=0, give_up_after_failures=0)
        with mock.patch("urllib.request.urlopen", self._dead(calls)):
            for _ in range(6):
                with self.assertRaises(HTTPError):
                    client.get("https://dead.test/a")
        self.assertEqual(len(calls), 6, "every request should still be attempted")


if __name__ == "__main__":
    unittest.main()
