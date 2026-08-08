"""YouTube seminar collector.

Channel Atom feeds are used rather than the Data API: they need no key, no
quota and no OAuth, which keeps the daily run self-sufficient. The tradeoff is
that a feed carries no duration, so ``min_duration_s`` can only reject videos
whose length is known — unknown-length videos are kept and flagged.

Transcripts require the optional ``youtube-transcript-api`` package. Without
it, videos are still collected and archived, just marked transcript-less.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone

from ..common.config import Config, Topic
from ..common.http import Client, HTTPError, from_settings
from ..common.log import get
from ..common.schema import Video, canonical_video_id, utcnow

_LOG = get(__name__)

_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def _text(node: ET.Element | None, default: str = "") -> str:
    if node is None or node.text is None:
        return default
    return node.text.strip()


def _channels(cfg: Config, topics: list[Topic]) -> list[dict]:
    """Global channels plus any a topic adds, deduplicated by channel id."""
    block = cfg.sources.get("youtube", {}) or {}
    channels: dict[str, dict] = {}

    for channel in block.get("channels") or []:
        channel_id = str(channel.get("channel_id") or "").strip()
        if channel_id:
            channels[channel_id] = channel

    for topic in topics:
        if not topic.source_enabled("youtube"):
            continue
        for channel in topic.source_option("youtube", "channels", []) or []:
            channel_id = str(channel.get("channel_id") or "").strip()
            if channel_id:
                channels.setdefault(channel_id, channel)

    return list(channels.values())


def _parse_entry(entry: ET.Element, fallback_channel: str) -> Video | None:
    video_id = _text(entry.find("yt:videoId", _NS))
    if not video_id:
        return None

    group = entry.find("media:group", _NS)
    description = _text(group.find("media:description", _NS)) if group is not None else ""
    author = entry.find("atom:author", _NS)
    channel = _text(author.find("atom:name", _NS)) if author is not None else ""

    return Video(
        id=canonical_video_id(video_id),
        title=_text(entry.find("atom:title", _NS)),
        source="youtube",
        source_id=video_id,
        channel=channel or fallback_channel,
        channel_id=_text(entry.find("yt:channelId", _NS)),
        url=f"https://www.youtube.com/watch?v={video_id}",
        description=description,
        published=_text(entry.find("atom:published", _NS))[:10],
        first_seen=utcnow(),
        last_seen=utcnow(),
    )


def fetch_transcript(video_id: str, languages: list[str] | None = None) -> list[dict]:
    """Fetch a transcript as ``[{"start_s": float, "text": str}]``.

    Returns an empty list when the optional dependency is missing or the video
    has no captions. Both are ordinary outcomes, not errors.
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore
    except ImportError:
        _LOG.debug("youtube-transcript-api not installed; skipping transcript")
        return []

    languages = languages or ["en", "en-US", "en-GB"]
    raw = None
    try:
        # The package renamed its entry point; support both shapes.
        if hasattr(YouTubeTranscriptApi, "get_transcript"):
            raw = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        else:  # pragma: no cover - depends on installed version
            fetched = YouTubeTranscriptApi().fetch(video_id, languages=languages)
            raw = fetched.to_raw_data() if hasattr(fetched, "to_raw_data") else list(fetched)
    except Exception as exc:  # noqa: BLE001 - library raises many custom types
        _LOG.debug("no transcript for %s: %s", video_id, exc)
        return []

    segments = []
    for item in raw or []:
        if isinstance(item, dict):
            start = item.get("start", 0.0)
            text = item.get("text", "")
        else:  # pragma: no cover - object-style segments
            start = getattr(item, "start", 0.0)
            text = getattr(item, "text", "")
        text = " ".join(str(text).split())
        if text:
            segments.append({"start_s": round(float(start), 2), "text": text})
    return segments


def transcript_text(segments: list[dict]) -> str:
    return " ".join(s.get("text", "") for s in segments).strip()


def collect(
    cfg: Config,
    topics: list[Topic],
    since: date,
    client: Client | None = None,
    errors: list[str] | None = None,
) -> list[Video]:
    """Fetch recent videos from every tracked channel."""
    block = cfg.sources.get("youtube", {}) or {}
    if not block.get("enabled", True):
        _LOG.info("youtube collector disabled in config/sources.yaml")
        return []

    channels = _channels(cfg, topics)
    if not channels:
        _LOG.info("no YouTube channels configured; skipping")
        return []

    feed_url = block.get("feed_url", "https://www.youtube.com/feeds/videos.xml")
    min_duration = int(block.get("min_duration_s", 0))
    client = client or from_settings(cfg.settings, min_interval_s=1.0)
    since_iso = since.isoformat()

    videos: dict[str, Video] = {}
    for channel in channels:
        channel_id = str(channel.get("channel_id"))
        name = str(channel.get("name") or channel_id)
        try:
            root = client.get_xml(feed_url, {"channel_id": channel_id})
        except HTTPError as exc:
            _LOG.error("youtube feed for '%s' failed: %s", name, exc)
            if errors is not None:
                errors.append(f"youtube[{name}]: {exc}")
            continue

        entries = root.findall("atom:entry", _NS)
        kept = 0
        for entry in entries:
            video = _parse_entry(entry, name)
            if video is None:
                continue
            if video.published and video.published < since_iso:
                continue
            # Duration is absent from the feed; only reject when it is known.
            if min_duration and video.duration_s and video.duration_s < min_duration:
                continue
            videos.setdefault(video.id, video)
            kept += 1
        _LOG.info("youtube: %d/%d recent videos from '%s'", kept, len(entries), name)

    return list(videos.values())


def parse_published(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(
            timezone.utc
        )
    except (ValueError, AttributeError):
        return None
