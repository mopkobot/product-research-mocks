"""Low-fidelity wireframe primitives (SVG) for Plan UI mocks.

Grayscale, structure-first. No product color, no photography, no emoji.
Numbers and labels are taken from the ticket acceptance criteria.
"""

from html import escape

INK = "#111827"
INK_SOFT = "#374151"
MUTED = "#5F6673"          # secondary text, 5.2:1 on FILL, 4.5:1 on white
FAINT = "#667085"          # small notes, 4.9:1 on white
FAINT_FILL = "#9AA3AF"     # graphical fills only, never text
BORDER = "#D5D9DF"
HAIR = "#E7EAEE"
FILL = "#F2F4F7"
FILL_2 = "#E9ECF1"
SURFACE = "#FFFFFF"
BG = "#F7F8FA"

SANS = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Menlo, DejaVu Sans Mono, monospace"

FRAME_W = 1440
HEADER_H = 56
SIDEBAR_W = 240
CONTENT_X = 272
CONTENT_W = 1136


def txt(x, y, s, size=13, weight=400, fill=INK, anchor="start", family=SANS, ls=0, opacity=None):
    extra = f' letter-spacing="{ls}"' if ls else ""
    if opacity is not None:
        extra += f' opacity="{opacity}"'
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>'
        f"{escape(str(s))}</text>"
    )


def rrect(x, y, w, h, r=10, fill=SURFACE, stroke=BORDER, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ' stroke="none"'
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
        f'fill="{fill}"{stroke_attr}{d}/>'
    )


def line(x1, y1, x2, y2, stroke=HAIR, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
        f'stroke-width="{sw}"{d}/>'
    )


def circle(cx, cy, r, fill=SURFACE, stroke=BORDER, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    stroke_attr = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ' stroke="none"'
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{stroke_attr}{d}/>'


def polyline(points, stroke=INK_SOFT, sw=2, dash=None, fill="none"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    pts = " ".join(f"{x},{y}" for x, y in points)
    return (
        f'<polyline points="{pts}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{d}/>'
    )


def pill(x, y, label, size=10.5, fg=INK_SOFT, bg=FILL, stroke=None, h=20, pad=8):
    w = max(28, int(len(str(label)) * size * 0.58) + pad * 2)
    out = rrect(x, y - h + 5, w, h, r=10, fill=bg, stroke=stroke)
    out += txt(x + w / 2, y, label, size=size, weight=600, fill=fg, anchor="middle")
    return out, w


def btn(x, y, label, w=None, h=34, variant="primary", size=12.5):
    w = w or max(84, int(len(label) * size * 0.58) + 28)
    if variant == "primary":
        fill, fg, stroke = INK, "#FFFFFF", None
    elif variant == "secondary":
        fill, fg, stroke = SURFACE, INK, BORDER
    else:  # ghost
        fill, fg, stroke = "none", INK_SOFT, None
    out = rrect(x, y, w, h, r=8, fill=fill, stroke=stroke)
    out += txt(x + w / 2, y + h / 2 + 4.5, label, size=size, weight=600, fill=fg, anchor="middle")
    return out, w


def field(x, y, w, label, value=None, hint=None, placeholder=False, h=36, focus=False, error=None):
    out = txt(x, y, label, size=10.5, weight=600, fill=MUTED, ls=0.4)
    box_y = y + 8
    stroke = INK if focus else (BORDER if not error else FAINT)
    out += rrect(x, box_y, w, h, r=8, fill=SURFACE, stroke=stroke, sw=2 if focus else 1)
    if value:
        out += txt(x + 12, box_y + h / 2 + 4.5, value, size=13, weight=400,
                   fill=MUTED if placeholder else INK,
                   family=MONO if placeholder is False and any(c.isdigit() for c in value) else SANS)
    if hint:
        out += txt(x, box_y + h + 15, hint, size=10.5, fill=FAINT)
    if error:
        out += txt(x, box_y + h + 15, error, size=10.5, weight=600, fill=INK_SOFT)
    return out, box_y + h


def select(x, y, w, label, value, h=36, chip=None):
    out = txt(x, y, label, size=10.5, weight=600, fill=MUTED, ls=0.4)
    out += rrect(x, y + 8, w, h, r=8, fill=SURFACE, stroke=BORDER)
    out += txt(x + 12, y + 8 + h / 2 + 4.5, value, size=13)
    out += polyline([(x + w - 22, y + h / 2 + 2), (x + w - 16, y + h / 2 + 8), (x + w - 10, y + h / 2 + 2)],
                    stroke=MUTED, sw=1.5)
    if chip:
        out += txt(x + w - 34, y + h / 2 + 4, chip, size=10.5, fill=FAINT, anchor="end")
    return out, y + 8 + h


def tabs(x, y, labels, active=0, w=None, h=34, size=12.5):
    out = ""
    widths = []
    cx = x
    for i, lab in enumerate(labels):
        tw = max(76, int(len(lab) * size * 0.6) + 30)
        widths.append(tw)
        active_i = i == active
        out += txt(cx + tw / 2, y + h / 2 + 4.5, lab, size=size,
                   weight=600 if active_i else 400,
                   fill=INK if active_i else MUTED, anchor="middle")
        if active_i:
            out += rrect(cx + 10, y + h - 3, tw - 20, 3, r=2, fill=INK, stroke=None)
        cx += tw
    out += line(x, y + h, cx, y + h, stroke=HAIR)
    return out, cx - x


def toggle(x, y, on=True, label=None, size=12.5):
    w, h = 38, 21
    out = rrect(x, y, w, h, r=h / 2, fill=INK if on else FILL_2, stroke=None)
    out += circle(x + (w - 17 if on else 17), y + h / 2, 8, fill=SURFACE, stroke=None)
    if label:
        out += txt(x + w + 10, y + h / 2 + 4.5, label, size=size, fill=INK)
    return out


def table(x, y, w, cols, rows, row_h=38, header_h=32, mono_cols=(), align=None, highlight=None):
    """cols: list of (label, width_px). rows: list of lists (str)."""
    total = sum(c[1] for c in cols)
    avail = w - 32
    if total > avail:
        scale = avail / total
        cols = [(label, cw * scale) for label, cw in cols]
    out = rrect(x, y, w, header_h + row_h * len(rows), r=10, fill=SURFACE, stroke=BORDER)
    out += rrect(x, y, w, header_h, r=10, fill=FILL, stroke=None)
    out += rrect(x, y + header_h - 10, w, 10, r=0, fill=FILL, stroke=None)
    cx = x + 16
    for i, (label, cw) in enumerate(cols):
        a = (align or ["start"] * len(cols))[i]
        tx = cx if a == "start" else cx + cw - 8
        out += txt(tx, y + 21, label.upper(), size=10, weight=700, fill=MUTED,
                   anchor=a, ls=0.5)
        cx += cw
    for r_i, row in enumerate(rows):
        ry = y + header_h + r_i * row_h
        if highlight is not None and r_i == highlight:
            out += rrect(x + 1, ry, w - 2, row_h, r=0, fill=FILL, stroke=None)
        if r_i:
            out += line(x, ry, x + w, ry, stroke=HAIR)
        cx = x + 16
        for c_i, cell in enumerate(row):
            a = (align or ["start"] * len(cols))[c_i]
            tx = cx if a == "start" else cx + cols[c_i][1] - 8
            fam = MONO if cell in mono_cols or (isinstance(cell, str) and cell.startswith("$")) else SANS
            out += txt(tx, ry + row_h / 2 + 4.5, cell, size=12.5,
                       weight=500 if fam == MONO else 400, fill=INK if a == "start" else INK_SOFT,
                       anchor=a, family=fam)
            cx += cols[c_i][1]
    return out, y + header_h + row_h * len(rows)


def card(x, y, w, h, title=None, sub=None, pad=18, fill=SURFACE, dash=None):
    out = rrect(x, y, w, h, r=12, fill=fill, stroke=BORDER, dash=dash)
    top = y + pad
    if title:
        out += txt(x + pad, y + pad + 12, title, size=14, weight=600, fill=INK)
        top = y + pad + 24
    if sub:
        out += txt(x + pad, top + 12, sub, size=11.5, fill=MUTED)
        top += 18
    return out, x + pad, top + 6, w - 2 * pad


def kpi(x, y, w, label, value, delta=None, h=92, mono=True, hint=None, delta_kind="neutral"):
    out = rrect(x, y, w, h, r=12, fill=SURFACE, stroke=BORDER)
    out += txt(x + 16, y + 24, label.upper(), size=10.5, weight=700, fill=MUTED, ls=0.6)
    out += txt(x + 16, y + 58, value, size=22, weight=600, fill=INK,
               family=MONO if mono else SANS)
    if delta:
        kind_fill = INK_SOFT if delta_kind == "neutral" else INK
        out += txt(x + 16, y + 78, delta, size=11, weight=600, fill=kind_fill)
    if hint:
        out += txt(x + w - 16, y + 24, hint, size=10.5, fill=FAINT, anchor="end")
    return out


def line_chart(x, y, w, h, series, x_labels=None, y_max=None, milestone_x=None,
               legend=True, y_ticks=4, band=None):
    """series: list of dicts {name, values, dash, area, color}."""
    out = ""
    values = [v for s in series for v in s["values"] if v is not None]
    y_max = y_max or (max(values) * 1.15 if values else 1)
    plot_x, plot_y = x + 46, y + (24 if legend else 4)
    plot_w, plot_h = w - 46 - 10, h - (24 if legend else 4) - 26
    for i in range(y_ticks + 1):
        gy = plot_y + plot_h - plot_h * i / y_ticks
        out += line(plot_x, gy, plot_x + plot_w, gy, stroke=HAIR)
        out += txt(plot_x - 8, gy + 4, compact(y_max * i / y_ticks), size=9.5,
                   fill=FAINT, anchor="end", family=MONO)
    if band:
        lo, hi = band
        pts_top = [(plot_x + plot_w * i / (len(hi) - 1), plot_y + plot_h - plot_h * v / y_max) for i, v in enumerate(hi)]
        pts_bot = [(plot_x + plot_w * i / (len(lo) - 1), plot_y + plot_h - plot_h * v / y_max) for i, v in enumerate(reversed(lo))]
        pts = pts_top + pts_bot
        d = " ".join(f"{px},{py}" for px, py in pts)
        out += f'<polygon points="{d}" fill="{FILL_2}" stroke="none"/>'
    n = max(len(s["values"]) for s in series)
    for s in series:
        pts = []
        for i, v in enumerate(s["values"]):
            if v is None:
                continue
            pts.append((plot_x + plot_w * i / (n - 1), plot_y + plot_h - plot_h * v / y_max))
        if s.get("area") and pts:
            d = " ".join(f"{px},{py}" for px, py in pts)
            d += f" {pts[-1][0]},{plot_y + plot_h} {pts[0][0]},{plot_y + plot_h}"
            out += f'<polygon points="{d}" fill="{FILL}" stroke="none"/>'
        out += polyline(pts, stroke=INK if not s.get("dash") else MUTED, sw=2.2,
                        dash=s.get("dash"))
    if milestone_x is not None:
        for mx, mlabel in milestone_x:
            px = plot_x + plot_w * mx / (n - 1)
            out += line(px, plot_y, px, plot_y + plot_h, stroke=FAINT_FILL, sw=1, dash="3 3")
            out += circle(px, plot_y, 4, fill=INK, stroke=None)
            out += txt(px, plot_y - 8, mlabel, size=9.5, weight=600, fill=INK_SOFT, anchor="middle")
    if x_labels:
        for i, lab in enumerate(x_labels):
            if i % max(1, len(x_labels) // 7) and i != len(x_labels) - 1:
                continue
            px = plot_x + plot_w * i / (len(x_labels) - 1)
            out += txt(px, plot_y + plot_h + 16, lab, size=9.5, fill=FAINT, anchor="middle", family=MONO)
    if legend:
        lx = x + 46
        for s in series:
            out += line(lx, y + 10, lx + 16, y + 10, stroke=INK if not s.get("dash") else MUTED,
                        sw=2, dash=s.get("dash"))
            out += txt(lx + 22, y + 14, s["name"], size=10.5, fill=MUTED)
            lx += 24 + int(len(s["name"]) * 6.2) + 16
    return out


def para(x, y, text, width, size=11.5, fill=MUTED, lh=16, weight=400, max_lines=3):
    limit = int(width / (size * 0.52))
    words, lines, current = text.split(), [], ""
    for word in words:
        if len(current) + len(word) + 1 > limit and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(0, limit - 1)] + "…"
    return "".join(
        txt(x, y + i * lh, ln, size=size, weight=weight, fill=fill) for i, ln in enumerate(lines)
    )


def stacked_bars(x, y, w, h, categories, series, y_max=None, y_ticks=3, legend=True):
    """series: list of (name, [values], shade). Bars stack bottom-up per category."""
    out = ""
    totals = [sum(s[1][i] for s in series) for i in range(len(categories))]
    y_max = y_max or (max(totals) * 1.12 if totals else 1)
    plot_x = x + 46
    plot_y = y + (24 if legend else 4)
    plot_w = w - 56
    plot_h = h - (24 if legend else 4) - 26
    for i in range(y_ticks + 1):
        gy = plot_y + plot_h - plot_h * i / y_ticks
        out += line(plot_x, gy, plot_x + plot_w, gy, stroke=HAIR)
        out += txt(plot_x - 8, gy + 4, compact(y_max * i / y_ticks), size=9.5,
                   fill=FAINT, anchor="end", family=MONO)
    slot = plot_w / len(categories)
    bar_w = min(64, slot * 0.52)
    for i, cat in enumerate(categories):
        bx = plot_x + slot * i + (slot - bar_w) / 2
        base = plot_y + plot_h
        for name, values, shade in series:
            value = values[i]
            if value <= 0:
                continue
            bh = plot_h * value / y_max
            base -= bh
            out += rrect(bx, base, bar_w, bh, r=2, fill=shade, stroke=None)
        out += txt(bx + bar_w / 2, plot_y + plot_h + 16, cat, size=9.5, fill=FAINT,
                   anchor="middle", family=MONO)
    if legend:
        lx = plot_x
        for name, values, shade in series:
            out += rrect(lx, y + 5, 10, 10, r=2, fill=shade, stroke=None)
            out += txt(lx + 16, y + 14, name, size=10.5, fill=MUTED)
            lx += 22 + int(len(name) * 5.9) + 14
    return out


def compact(v):
    v = float(v)
    if abs(v) >= 1_000_000:
        return f"${v/1_000_000:.1f}M"
    if abs(v) >= 1_000:
        return f"${v/1_000:.0f}K"
    return f"${v:.0f}"


def bars(x, y, w, rows, row_h=34, gap=10, max_val=None, label_w=190, value_w=96):
    """rows: list of (label, value, note)."""
    out = ""
    max_val = max_val or max(r[1] for r in rows) or 1
    for i, (label, value, note) in enumerate(rows):
        ry = y + i * (row_h + gap)
        out += txt(x, ry + row_h / 2 + 4, label, size=12)
        bw = w - label_w - value_w
        out += rrect(x + label_w, ry + 6, bw, row_h - 12, r=4, fill=FILL, stroke=None)
        out += rrect(x + label_w, ry + 6, max(3, bw * value / max_val), row_h - 12, r=4, fill=INK_SOFT, stroke=None)
        out += txt(x + label_w + bw + 10, ry + row_h / 2 + 4, note or f"{value:,.0f}",
                   size=11.5, fill=INK, family=MONO)
    return out


def donut(cx, cy, r, segments, thickness=18, center_top=None, center_bottom=None):
    """segments: list of (label, fraction). Fills from 12 o'clock clockwise with grays."""
    out = circle(cx, cy, r, fill="none", stroke=HAIR, sw=thickness)
    shades = [INK, MUTED, FAINT_FILL, FILL_2]
    start = -90.0
    import math
    for i, (label, frac) in enumerate(segments):
        if frac <= 0:
            continue
        end = start + 360 * frac
        large = 1 if (end - start) > 180 else 0
        x1 = cx + r * math.cos(math.radians(start))
        y1 = cy + r * math.sin(math.radians(start))
        x2 = cx + r * math.cos(math.radians(end))
        y2 = cy + r * math.sin(math.radians(end))
        out += (
            f'<path d="M {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f}" '
            f'fill="none" stroke="{shades[i % len(shades)]}" stroke-width="{thickness}" '
            f'stroke-linecap="butt"/>'
        )
        start = end
    if center_top:
        out += txt(cx, cy + 2, center_top, size=18, weight=600, anchor="middle", family=MONO)
    if center_bottom:
        out += txt(cx, cy + 20, center_bottom, size=10.5, fill=MUTED, anchor="middle")
    return out


def gauge(x, y, r, fraction, label, value, note=None, start=200, end=340):
    import math
    out = ""
    steps = 40
    for i in range(steps):
        a0 = start + (end - start) * i / steps
        a1 = start + (end - start) * (i + 1) / steps
        on = (i / steps) < fraction
        x1, y1 = x + r * math.cos(math.radians(a0)), y + r * math.sin(math.radians(a0))
        x2, y2 = x + r * math.cos(math.radians(a1)), y + r * math.sin(math.radians(a1))
        out += line(x1, y1, x2, y2, stroke=INK if on else HAIR, sw=8)
    out += txt(x, y + 34, value, size=21, weight=600, anchor="middle", family=MONO)
    out += txt(x, y + 52, label, size=11, fill=MUTED, anchor="middle")
    if note:
        out += txt(x, y + 68, note, size=10, fill=FAINT, anchor="middle")
    return out


def note_marker(n, x, y, on_dark=False):
    fill = SURFACE if on_dark else INK
    fg = INK if on_dark else "#FFFFFF"
    return circle(x, y, 11, fill=fill, stroke=None) + txt(x, y + 4, str(n), size=11,
                                                          weight=700, fill=fg, anchor="middle")


def warn(text, x, y, w, tone="warn", title=None):
    out = rrect(x, y, w, 46, r=8, fill=FILL, stroke=BORDER, dash="4 4")
    out += txt(x + 16, y + 21 if not title else y + 30, "!" if tone == "warn" else "i",
               size=12, weight=700, fill=INK_SOFT)
    # wrap by approximate character width, max two lines
    limit = int((w - 76) / 6.4)
    words, lines, current = text.split(), [], ""
    for word in words:
        if len(current) + len(word) + 1 > limit and current:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    if len(lines) > 2:
        lines = lines[:2]
        lines[1] = lines[1][: max(0, limit - 1)] + "…"
    if title:
        out += txt(x + 34, y + 19, title, size=12, weight=600, fill=INK)
        out += txt(x + 34, y + 36, lines[0], size=11, fill=MUTED)
        return out
    if len(lines) == 1:
        out += txt(x + 34, y + 27, lines[0], size=11.5, fill=INK_SOFT)
    else:
        out += txt(x + 34, y + 20, lines[0], size=11.5, fill=INK_SOFT)
        out += txt(x + 34, y + 35, lines[1], size=11.5, fill=INK_SOFT)
    return out


def empty(x, y, w, h, title, body, cta=None):
    out = rrect(x, y, w, h, r=12, fill=SURFACE, stroke=BORDER, dash="6 5")
    out += circle(x + w / 2, y + h / 2 - 34, 22, fill=FILL, stroke=BORDER, dash="4 3")
    out += txt(x + w / 2, y + h / 2 + 6, title, size=14, weight=600, anchor="middle")
    out += txt(x + w / 2, y + h / 2 + 26, body, size=11.5, fill=MUTED, anchor="middle")
    if cta:
        bw = max(96, int(len(cta) * 7.2) + 28)
        out += rrect(x + w / 2 - bw / 2, y + h / 2 + 40, bw, 32, r=8, fill=SURFACE, stroke=BORDER)
        out += txt(x + w / 2, y + h / 2 + 60, cta, size=12, weight=600, anchor="middle")
    return out


def sidebar(y_top, active, height):
    out = rrect(0, y_top, SIDEBAR_W, height, r=0, fill=SURFACE, stroke=None)
    out += line(SIDEBAR_W, y_top, SIDEBAR_W, y_top + height, stroke=BORDER)
    groups = [
        (None, ["Dashboard", "Current Finances", "Plans"]),
        ("PLAN", ["Income", "Expenses & flows", "Assets & debts", "Milestones", "Strategy", "Estate"]),
        ("ANALYZE", ["Projection", "Tax analytics", "Monte Carlo", "Compare", "Snapshots"]),
        ("ACCOUNT", ["Data & sharing", "Settings"]),
    ]
    y = y_top + 18
    for label, items in groups:
        if label:
            out += txt(20, y + 10, label, size=9.5, weight=700, fill=FAINT, ls=0.8)
            y += 22
        for item in items:
            is_active = item == active
            if is_active:
                out += rrect(10, y - 12, SIDEBAR_W - 20, 32, r=7, fill=FILL, stroke=None)
            icx, icy = 26, y - 12 + 15
            out += rrect(icx - 6, icy - 6, 12, 12, r=3, fill=SURFACE if not is_active else INK,
                         stroke=BORDER if not is_active else None)
            out += txt(44, y + 2, item, size=12.5, weight=600 if is_active else 400,
                       fill=INK if is_active else INK_SOFT)
            y += 34
        y += 10
    return out


def chrome(active, plan_name="Plan For Retirement", plan_badge="From current finances",
           premium=False, height=820, run_label="Run plan"):
    out = rrect(0, 0, FRAME_W, HEADER_H, r=0, fill=SURFACE, stroke=None)
    out += line(0, HEADER_H, FRAME_W, HEADER_H, stroke=BORDER)
    out += rrect(20, 18, 20, 20, r=5, fill=INK, stroke=None)
    out += txt(48, 33, "PLAN", size=13, weight=700, ls=2.4)
    out += line(SIDEBAR_W, 0, SIDEBAR_W, HEADER_H, stroke=BORDER)
    out += rrect(264, 12, 300, 32, r=8, fill=SURFACE, stroke=BORDER)
    out += txt(278, 33, plan_name, size=12.5, weight=600)
    out += txt(544, 33, "▾", size=11, fill=MUTED)
    badge, bw = pill(580, 34, plan_badge, fg=INK_SOFT)
    out += badge
    x = FRAME_W - 24
    out += circle(x - 8, HEADER_H / 2, 14, fill=FILL, stroke=BORDER)
    out += txt(x - 8, HEADER_H / 2 + 4, "MO", size=10.5, weight=700, anchor="middle", fill=INK_SOFT)
    x -= 44
    out += circle(x - 8, HEADER_H / 2, 14, fill=SURFACE, stroke=BORDER)
    out += txt(x - 8, HEADER_H / 2 + 4, "?", size=11, weight=700, anchor="middle", fill=MUTED)
    x -= 48
    b, bw = btn(x - 96, 13, run_label, w=96, h=30)
    out += b
    x -= 108
    if premium:
        badge, bw = pill(x - 74, 34, "PREMIUM", fg="#FFFFFF", bg=INK)
        out += badge
    out += sidebar(HEADER_H, active, height - HEADER_H)
    return out


class Page:
    def __init__(self, number, title, subtitle, active, crumb="Plans / Plan For Retirement",
                 frame_h=840, plan_badge="From current finances", premium=False,
                 actions=None, run_label="Run plan"):
        self.number = number
        self.title = title
        self.parts = []
        self.frame_h = frame_h
        self.parts.append(chrome(active, plan_badge=plan_badge, premium=premium,
                                 height=frame_h, run_label=run_label))
        self.parts.append(txt(CONTENT_X, 96, crumb.upper(), size=9.5, weight=700,
                              fill=FAINT, ls=0.7))
        self.parts.append(txt(CONTENT_X, 124, title, size=25, weight=600))
        self.parts.append(txt(CONTENT_X, 146, subtitle, size=12.5, fill=MUTED))
        if actions:
            widths = 0
            for a in actions:
                widths += len(a) * 7.0 + 40
            ax = CONTENT_X + CONTENT_W - widths + 8
            for i, a in enumerate(actions):
                variant = "primary" if i == len(actions) - 1 else "secondary"
                b, bw = btn(ax, 100, a, variant=variant)
                self.parts.append(b)
                ax += bw + 10
        self.y = 176

    # primitive passthroughs
    def add(self, s):
        self.parts.append(s)
        return self

    def txt(self, *a, **k):
        self.parts.append(txt(*a, **k))
        return self

    def card(self, x, y, w, h, title=None, sub=None, pad=18, fill=SURFACE, dash=None):
        s, ix, iy, iw = card(x, y, w, h, title, sub, pad, fill, dash)
        self.parts.append(s)
        return ix, iy, iw

    def block(self, title, y=None, x=CONTENT_X, w=CONTENT_W, h=180, sub=None, fill=SURFACE):
        y = self.y if y is None else y
        s, ix, iy, iw = card(x, y, w, h, title, sub, fill=fill)
        self.parts.append(s)
        self.y = y + h + 16
        return ix, iy, iw

    def note(self, n, x, y):
        self.parts.append(note_marker(n, x, y))
        return self

    def markers(self, items):
        y_last = -100
        for n, x, y in items:
            ny = y
            if ny - y_last < 28:
                ny = y_last + 28
            y_last = ny
            self.parts.append(note_marker(n, CONTENT_X - 24, ny))
        return self

    def footer(self, notes, height=None, start_y=None):
        y0 = start_y or (self.frame_h + 24)
        self.parts.append(txt(CONTENT_X, y0 + 4, "ANNOTATIONS", size=10, weight=700,
                              fill=MUTED, ls=0.9))
        y = y0 + 28
        for n, text in notes:
            self.parts.append(note_marker(n, CONTENT_X + 11, y - 4))
            # wrap to two lines at ~108 chars
            words, line_out, lines = text.split(), "", []
            for word in words:
                if len(line_out) + len(word) + 1 > 116:
                    lines.append(line_out)
                    line_out = word
                else:
                    line_out = f"{line_out} {word}".strip()
            lines.append(line_out)
            for i, ln in enumerate(lines):
                self.parts.append(txt(CONTENT_X + 32, y + i * 17, ln, size=11.5, fill=INK_SOFT))
            y += 17 * len(lines) + 12
        self.total_h = y + 24
        return self

    def svg(self):
        h = self.total_h
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{FRAME_W}" height="{h}" '
            f'viewBox="0 0 {FRAME_W} {h}" role="img" aria-label="{escape(self.title)} wireframe">'
            f'<title>{escape(self.title)} wireframe</title>'
            f'<rect width="{FRAME_W}" height="{h}" fill="{BG}"/>'
            + "".join(self.parts)
            + "</svg>"
        )
