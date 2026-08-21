"""Source collectors.

Every collector exposes ``collect(...) -> list[Paper] | list[Video]`` and must
fail soft: one unreachable API cannot be allowed to abort the daily run, so
collectors log and return what they have.
"""
