#!/usr/bin/env python3
"""Build a slide deck from YAML.

    python3 decks/build.py overthinking              # -> decks/overthinking/build/
    python3 decks/build.py overthinking --standalone # + the offline twin
    python3 decks/build.py overthinking --watch      # rebuild whenever a file changes

A deck is a directory holding `deck.yaml`, `references.yaml`, one YAML file per
slide under `slides/`, and its pictures under `assets/`. Nothing in `build/` is
edited by hand: it is rewritten from those inputs on every run, which is the
whole point of the split — the deck's content is small text files somebody can
read and change, and the 120 KB of HTML is derived from them.

The block vocabulary each slide is written in is documented in decks/README.md.
"""

import argparse
import base64
import html as htmlmod
import io
import pathlib
import re
import shutil
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent

# --------------------------------------------------------------------- helpers


STYLES = {}   # named styles from deck.yaml; see resolve_style


def resolve_style(value):
    """A `style:` may name an entry in deck.yaml's `styles:` instead of
    spelling CSS out. Several names may be given, separated by spaces, and
    anything that is not a name is passed through as the CSS it is."""
    if not value or ":" in value:
        return value
    parts = [STYLES.get(w, w) for w in value.split()]
    return "".join(p if p.endswith(";") else p + ";" for p in parts if p)


def attr(name, value):
    """One HTML attribute, or nothing when the value is empty."""
    if name == "style":
        value = resolve_style(value)
    return f' {name}="{value}"' if value else ""


def as_text(v, key="text"):
    """A block that may be written either as a bare string or as a mapping."""
    return {key: v} if isinstance(v, str) else dict(v or {})


def indent(s, n):
    pad = " " * n
    return "\n".join(pad + l if l.strip() else "" for l in s.split("\n"))


class BuildError(Exception):
    pass


# ---------------------------------------------------------------------- blocks
#
# Every renderer takes the block's value and returns HTML. A block in a slide
# file is a single-key mapping whose key names the renderer:  - lead: "…"


def r_lead(v, ctx):
    d = as_text(v)
    return f'<div class="lead"{attr("style", d.get("style"))}>{d["text"]}</div>'


def r_text(v, ctx):
    d = as_text(v)
    cls = attr("class", d.get("cls"))
    return f'<div{cls}{attr("style", d.get("style"))}>{d["text"]}</div>'


def r_note(v, ctx):
    d = as_text(v)
    return f'<div class="card-n"{attr("style", d.get("style"))}>{d["text"]}</div>'


def r_caption(v, ctx):
    d = as_text(v)
    return f'<div class="figsrc"{attr("style", d.get("style"))}>{d["text"]}</div>'


def r_bullets(v, ctx):
    d = {"bullets": v} if isinstance(v, list) else dict(v or {})
    cls = "b sm" if d.get("size") == "sm" else "b"
    items = "\n".join(f"  <li>{b}</li>" for b in d["bullets"])
    return f'<ul class="{cls}"{attr("style", d.get("style"))}>\n{items}\n</ul>'


def _k_color(card):
    """A card kicker takes the card's own colour unless told otherwise."""
    if card.get("k_color"):
        return card["k_color"]
    c = card.get("color")
    return c if c and c != "plain" else "gray"


def r_card(v, ctx):
    d = dict(v or {})
    color = d.get("color")
    cls = "card " + color if color else "card"
    parts = []
    if d.get("k") is not None:
        style = f"color:var(--{_k_color(d)});" + (resolve_style(d.get("k_style")) or "")
        parts.append(f'  <div class="card-k" style="{style}">{d["k"]}</div>')
    if d.get("t") is not None:
        parts.append(f'  <div class="card-t"{attr("style", d.get("t_style"))}>{d["t"]}</div>')
    if d.get("blocks"):
        # A card whose parts do not fit the k/t/bullets/n shape spells them out
        # in order instead, in the same block vocabulary as a slide body.
        parts += [indent(render_block(b, ctx), 2) for b in d["blocks"]]
    else:
        if d.get("bullets"):
            parts.append(indent(r_bullets({"bullets": d["bullets"], "size": d.get("bullet_size"),
                                           "style": d.get("bullet_style")}, ctx), 2))
        notes = d.get("n")
        if notes is not None:
            notes = notes if isinstance(notes, list) else [notes]
            styles = d.get("n_style")
            styles = styles if isinstance(styles, list) else [styles] * len(notes)
            styles += [None] * (len(notes) - len(styles))
            for note, st in zip(notes, styles):
                parts.append(f'  <div class="card-n"{attr("style", st)}>{note}</div>')
    body = "\n".join(parts)
    return f'<div class="{cls}"{attr("style", d.get("style"))}>\n{body}\n</div>'


def r_cards(v, ctx):
    d = dict(v or {})
    cols = int(d.get("cols", len(d["items"])))
    if cols not in (2, 3, 4):
        raise BuildError(f"cards: cols must be 2, 3 or 4 (got {cols})")
    items = "\n".join(indent(r_card(c, ctx), 2) for c in d["items"])
    return f'<div class="g{cols}"{attr("style", d.get("style"))}>\n{items}\n</div>'


def _cell(c, tag):
    if isinstance(c, str):
        return f"<{tag}>{c}</{tag}>"
    d = dict(c)
    return (f'<{tag}{attr("class", d.get("cls"))}{attr("style", d.get("style"))}>'
            f'{d.get("html", "")}</{tag}>')


def r_table(v, ctx):
    d = dict(v or {})
    out = [f'<table class="t"{attr("style", d.get("style"))}>']
    if d.get("head"):
        out.append("  <thead><tr>" + "".join(_cell(c, "th") for c in d["head"]) + "</tr></thead>")
    out.append("  <tbody>")
    for row in d.get("rows", []):
        out.append("    <tr>")
        out += [f"      {_cell(c, 'td')}" for c in row]
        out.append("    </tr>")
    out += ["  </tbody>", "</table>"]
    return "\n".join(out)


def r_image(v, ctx):
    d = dict(v or {})
    ctx["figures"].add(d["src"])
    return (f'<img src="figures/{d["src"]}"{attr("alt", d.get("alt"))}'
            f'{attr("style", d.get("style"))}>')


def r_figure(v, ctx):
    d = dict(v or {})
    parts = [f'  {r_image({k: d[k] for k in ("src", "alt") if k in d} | ({"style": d["img_style"]} if d.get("img_style") else {}), ctx)}']
    if d.get("caption"):
        parts.append("  " + r_caption({"text": d["caption"], "style": d.get("caption_style")}, ctx))
    body = "\n".join(parts)
    return f'<div class="figwrap"{attr("style", d.get("style"))}>\n{body}\n</div>'


def r_svg(v, ctx):
    d = as_text(v, "file")
    path = ctx["deck"] / "assets" / "diagrams" / d["file"]
    if not path.exists():
        raise BuildError(f"missing diagram: {path}")
    svg = path.read_text(encoding="utf-8").strip()
    if d.get("style"):
        svg = re.sub(r"<svg\b", f'<svg style="{resolve_style(d["style"])}"', svg, count=1)
    return svg


def r_cond(v, ctx):
    spans = []
    for item in v:
        d = as_text(item)
        cls = attr("class", d.get("kind"))
        spans.append(f'<span{cls}>{d["text"]}</span>')
    return '<div class="cond">' + "".join(spans) + "</div>"


def r_box(v, ctx):
    d = dict(v or {})
    inner = "\n".join(indent(render_block(b, ctx), 2) for b in d.get("blocks", []))
    return (f'<div{attr("class", d.get("cls"))}{attr("style", d.get("style"))}>'
            f"\n{inner}\n</div>")


def r_html(v, ctx):
    return v


BLOCKS = {"lead": r_lead, "text": r_text, "note": r_note, "caption": r_caption,
          "bullets": r_bullets, "card": r_card, "cards": r_cards, "table": r_table,
          "figure": r_figure, "image": r_image, "svg": r_svg, "cond": r_cond,
          "box": r_box, "html": r_html}


def render_block(block, ctx):
    if not isinstance(block, dict) or len(block) != 1:
        raise BuildError(f"a block is one mapping with one key; got {block!r}")
    (kind, value), = block.items()
    if kind not in BLOCKS:
        raise BuildError(f"unknown block type {kind!r} — known: {', '.join(sorted(BLOCKS))}")
    return BLOCKS[kind](value, ctx)


# ---------------------------------------------------------------------- slides


def render_slide(s, n, total, refs, ctx):
    out = []
    layout = s.get("layout", "content")

    if layout in ("cover", "part"):
        out.append(f'<div style="{s.get("hero_style", "")}">\n{indent(s["hero"], 2)}\n</div>')
    else:
        if s.get("eyebrow"):
            cls = "eyebrow " + s["eyebrow_color"] if s.get("eyebrow_color") else "eyebrow"
            out.append(f'<div class="{cls}"{attr("style", s.get("eyebrow_style"))}>'
                       f'<span>●</span> {s["eyebrow"]}</div>')
        if s.get("title"):
            out.append(f'<h1 class="stitle">{s["title"]}</h1>')
        style = attr("style", f'height:{s["body_height"]};' if s.get("body_height") else None)
        body = "\n".join(indent(render_block(b, ctx), 2) for b in s.get("blocks", []))
        out.append(f'<div class="body"{style}>\n{body}\n</div>')

    if s.get("cite"):
        lines = []
        for key in s["cite"]:
            if key not in refs:
                raise BuildError(f"slide {n}: unknown reference {key!r} — "
                                 f"add it to references.yaml")
            ctx["cited"].add(key)
            lines.append(f"  <div>{refs[key]}</div>")
        out.append('<div class="cite">\n' + "\n".join(lines) + "\n</div>")

    out.append(f'<div class="foot"><div>{s.get("foot", "")}</div>'
               f'<div class="pg">{n:02d} / {total}</div></div>')

    cls = "slide active" if n == 1 else "slide"
    return (f'    <!-- {n:02d} {s.get("title") or s.get("foot") or ""} -->\n'
            f'    <section class="{cls}">\n'
            + indent("\n".join(out), 6) + f"\n    </section>")


# ----------------------------------------------------------------------- build


def load_deck(name):
    deck = (HERE / name) if not pathlib.Path(name).is_dir() else pathlib.Path(name)
    if not (deck / "deck.yaml").exists():
        raise BuildError(f"no deck.yaml under {deck}")
    meta = yaml.safe_load((deck / "deck.yaml").read_text(encoding="utf-8"))
    refs_file = deck / "references.yaml"
    refs = yaml.safe_load(refs_file.read_text(encoding="utf-8")) if refs_file.exists() else {}

    files = sorted((deck / "slides").glob("*.yaml"))
    if not files:
        raise BuildError(f"no slides under {deck / 'slides'}")
    slides = []
    for f in files:
        try:
            doc = yaml.safe_load(f.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            where = getattr(e, "problem_mark", None)
            at = f" line {where.line + 1}" if where else ""
            raise BuildError(f"{f.name}{at}: {getattr(e, 'problem', e)}") from None
        if doc is None:
            raise BuildError(f"{f.name} is empty")
        doc["_file"] = f.name
        slides.append(doc)
    return deck, meta, refs, slides


def build(name, standalone=False):
    deck, meta, refs, slides = load_deck(name)
    theme = (deck / meta["theme"]).resolve() if meta.get("theme") else HERE / "theme"
    css = (theme / "deck.css").read_text(encoding="utf-8")
    js = (theme / "deck.js").read_text(encoding="utf-8")

    STYLES.clear()
    STYLES.update(meta.get("styles") or {})

    ctx = {"deck": deck, "figures": set(), "cited": set()}
    total = len(slides)
    body = []
    for i, s in enumerate(slides, 1):
        try:
            body.append(render_slide(s, i, total, refs, ctx))
        except BuildError as e:
            raise BuildError(f"{s['_file']}: {e}") from None

    doc = f"""<!DOCTYPE html>
<html lang="{meta.get('lang', 'ko')}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{htmlmod.escape(meta['title'])}</title>
  <!-- Generated by decks/build.py from {deck.name}/. Do not edit; edit the YAML. -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{meta['fonts']}" rel="stylesheet">
  <style>
{indent(css.rstrip(), 4)}
  </style>
</head>
<body>
  <div id="stage">
    <div id="bar"></div>

{chr(10).join(body)}
  </div>
  <div id="hint">{"".join(f"<span>{h}</span>" for h in meta.get("hint", []))}</div>
  <script>
{indent(js.rstrip(), 4)}
  </script>
</body>
</html>
"""

    out_dir = deck / "build"
    out_dir.mkdir(exist_ok=True)
    dst = out_dir / f"{deck.name}.html"
    dst.write_bytes(b"\xef\xbb\xbf" + doc.encode("utf-8"))

    fig_src, fig_dst = deck / "assets" / "figures", out_dir / "figures"
    fig_dst.mkdir(exist_ok=True)
    for f in sorted(ctx["figures"]):
        src = fig_src / f
        if not src.exists():
            raise BuildError(f"missing figure: {src}")
        shutil.copy2(src, fig_dst / f)
    for stale in fig_dst.glob("*"):
        if stale.name not in ctx["figures"]:
            stale.unlink()

    print(f"{dst}  —  {total} slides, {len(ctx['figures'])} figure(s), "
          f"{len(ctx['cited'])} reference(s), {dst.stat().st_size/1024:.0f} KB")

    unused_f = sorted(p.name for p in fig_src.glob("*") if p.name not in ctx["figures"])
    unused_r = sorted(set(refs) - ctx["cited"])
    if unused_f:
        print(f"  unused in assets/figures: {', '.join(unused_f)}")
    if unused_r:
        print(f"  unused in references.yaml: {', '.join(unused_r)}")

    if standalone:
        build_standalone(dst, meta)
    return dst


# ------------------------------------------------------------------ standalone

NOTO_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
NOTO_BLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
KR_FACE, KR_MONO_FACE = 1, 6

BANNER = """    /* ======================================================================
       STANDALONE BUILD — generated, do not hand-edit.
       Rebuild with:  python3 decks/build.py <deck> --standalone
       The typefaces below are Noto Sans CJK KR / Noto Sans Mono CJK KR
       (SIL Open Font License 1.1), subset to the glyphs this deck uses and
       inlined, so the file renders with no network access.
       ====================================================================== */
"""


def subset_woff(path, face, text):
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options

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


def build_standalone(src, meta):
    """The offline twin: one file, no network, no sibling directory.

    A deck is presented on a machine that is not the one it was written on, and
    a missing font or a missing figure is discovered in the room. This carries
    both inside itself.
    """
    html = src.read_text(encoding="utf-8-sig")

    # Every character the deck could render. Taking the whole document rather
    # than only its text nodes over-includes some ASCII the face already has;
    # under-including is the failure that matters, because a missing glyph
    # renders as a blank box with nothing to say why.
    text = "".join(sorted({c for c in html if c.isprintable() or c == " "} | set("  ")))
    print(f"  glyph set: {len(text)} characters")

    rules, total = [], 0
    for family, lo, hi, path, face in [
            ("DeckSans", 100, 500, NOTO_REG, KR_FACE),
            ("DeckSans", 600, 900, NOTO_BLD, KR_FACE),
            ("DeckMono", 100, 500, NOTO_REG, KR_MONO_FACE),
            ("DeckMono", 600, 900, NOTO_BLD, KR_MONO_FACE)]:
        data = subset_woff(path, face, text)
        total += len(data)
        b64 = base64.b64encode(data).decode("ascii")
        rules.append(f"    @font-face {{\n      font-family: '{family}';\n"
                     f"      font-style: normal;\n      font-weight: {lo} {hi};\n"
                     f"      font-display: block;\n"
                     f"      src: url(data:font/woff;base64,{b64}) format('woff');\n    }}\n")
    print(f"  embedded fonts: {total/1024:.0f} KB before base64")

    out = re.sub(r'\n\s*<link rel="preconnect"[^>]*>', "", html)
    out = re.sub(r'\n\s*<link href="https://fonts\.googleapis\.com[^>]*>', "", out)
    out = out.replace(f"<title>{htmlmod.escape(meta['title'])}</title>",
                      f"<title>{htmlmod.escape(meta['title'])} (standalone)</title>", 1)

    img_bytes = 0

    def inline(m):
        nonlocal img_bytes
        f = src.parent / m.group(1)
        if not f.exists():
            raise BuildError(f"missing figure: {f}")
        raw = f.read_bytes()
        img_bytes += len(raw)
        mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                "svg": "image/svg+xml", "webp": "image/webp"}[f.suffix.lstrip(".").lower()]
        return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(raw).decode("ascii"))

    out, n_img = re.subn(r'src="((?!data:|https?:)[^"]+)"', inline, out)
    print(f"  inlined figures: {n_img} file(s), {img_bytes/1024:.0f} KB before base64")

    out = out.replace("  <style>\n", "  <style>\n" + BANNER + "".join(rules), 1)
    out = out.replace(
        '--font-main: "Inter", "Noto Sans KR", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;',
        '--font-main: "DeckSans", "Noto Sans CJK KR", "Noto Sans KR", -apple-system, sans-serif;')
    out = out.replace(
        '--font-mono: "JetBrains Mono", Menlo, Consolas, monospace;',
        '--font-mono: "DeckMono", "Noto Sans Mono CJK KR", Menlo, monospace;')

    dst = src.with_name(src.stem + "-standalone.html")
    dst.write_bytes(b"\xef\xbb\xbf" + out.encode("utf-8"))
    print(f"{dst}  —  {dst.stat().st_size/1024:.0f} KB")

    # Only things the browser fetches on its own count. A citation's <a href>
    # is a link the reader may click, not a subresource, and stays.
    left = sorted(set(re.findall(r'src="(https?://[^"]+)"', out)
                      + re.findall(r'<link[^>]+href="(https?://[^"]+)"', out)
                      + re.findall(r'url\((https?://[^)]+)\)', out)))
    print("  remaining subresource URLs:", left or "none")
    if left:
        raise BuildError(f"standalone still reaches the network: {left}")
    return dst


def watch(name, standalone):
    """Rebuild whenever an input changes, so editing is: save, refresh the tab.

    A failed build prints its reason and keeps waiting — the last good HTML is
    still on disk, so the browser goes on showing the deck rather than a blank
    page while a half-finished edit is being written."""
    import time

    deck = (HERE / name) if not pathlib.Path(name).is_dir() else pathlib.Path(name)
    theme = HERE / "theme"

    def stamp():
        out = {}
        for root in (deck, theme):
            for p in root.rglob("*"):
                if p.is_file() and "build" not in p.relative_to(root).parts:
                    out[p] = p.stat().st_mtime_ns
        return out

    print(f"watching {deck} — ctrl-C to stop")
    last = None
    while True:
        now = stamp()
        if now != last:
            last = now
            try:
                build(name, standalone=standalone)
            except BuildError as e:
                print(f"build failed — {e}", file=sys.stderr)
            except Exception as e:                      # a malformed YAML mid-save
                print(f"build failed — {type(e).__name__}: {e}", file=sys.stderr)
        time.sleep(0.5)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck", nargs="?", default="overthinking",
                    help="deck directory name under decks/ (default: overthinking)")
    ap.add_argument("--standalone", action="store_true",
                    help="also write the offline twin, with fonts and figures inlined")
    ap.add_argument("--watch", action="store_true",
                    help="rebuild on every change to the deck or the theme")
    args = ap.parse_args()
    if args.watch:
        try:
            watch(args.deck, args.standalone)
        except KeyboardInterrupt:
            print()
        return 0
    try:
        build(args.deck, standalone=args.standalone)
    except BuildError as e:
        print(f"build failed — {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
