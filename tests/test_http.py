"""Tests for the shared HTTP client.

These drive the real ``Client`` rather than a stub. That is the point: the
collectors are tested through a stub whose signature is more permissive than
the real thing, so anything about the client's own contract has to be checked
here or it is not checked at all.
"""

from __future__ import annotations

import http.client
import unittest
from unittest import mock

from pipelines.common.http import Client, HTTPError


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


if __name__ == "__main__":
    unittest.main()
