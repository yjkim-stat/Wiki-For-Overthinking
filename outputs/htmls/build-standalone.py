#!/usr/bin/env python3
"""Build the offline twin of a deck.

Reads outputs/htmls/overthinking.html — which pulls its typefaces from Google
Fonts and its captured figures from figures/ — and writes
outputs/htmls/overthinking-standalone.html, which carries both inside itself.

Every glyph the deck actually uses is subset out of the Noto Sans CJK KR faces
installed on this host, compressed to WOFF and inlined as a data: URI; every
<img src="figures/…"> is inlined the same way. The standalone file therefore
opens correctly with no network and no sibling files.

Run it again after editing the source deck; the two are meant to stay in sync.
"""

import base64
import io
import pathlib
import re
import sys

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter, Options

SRC = pathlib.Path("outputs/htmls/overthinking.html")
DST = pathlib.Path("outputs/htmls/overthinking-standalone.html")

NOTO_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
NOTO_BLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
KR_FACE = 1        # Noto Sans CJK KR
KR_MONO_FACE = 6   # Noto Sans Mono CJK KR


def deck_charset(html: str) -> str:
    """Every character the deck could render.

    Taking the whole document rather than only its text nodes over-includes a
    little CSS and script punctuation, all of it ASCII the face already
    carries. Under-including is the failure that matters: a glyph missing from
    the subset renders as a blank box with nothing to say why.
    """
    chars = set(html)
    chars |= set("  ")
    return "".join(sorted(c for c in chars if c.isprintable() or c == " "))


def subset_woff(path: str, face: int, text: str) -> bytes:
    font = TTFont(path, fontNumber=face) if path.endswith(".ttc") else TTFont(path)

    opts = Options()
    opts.layout_features = ["*"]
    opts.name_IDs = [1, 2, 3, 4, 6]
    opts.notdef_outline = True
    opts.recalc_bounds = True
    opts.drop_tables += ["DSIG"]

    sub = Subsetter(options=opts)
    sub.populate(text=text)
    sub.subset(font)

    font.flavor = "woff"          # zlib — no brotli on this host, so not woff2
    buf = io.BytesIO()
    font.save(buf)
    return buf.getvalue()


def face_rule(family: str, lo: int, hi: int, style: str, data: bytes) -> str:
    b64 = base64.b64encode(data).decode("ascii")
    return (
        "    @font-face {\n"
        f"      font-family: '{family}';\n"
        f"      font-style: {style};\n"
        f"      font-weight: {lo} {hi};\n"
        "      font-display: block;\n"
        f"      src: url(data:font/woff;base64,{b64}) format('woff');\n"
        "    }\n"
    )


def main() -> int:
    if not SRC.exists():
        print(f"missing {SRC}", file=sys.stderr)
        return 1

    html = SRC.read_text(encoding="utf-8-sig")
    text = deck_charset(html)
    print(f"glyph set: {len(text)} characters")

    faces = [
        ("DeckSans", 100, 500, "normal", NOTO_REG, KR_FACE),
        ("DeckSans", 600, 900, "normal", NOTO_BLD, KR_FACE),
        ("DeckMono", 100, 500, "normal", NOTO_REG, KR_MONO_FACE),
        ("DeckMono", 600, 900, "normal", NOTO_BLD, KR_MONO_FACE),
    ]

    rules = []
    total = 0
    for family, lo, hi, style, path, face in faces:
        data = subset_woff(path, face, text)
        total += len(data)
        print(f"  {family} {lo}-{hi}: {len(data)/1024:.0f} KB")
        rules.append(face_rule(family, lo, hi, style, data))
    print(f"embedded fonts: {total/1024:.0f} KB before base64")

    out = html

    # 1. Drop every network reference.
    out = re.sub(r'\n\s*<link rel="preconnect"[^>]*>', "", out)
    out = re.sub(r'\n\s*<link href="https://fonts\.googleapis\.com[^>]*>', "", out)

    # 2. Retitle so the two files are distinguishable in a tab strip.
    out = out.replace(
        "<title>Overthinking — 측정 · 완화 · 한계</title>",
        "<title>Overthinking — 측정 · 완화 · 한계 (standalone)</title>",
    )

    # 3. Inline the captured figures, so the file needs no sibling directory.
    img_bytes = 0
    def inline_img(m):
        nonlocal img_bytes
        rel = m.group(1)
        f = SRC.parent / rel
        if not f.exists():
            raise SystemExit(f"missing figure: {f}")
        raw = f.read_bytes()
        img_bytes += len(raw)
        mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                "svg": "image/svg+xml", "webp": "image/webp"}[f.suffix.lstrip(".").lower()]
        return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(raw).decode("ascii"))

    out, n_img = re.subn(r'src="((?!data:|https?:)[^"]+)"', inline_img, out)
    print(f"inlined figures: {n_img} file(s), {img_bytes/1024:.0f} KB before base64")

    # 4. Inline the faces at the top of the stylesheet.
    banner = (
        "    /* ======================================================================\n"
        "       STANDALONE BUILD — generated, do not hand-edit.\n"
        "       Source: overthinking.html. Regenerate with build_standalone.py after\n"
        "       any edit there. The typefaces below are Noto Sans CJK KR / Noto Sans\n"
        "       Mono CJK KR (SIL Open Font License 1.1), subset to the glyphs this\n"
        "       deck uses and inlined, so the file renders with no network access.\n"
        "       ====================================================================== */\n"
    )
    out = out.replace("  <style>\n", "  <style>\n" + banner + "".join(rules), 1)

    # 5. Point the stacks at the embedded families.
    out = out.replace(
        '--font-main: "Inter", "Noto Sans KR", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;',
        '--font-main: "DeckSans", "Noto Sans CJK KR", "Noto Sans KR", -apple-system, sans-serif;',
    )
    out = out.replace(
        '--font-mono: "JetBrains Mono", Menlo, Consolas, monospace;',
        '--font-mono: "DeckMono", "Noto Sans Mono CJK KR", Menlo, monospace;',
    )

    DST.write_bytes(b"\xef\xbb\xbf" + out.encode("utf-8"))
    print(f"wrote {DST} — {DST.stat().st_size/1024:.0f} KB")

    leftover = re.findall(r'(?:href|src)="(https?://[^"]+)"', out)
    external = [u for u in leftover if not u.startswith("http") or "fonts." in u or "cdn" in u]
    print("remaining subresource URLs:", external or "none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
