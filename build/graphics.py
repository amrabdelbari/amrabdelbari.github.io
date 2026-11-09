"""Inline SVG: contact icons, animated project illustrations (SMIL) and the publications chart."""
import math, random

ICONS = {
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-7M12 13.5a2.5 2.5 0 0 1 5 0V17"/>',
    "scholar": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v5"/>',
    "github": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6M14 4l-4 16"/>',
    "orcid": '<circle cx="12" cy="12" r="9"/><path d="M9 8v.01M9 11v6M12.5 8v9h1.2a4.5 4.5 0 0 0 0-9z"/>',
    "neu": '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def _svg(body, label):
    return f'<svg class="art" viewBox="0 0 240 120" role="img" aria-label="{label}" dir="ltr">{body}</svg>'


def radar():
    b = ['<g transform="translate(120,114)">']
    b += [f'<path class="ln" d="M{-r},0 A{r},{r} 0 0 1 {r},0"/>' for r in (34, 68, 102)]
    for a in (30, 60, 90, 120, 150):
        x, y = 102 * math.cos(math.radians(a)), -102 * math.sin(math.radians(a))
        b.append(f'<line class="ln" x1="0" y1="0" x2="{x:.1f}" y2="{y:.1f}"/>')
    b.append('<path class="acc" opacity=".28" d="M0,0 L102,0 A102,102 0 0 0 92.4,-43.1 Z">'
             '<animateTransform attributeName="transform" type="rotate" values="0;-155;0" dur="8s" repeatCount="indefinite"/></path>')
    for i, (x, y) in enumerate([(52, -62), (-58, -40), (78, -24), (-20, -84)]):
        b.append(f'<circle class="good" cx="{x}" cy="{y}" r="3.2" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="8s" begin="{i*1.7}s" repeatCount="indefinite"/></circle>')
    b.append('<path class="ink" d="M5,0 L-4,-4 L-2,0 L-4,4Z"><animateMotion path="M-120,-96 L120,-70" dur="9s" repeatCount="indefinite"/></path>')
    b.append('</g>')
    # FM tower
    b.append('<path class="q" d="M20,112 L28,80 L36,112 M23,100 L33,100 M25,90 L31,90"/>'
             '<path class="sacc" opacity=".6" d="M38,76 a10,10 0 0 1 0,12 M42,72 a16,16 0 0 1 0,20"/><text x="16" y="74">FM</text>')
    return _svg("".join(b), "Passive radar sweep")


def qr():
    rnd = random.Random(7)
    n, s, x0, y0 = 13, 7.4, 72, 12
    cells = []
    finder = lambda i, j: any(i - a in range(7) and j - c in range(7) for a, c in ((0, 0), (0, n - 7), (n - 7, 0)))
    for i in range(n):
        for j in range(n):
            x, y = x0 + j * s, y0 + i * s
            if finder(i, j):
                a = 0 if i < 7 else n - 7
                c = 0 if j < 7 else n - 7
                di, dj = i - a, j - c
                on = di in (0, 6) or dj in (0, 6) or (2 <= di <= 4 and 2 <= dj <= 4)
                if on:
                    cells.append(f'<rect class="ink" x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}"/>')
                continue
            dur, beg = rnd.uniform(1.2, 3.2), rnd.uniform(0, 3)
            cls = rnd.choice(["ink", "ink", "acc"])
            cells.append(f'<rect class="{cls}" x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}">'
                         f'<animate attributeName="opacity" values="1;0;1" dur="{dur:.2f}s" begin="{beg:.2f}s" repeatCount="indefinite"/></rect>')
    phones = ('<rect class="q" x="14" y="26" width="38" height="68" rx="6"/><rect class="q" x="188" y="26" width="38" height="68" rx="6"/>'
              '<circle class="q" cx="207" cy="36" r="4"/>'
              '<path class="sacc" stroke-dasharray="3 5" d="M52,60 H68 M172,60 H188">'
              '<animate attributeName="stroke-dashoffset" values="16;0" dur=".8s" repeatCount="indefinite"/></path>')
    return _svg(phones + "".join(cells), "Animated QR code between two phones")


def p2p():
    nodes = [(30, 34), (78, 92), (118, 28), (160, 84), (212, 40), (206, 100), (70, 52)]
    edges = [(0, 6), (6, 2), (6, 1), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (0, 1)]
    b = []
    for a, c in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[c]
        b.append(f'<line class="ln" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="1.6"/>')
    for k, (a, c) in enumerate([(0, 6), (6, 2), (2, 4), (4, 5), (1, 3), (3, 4)]):
        (x1, y1), (x2, y2) = nodes[a], nodes[c]
        cls = "acc" if k % 2 == 0 else "good"
        b.append(f'<circle class="{cls}" r="3"><animateMotion path="M{x1},{y1} L{x2},{y2}" dur="{1.6 + k*0.3:.1f}s" begin="{k*0.4:.1f}s" repeatCount="indefinite"/></circle>')
    for i, (x, y) in enumerate(nodes):
        b.append(f'<circle class="acc" cx="{x}" cy="{y}" r="9" opacity=".18"><animate attributeName="r" values="7;12;7" dur="2.4s" begin="{i*0.35:.2f}s" repeatCount="indefinite"/></circle>'
                 f'<circle class="ink" cx="{x}" cy="{y}" r="4.5"/>')
    return _svg("".join(b), "Peer-to-peer network with moving packets")


def track():
    paths = ["M30,90 C70,10 140,110 210,30 C170,100 90,120 30,90Z",
             "M200,96 C150,40 100,100 60,30 C110,20 170,30 200,96Z",
             "M110,60 C150,20 220,70 170,100 C120,110 70,90 110,60Z"]
    cols = ["acc", "bad", "good"]
    b = []
    for i, (p, c) in enumerate(zip(paths, cols)):
        b.append(f'<path class="ln" stroke-dasharray="2 4" d="{p}"/>')
        b.append(f'<g><animateMotion path="{p}" dur="{7 + i*1.5}s" repeatCount="indefinite"/>'
                 f'<rect x="-10" y="-10" width="20" height="20" rx="2" style="fill:none;stroke:var(--{["accent","bad","good"][i]});stroke-width:1.5"/>'
                 f'<circle class="ink" r="2.6"/><text x="12" y="-7">ID {i+1}</text></g>')
    return _svg("".join(b), "Tracked insects with bounding boxes and IDs")


def npu():
    b = []
    cols, rows, s, g, x0, y0 = 8, 4, 19, 5, 46, 16
    for i in range(rows):
        b.append(f'<path class="sacc" opacity=".5" d="M14,{y0+i*(s+g)+s/2} H38 M32,{y0+i*(s+g)+s/2-4} L38,{y0+i*(s+g)+s/2} L32,{y0+i*(s+g)+s/2+4}"/>')
        for j in range(cols):
            x, y = x0 + j * (s + g), y0 + i * (s + g)
            b.append(f'<rect class="acc" x="{x}" y="{y}" width="{s}" height="{s}" rx="3" opacity=".15">'
                     f'<animate attributeName="opacity" values=".12;.95;.12" dur="2.4s" begin="{(i+j)*0.12:.2f}s" repeatCount="indefinite"/></rect>')
    b.append('<text x="46" y="114">INT8 · 8×4 systolic array</text>')
    return _svg("".join(b), "Systolic array with a diagonal data wave")


def ecg():
    pts, x = ["M0,74"], 0
    while x < 240:
        pts.append(f"L{x+22},74 L{x+27},66 L{x+32},74 L{x+38},74 L{x+42},30 L{x+47},96 L{x+52},74 L{x+64},74 L{x+71},62 L{x+80},74")
        x += 80
    d = " ".join(pts)
    body = (f'<path class="ln" d="M0,74 H240"/>'
            f'<path class="sgood" d="{d}" pathLength="100" stroke-dasharray="100" stroke-width="2">'
            f'<animate attributeName="stroke-dashoffset" values="100;0;0" keyTimes="0;.75;1" dur="3.2s" repeatCount="indefinite"/></path>'
            '<rect class="q" x="162" y="10" width="66" height="26" rx="12"/>'
            '<path class="q" d="M172,36 l-4,7 l10,-7"/>')
    for k in range(3):
        body += f'<circle class="acc" cx="{182 + k*13}" cy="23" r="3.2"><animate attributeName="opacity" values=".2;1;.2" dur="1.2s" begin="{k*0.2:.1f}s" repeatCount="indefinite"/></circle>'
    return _svg(body, "Heartbeat line and chat bubble")


ART = {"radar": radar, "qr": qr, "p2p": p2p, "track": track, "npu": npu, "ecg": ecg}


def chart(pubs):
    years = list(range(2019, 2026))
    J = {y: sum(1 for p in pubs["journal"] if p[0] == y) for y in years}
    C = {y: sum(1 for p in pubs["conf"] if p[0] == y) for y in years}
    W, H, top, bot, left = 480, 200, 14, 26, 10
    mx = max(J[y] + C[y] for y in years) or 1
    unit = (H - top - bot) / mx
    bw = (W - left * 2) / len(years)
    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Publications per year" dir="ltr">']
    for k in range(mx + 1):
        y = H - bot - k * unit
        out.append(f'<line x1="0" x2="{W}" y1="{y:.1f}" y2="{y:.1f}" stroke="var(--line)" stroke-dasharray="{"0" if k == 0 else "2 4"}"/>')
    for i, yr in enumerate(years):
        x = left + i * bw + bw * 0.22
        w = bw * 0.56
        yb = H - bot
        hj, hc = J[yr] * unit, C[yr] * unit
        if hc:
            out.append(f'<rect class="bar" x="{x:.1f}" y="{yb-hj-hc:.1f}" width="{w:.1f}" height="{hc:.1f}" rx="4" fill="color-mix(in srgb, var(--accent) 40%, var(--panel))" style="transition-delay:{i*80+120}ms"/>')
        if hj:
            out.append(f'<rect class="bar" x="{x:.1f}" y="{yb-hj:.1f}" width="{w:.1f}" height="{hj:.1f}" rx="4" fill="var(--accent)" style="transition-delay:{i*80}ms"/>')
        tot = J[yr] + C[yr]
        if tot:
            out.append(f'<text class="v" x="{x+w/2:.1f}" y="{yb-hj-hc-6:.1f}" text-anchor="middle">{tot}</text>')
        out.append(f'<text x="{x+w/2:.1f}" y="{H-8}" text-anchor="middle">{yr}</text>')
    out.append("</svg>")
    return "".join(out)
