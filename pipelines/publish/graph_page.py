"""The wiki, drawn.

``wiki/_meta/graph.json`` already says what the wiki is shaped like — which
entities exist, which topic covers them, which ones keep turning up together.
This renders that as a page you can look at instead of read.

Three decisions shape it.

*Almost no words.* Every label is hidden until the mark is hovered or focused,
because a concept map with two hundred labels printed on it is a wall of text
and nobody reads walls. What is always visible is shape, size and colour: what
kind of thing it is, how much evidence stands behind it, and which topic it
hangs off.

*Colour is validated, not chosen.* The three entity kinds take three
categorical steps checked with the palette validator over every pair, in both
modes — worst CVD ΔE 8.0 light and 7.0 dark. Both land in the 6–8 band that is
legal only with a second channel, so **kind is also carried by shape**: circle,
square, diamond. Topics are not a fourth colour; they are a different level of
the structure and wear neutral ink. Coral falls under 3:1 on the light surface,
so the relief rule applies and the page ships a table view.

*The layout is deterministic.* Generated files are committed here, so a layout
seeded from a clock or a random number generator would rewrite the page on
every render and fill the history with noise. Positions are seeded from a hash
of each node's id and relaxed for a fixed number of iterations: same input,
same picture, byte for byte.
"""

from __future__ import annotations

import hashlib
import html
import math
from pathlib import Path

from ..common.config import Config
from ..common.log import get
from ..common.schema import utcnow
from ..common.store import read_json, write_text
from . import load_template, render_template

_LOG = get(__name__)

WIDTH, HEIGHT, PAD = 1000.0, 640.0, 46.0
ITERATIONS = 260
# A picture of six hundred nodes is not a picture. Past this, the least-attested
# entities are dropped and the page says how many.
MAX_NODES = 90

# kind -> (css class, svg shape, human label)
_KINDS = {
    "topic": ("k0", "anchor", "Topic"),
    "concept": ("k1", "circle", "Concept"),
    "method": ("k2", "square", "Method"),
    "dataset": ("k3", "diamond", "Dataset"),
}


def _seed(node_id: str) -> tuple[float, float]:
    """A stable starting point, so the same graph always lays out the same way."""
    digest = hashlib.sha1(node_id.encode("utf-8")).digest()
    x = int.from_bytes(digest[0:4], "big") / 0xFFFFFFFF
    y = int.from_bytes(digest[4:8], "big") / 0xFFFFFFFF
    return x, y


def layout(nodes: list[dict], edges: list[dict]) -> dict[str, tuple[float, float]]:
    """Force-directed placement: linked things pull together, everything repels.

    Fruchterman–Reingold with a fixed schedule. Not the prettiest algorithm
    available, but it is short, dependency-free and — given the hashed seed —
    reproducible, which matters more than prettiness for a file under version
    control.
    """
    if not nodes:
        return {}

    ids = [n["id"] for n in nodes]
    index = {node_id: i for i, node_id in enumerate(ids)}
    pos = [list(_seed(node_id)) for node_id in ids]

    links = [
        (index[e["source"]], index[e["target"]])
        for e in edges
        if e.get("source") in index and e.get("target") in index
    ]

    count = len(ids)
    k = math.sqrt(1.0 / count) * 0.9
    temperature = 0.11

    for _ in range(ITERATIONS):
        disp = [[0.0, 0.0] for _ in range(count)]

        for i in range(count):
            for j in range(i + 1, count):
                dx = pos[i][0] - pos[j][0]
                dy = pos[i][1] - pos[j][1]
                dist2 = dx * dx + dy * dy
                if dist2 < 1e-9:
                    # Coincident nodes get a deterministic nudge rather than a
                    # random one, or the layout stops being reproducible.
                    dx, dy, dist2 = (i - j) * 1e-4 or 1e-4, 1e-4, 1e-8
                dist = math.sqrt(dist2)
                force = (k * k) / dist2
                ux, uy = dx / dist, dy / dist
                disp[i][0] += ux * force
                disp[i][1] += uy * force
                disp[j][0] -= ux * force
                disp[j][1] -= uy * force

        for a, b in links:
            dx = pos[a][0] - pos[b][0]
            dy = pos[a][1] - pos[b][1]
            dist = math.hypot(dx, dy) or 1e-6
            force = dist / k
            ux, uy = dx / dist, dy / dist
            disp[a][0] -= ux * force * 0.5
            disp[a][1] -= uy * force * 0.5
            disp[b][0] += ux * force * 0.5
            disp[b][1] += uy * force * 0.5

        for i in range(count):
            dx, dy = disp[i]
            length = math.hypot(dx, dy) or 1e-9
            step = min(length, temperature)
            pos[i][0] = min(1.2, max(-0.2, pos[i][0] + dx / length * step))
            pos[i][1] = min(1.2, max(-0.2, pos[i][1] + dy / length * step))
        temperature *= 0.975

    xs = [p[0] for p in pos]
    ys = [p[1] for p in pos]
    span_x = (max(xs) - min(xs)) or 1.0
    span_y = (max(ys) - min(ys)) or 1.0
    placed: dict[str, tuple[float, float]] = {}
    for node_id, (x, y) in zip(ids, pos):
        placed[node_id] = (
            PAD + (x - min(xs)) / span_x * (WIDTH - 2 * PAD),
            PAD + (y - min(ys)) / span_y * (HEIGHT - 2 * PAD),
        )
    return placed


def _radius(node: dict) -> float:
    """Area follows evidence, with enough spread to be legible.

    A square-root scale is right for area, but over the range these counts
    actually take — two to a dozen sources — it compresses everything into
    three pixels of difference. The multiplier is set so the smallest and
    largest marks differ obviously at a glance.
    """
    if node.get("kind") == "topic":
        return 17.0
    return 7.0 + min(19.0, math.sqrt(max(1, int(node.get("sources", 1)))) * 5.2)


def _shape(node: dict, x: float, y: float, r: float, css: str) -> str:
    kind = node.get("kind", "concept")
    if kind == "method":
        s = r * 0.92
        return (f'<rect class="{css}" x="{x - s:.1f}" y="{y - s:.1f}" '
                f'width="{2 * s:.1f}" height="{2 * s:.1f}" rx="2.5"/>')
    if kind == "dataset":
        d = r * 1.15
        pts = f"{x:.1f},{y - d:.1f} {x + d:.1f},{y:.1f} {x:.1f},{y + d:.1f} {x - d:.1f},{y:.1f}"
        return f'<polygon class="{css}" points="{pts}"/>'
    return f'<circle class="{css}" cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>'


def _svg(nodes: list[dict], edges: list[dict], placed: dict) -> str:
    parts = [
        f'<svg viewBox="0 0 {WIDTH:.0f} {HEIGHT:.0f}" role="img" '
        f'aria-label="Wiki concept map">'
    ]

    radii = {n["id"]: _radius(n) for n in nodes}
    for edge in edges:
        a, b = placed.get(edge["source"]), placed.get(edge["target"])
        if not a or not b:
            continue
        # Trimmed to each mark's edge rather than run to its centre, so a dense
        # graph reads as things joined by lines instead of things with lines
        # driven through them.
        dx, dy = b[0] - a[0], b[1] - a[1]
        span = math.hypot(dx, dy)
        if span < 1e-6:
            continue
        ux, uy = dx / span, dy / span
        ra = radii.get(edge["source"], 8.0) + 2.0
        rb = radii.get(edge["target"], 8.0) + 2.0
        if ra + rb >= span:
            continue
        css = "edge co" if edge.get("type") == "co-occurs" else "edge"
        parts.append(
            f'<line class="{css}" x1="{a[0] + ux * ra:.1f}" y1="{a[1] + uy * ra:.1f}" '
            f'x2="{b[0] - ux * rb:.1f}" y2="{b[1] - uy * rb:.1f}"/>'
        )

    for node in nodes:
        spot = placed.get(node["id"])
        if not spot:
            continue
        x, y = spot
        kind = node.get("kind", "concept")
        css, _, _ = _KINDS.get(kind, _KINDS["concept"])
        r = _radius(node)
        label = html.escape(str(node.get("label", "")))

        parts.append(f'<g class="node" tabindex="0"><title>{label}</title>')
        # A surface-coloured halo under the mark, so overlapping nodes stay
        # separable where the layout could not pull them apart.
        parts.append(_shape(node, x, y, r, "halo"))
        parts.append(_shape(node, x, y, r, f"mark {css}"))
        if kind == "topic":
            parts.append(
                f'<text class="anchor-lbl" x="{x:.1f}" y="{y + r + 14:.1f}">{label}</text>'
            )
        else:
            if node.get("settled"):
                # Where the group has taken a position. A dot on the mark, not
                # a fourth hue: three categorical steps are what validated.
                parts.append(
                    f'<circle class="settled {css}" cx="{x:.1f}" cy="{y:.1f}" r="3.2"/>'
                )
            parts.append(
                f'<circle class="hit" cx="{x:.1f}" cy="{y:.1f}" r="{r + 9:.1f}"/>'
            )
            parts.append(
                f'<text class="lbl" x="{x:.1f}" y="{y - r - 7:.1f}">{label}</text>'
            )
        parts.append("</g>")

    parts.append("</svg>")
    return "\n".join(parts)


def _legend(present: set[str]) -> str:
    order = ["topic", "concept", "method", "dataset"]
    marks = {
        "topic": '<svg width="13" height="13"><circle cx="6.5" cy="6.5" r="5" '
                 'class="mark k0"/></svg>',
        "concept": '<svg width="13" height="13"><circle cx="6.5" cy="6.5" r="5" '
                   'class="mark k1"/></svg>',
        "method": '<svg width="13" height="13"><rect x="1.5" y="1.5" width="10" '
                  'height="10" rx="2" class="mark k2"/></svg>',
        "dataset": '<svg width="13" height="13"><polygon points="6.5,1 12,6.5 6.5,12 1,6.5" '
                   'class="mark k3"/></svg>',
    }
    out = [
        f"<span>{marks[k]}{_KINDS[k][2]}</span>" for k in order if k in present
    ]
    out.append(
        '<span><svg width="13" height="13"><circle cx="6.5" cy="6.5" r="5" '
        'class="mark k0"/><circle cx="6.5" cy="6.5" r="2.4" class="settled k0"/>'
        "</svg>settled</span>"
    )
    out.append('<span style="color:var(--faint)">size = sources</span>')
    return "\n".join(out)


def _table(nodes: list[dict]) -> str:
    swatch = {"topic": "s0", "concept": "s1", "method": "s2", "dataset": "s3"}
    rows = []
    for node in sorted(
        nodes, key=lambda n: (-int(n.get("sources", 0)), str(n.get("label", "")))
    ):
        kind = node.get("kind", "concept")
        sources = node.get("sources")
        rows.append(
            "<tr>"
            f'<td><span class="swatch {swatch.get(kind, "s1")}"></span>'
            f'{html.escape(str(node.get("label", "")))}</td>'
            f"<td>{_KINDS.get(kind, _KINDS['concept'])[2]}</td>"
            f'<td class="n">{"" if sources is None else int(sources)}</td>'
            "</tr>"
        )
    return (
        "<table><thead><tr><th>Name</th><th>Kind</th><th>Sources</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def build(cfg: Config) -> Path | None:
    """Render ``wiki/graph.html`` from the graph the wiki renderer already wrote."""
    source = cfg.layout.wiki_meta / "graph.json"
    graph = read_json(source) or {}
    nodes = [n for n in (graph.get("nodes") or []) if isinstance(n, dict) and n.get("id")]
    edges = [e for e in (graph.get("edges") or []) if isinstance(e, dict)]

    total = len(nodes)
    dropped = 0
    if total > MAX_NODES:
        keep = sorted(
            nodes,
            key=lambda n: (n.get("kind") != "topic", -int(n.get("sources", 0) or 0)),
        )[:MAX_NODES]
        kept_ids = {n["id"] for n in keep}
        nodes = keep
        edges = [
            e for e in edges
            if e.get("source") in kept_ids and e.get("target") in kept_ids
        ]
        dropped = total - len(nodes)

    placed = layout(nodes, edges)
    entities = [n for n in nodes if n.get("kind") != "topic"]
    counts = f"{len(entities)} entities · {len(edges)} links"
    if dropped:
        counts += f" · {dropped} least-attested not shown"

    template = load_template(cfg.layout.template_dirs, "wiki", "graph.html")
    page = render_template(
        template,
        {
            "TITLE": "Wiki map",
            "COUNTS": counts,
            "LEGEND": _legend({str(n.get("kind")) for n in nodes}),
            "SVG": _svg(nodes, edges, placed),
            "TABLE_SUMMARY": f"Table view — {len(nodes)} rows",
            "TABLE": _table(nodes),
            "GENERATED": f"Generated {utcnow()} · hover a mark for its name",
        },
    )

    target = cfg.layout.wiki / "graph.html"
    write_text(target, page)
    _LOG.info("wiki map: %d node(s), %d edge(s)", len(nodes), len(edges))
    return target
