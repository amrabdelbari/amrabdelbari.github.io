#!/usr/bin/env python3
"""Builds index.html (English), ar/index.html (Arabic) and tr/index.html (Turkish)
from one template, so the three versions always share the same layout and data.

    python3 build/build.py

Edit text in build/i18n.py, publications in PUBS below, then re-run and commit the output.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from i18n import LANGS
from graphics import icon, ART, chart

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://amrabdelbari.github.io"

LINKS = {
    "scholar":  "https://scholar.google.com/citations?user=TgjgGgoAAAAJ&amp;hl={hl}",
    "linkedin": "https://www.linkedin.com/in/amr-abdelbari-935a6542/",
    "neu":      "https://aif.neu.edu.tr/staff/amr-abdelbari/",
    "orcid":    "https://orcid.org/0000-0002-5861-7762",
    "github":   "https://github.com/amro2021",
}

ME = "A. Abdelbari"
PUBS = {
    "journal": [
        (2025, "A. Abdelbari, B. Bilgehan", "Precoding Design for Massive MIMO Channels with Imperfect CSI Based on Supervised Dimension Reduction Method",
         "International Journal of Communication Systems, vol. 38, e70223", "10.1002/dac.70223"),
        (2021, "A. Abdelbari, B. Bilgehan", "PESO: Probabilistic Evaluation of Subspaces Orthogonality for Wideband DOA Estimation",
         "Multidimensional Systems and Signal Processing", "10.1007/s11045-020-00757-6"),
        (2020, "A. Abdelbari, B. Bilgehan", "A Probabilistic-Based Approach for DOA Estimation and Localization of Multiple Sources",
         "International Journal of Communication Systems, vol. 33, e4425", "10.1002/dac.4425"),
        (2020, "H. Haci, A. Abdelbari", "Throughput Enhanced Scheduling (TES) Scheme for Ultra-Dense Networks",
         "International Journal of Communication Systems, vol. 33, e4229", "10.1002/dac.4229"),
        (2019, "B. Bilgehan, A. Abdelbari", "Fast Detection and DOA Estimation of the Unknown Wideband Signal Sources",
         "International Journal of Communication Systems, vol. 32, e3968", "10.1002/dac.3968"),
    ],
    "conf": [
        (2022, "A. Abdelbari", "MDA: Multiple Decentralized Anchors for Hiding Communication Information",
         "ISMSIT 2022, Ankara (IEEE)", "10.1109/ISMSIT56059.2022.9932770"),
        (2022, "A. Abdelbari, B. Bilgehan", "A Novel Precoding Design for Frequency-Selective Massive MIMO Channel",
         "AIoTCs 2022, Nicosia (IEEE), pp. 29–32", "10.1109/AIoTCs58181.2022.00012"),
        (2020, "A. Abdelbari, B. Bilgehan", "A Novel DOA Estimation Method of Several Sources for 5G Networks",
         "ICECCE 2020, Istanbul (IEEE)", "10.1109/ICECCE49384.2020.9179306"),
        (2020, "N. Naser, A. Abdelbari", "Estimation of Global Solar Radiation Using Back Propagation Neural Network: A Case Study Tripoli, Libya",
         "ICECCE 2020, Istanbul (IEEE)", "10.1109/ICECCE49384.2020.9179201"),
        (2019, "A. Abdelbari, H. Haci", "An Opportunistic User Scheduling Scheme for Ultra-Dense Wireless Networks",
         "ELECO 2019, Bursa (IEEE), pp. 1080–1084", "10.23919/ELECO47770.2019.8990469"),
        (2019, "A. Abdelbari, H. Haci", "Fuzzy Logic-Based User Scheduling Scheme for 5G Wireless Networks and Beyond",
         "ICSCCW 2019, Springer AISC vol. 1095", "10.1007/978-3-030-35249-3_55"),
        (2019, "B. Bilgehan, A. Abdelbari", "A Novel DOA Estimation Method for Wideband Sources Based on Fuzzy Systems",
         "ICSCCW 2019, Springer AISC vol. 1095", "10.1007/978-3-030-35249-3_52"),
        (2019, "H. Haci, A. Abdelbari", "A Novel Scheduling Scheme for Ultra-Dense Networks",
         "ISNCC 2019, Istanbul (IEEE)", "10.1109/ISNCC.2019.8909118"),
    ],
    "thesis": [
        (2021, "phd", "On the Localization and Detection of Multiple Signals", "http://docs.neu.edu.tr/library/9451044175.pdf"),
        (2018, "msc", "Direction of Arrival Estimation of Wideband RF Sources", "http://docs.neu.edu.tr/library/6718703723.pdf"),
    ],
}

EXT = 'target="_blank" rel="noopener"'


def pub_html(L):
    out = []
    groups = [("journal", L["pub_journal"]), ("conf", L["pub_conf"])]
    for key, label in groups:
        out.append(f'<div class="pubgroup">{label} · {len(PUBS[key])}</div><div class="pubs">')
        for year, authors, title, venue, doi in PUBS[key]:
            authors = authors.replace(ME, f"<b>{ME}</b>")
            out.append(
                f'<div class="panel pub"><div class="k">{year}</div><div class="en" lang="en">'
                f'<h3><a href="https://doi.org/{doi}" {EXT}>{title}</a></h3>'
                f'<p>{authors} · <i>{venue}</i></p>'
                f'<a class="doi" href="https://doi.org/{doi}" {EXT}>doi:{doi}</a></div></div>')
        out.append("</div>")
    out.append(f'<div class="pubgroup">{L["pub_thesis"]}</div><div class="pubs">')
    for year, kind, title, url in PUBS["thesis"]:
        out.append(
            f'<div class="panel pub"><div class="k">{year}</div><div>'
            f'<h3 class="en" lang="en"><a href="{url}" {EXT}>{title}</a></h3>'
            f'<p>{L["thesis_" + kind]}</p></div></div>')
    out.append("</div>")
    out.append(f'<div class="pubgroup">{L["pub_prep"]}</div><div class="pubs">')
    for k, h, p in L["prep"]:
        out.append(f'<div class="panel pub"><div class="k">{k}</div><div><h3>{h}</h3><p>{p}</p></div></div>')
    out.append("</div>")
    return "\n      ".join(out)


def profiles(L, hl):
    items = [("scholar", "Google Scholar"), ("linkedin", "LinkedIn"), ("orcid", "ORCID"),
             ("neu", L["neu_page"]), ("github", "GitHub")]
    return "".join(f'<a class="btn" href="{LINKS[k].format(hl=hl)}" {EXT}>{icon(k)}{label}</a>' for k, label in items)


def render(code, L):
    up = "" if code == "en" else "../"
    a = up + "assets/"
    url = SITE + "/" + ("" if code == "en" else code + "/")
    langs = "".join(
        f'<a href="{up + ("" if c == "en" else c + "/")}" hreflang="{c}" lang="{c}"'
        + (' aria-current="page"' if c == code else "") + f'>{LANGS[c]["lang_label"]}</a>'
        for c in ("en", "ar", "tr"))
    alt = "".join(f'<link rel="alternate" hreflang="{c}" href="{SITE}/{"" if c == "en" else c + "/"}">\n'
                  for c in ("en", "ar", "tr"))
    feats = "".join(f"<li>{x}</li>" for x in L["feats"])
    stats = "".join(f'<div class="stat"><b>{b}</b><span>{s}</span></div>' for b, s in L["stats"])
    rows = "".join(f"<tr><td>{n}</td><td>{s}</td><td>{o}</td></tr>" for n, s, o in L["rows"])
    lessons = "".join(f'<div class="panel"><h4>{h}</h4><p>{p}</p></div>' for h, p in L["lessons"])
    cards = []
    for c in L["cards"]:
        links = "".join(f'<a href="{u}" {EXT}>{t} ↗</a>' for t, u in c.get("links", []))
        tags = "".join(f'<span class="tag">{t}</span>' for t in c["tags"])
        cards.append(
            f'<div class="panel card">{ART[c["art"]]()}<div class="top"><h3>{c["title"]}</h3><span class="pill {c["pillc"]}">{c["pill"]}</span></div>'
            f'<p>{c["p"]}</p><div class="tags">{tags}</div>' + (f'<div class="links">{links}</div>' if links else "") + "</div>")
    courses = "".join(f"<div class=\"course\"><code>{c}</code><span>{d}</span></div>" for c, d in L["courses"])
    edu = "".join(f"<li><b>{y}</b> · {t}</li>" for y, t in L["edu"])
    tags = "".join(f'<span class="tag">{t}</span>' for t in
                   ["Python", "ArduPilot SITL", "PX4", "MAVLink", "ROS 2", "Gazebo", "FastAPI / uvicorn", "NumPy", "WebGL cockpit", "GitHub Actions"])
    hl = code
    contact_icons = "".join(
        f'<a class="ico" href="{u}" {EXT} title="{t}">{icon(k)}<span class="sr">{t}</span></a>'
        for k, t, u in [("linkedin", "LinkedIn", LINKS["linkedin"]), ("scholar", "Google Scholar", LINKS["scholar"].format(hl=hl)),
                        ("github", "GitHub", LINKS["github"]), ("orcid", "ORCID", LINKS["orcid"]), ("neu", L["neu_page"], LINKS["neu"])])
    band = "".join(f'<div><b data-count>{n}</b><span>{t}</span></div>' for n, t in L["band"])
    timeline = "".join(f'<div class="tl"><b>{y}</b><h4>{h}</h4><p>{p}</p></div>' for y, h, p in L["timeline"])

    return f"""<!doctype html>
<html lang="{code}" dir="{L['dir']}">
<script>document.documentElement.classList.add('js')</script>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{L['title']}</title>
<meta name="description" content="{L['description']}">
<meta property="og:title" content="{L['title']}">
<meta property="og:description" content="{L['og_desc']}">
<meta property="og:image" content="{SITE}/assets/photo.jpg">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#141413">
<link rel="canonical" href="{url}">
{alt}<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%232f6fde'/%3E%3Cpath d='M16 6 L19 15 L27 17 L19 19 L16 26 L13 19 L5 17 L13 15Z' fill='white'/%3E%3C/svg%3E">
<link rel="stylesheet" href="{a}site.css">
</head>
<body>

<header class="bar">
  <div class="wrap">
    <b>{L['name']}</b>
    <span class="pill good opt-pill" title="{L['otw_title']}">● {L['otw']}</span>
    <nav>
      <a href="#arena-project" class="opt">{L['nav_arena']}</a>
      <a href="#projects" class="opt">{L['nav_projects']}</a>
      <a href="#research">{L['nav_research']}</a>
      <a href="#about" class="opt">{L['nav_about']}</a>
      <a href="#contact" class="opt">{L['nav_contact']}</a>
    </nav>
    <a class="btn primary mailbtn opt" href="mailto:amr.abdelbari@neu.edu.tr">{icon('mail')}{L['email_me']}</a>
    <div class="langs" aria-label="Language">{langs}</div>
  </div>
</header>

<main class="wrap">

  <div class="hero">
    <div>
      <div class="who">
        <div class="ring"><div class="avatar" aria-hidden="true">{L['initials']}<img src="{a}photo.jpg" alt="" onerror="this.remove()"></div><span class="dot" title="{L['otw']}"></span></div>
        <div><div class="name">{L['fullname']}</div><div class="kicker">{L['kicker']}</div></div>
      </div>
      <h1>{L['h1']}</h1>
      <p class="lede">{L['lede']}</p>
      <div class="cta">
        <a class="btn primary" href="#arena-project">{L['cta_arena']}</a>
        <a class="btn" href="#research">{L['cta_research']}</a>
      </div>
      <div class="contactbar" id="contact">
        <span class="lbl">{L['contact_label']}</span>
        <span class="mails"><a class="mail" href="mailto:amr.abdelbari@neu.edu.tr">amr.abdelbari@neu.edu.tr</a><a class="mail2" href="mailto:amro410@gmail.com">amro410@gmail.com</a></span>
        {contact_icons}
      </div>
    </div>

    <div class="panel" aria-label="{L['arena_aria']}">
      <div class="h"><span>{L['arena_live']}</span><span class="pill good" id="state">{L['running']}</span><span class="pill" id="clock">00:00</span><span class="grow"></span><span lang="en">sim-lite</span></div>
      <canvas id="arena" dir="ltr" width="640" height="512"></canvas>
      <div class="scoreboard" id="board" dir="ltr"></div>
      <div id="feed" dir="{L['dir']}"></div>
    </div>
  </div>

  <div class="band reveal">{band}</div>

  <section class="block reveal" id="arena-project">
    <div class="sec-head"><span class="num">01</span><h2>{L['arena_title']}</h2><p>{L['arena_sub']}</p></div>
    <div class="flag">
      <div class="panel">
        <h3>{L['arena_h3']}</h3>
        <p>{L['arena_p']}</p>
        <div class="tags">{tags}</div>
        <ul class="feat">{feats}</ul>
<div class="arch">visiting team laptop                 host (Ubuntu)
  auto_team.py / manual_team.py ──HTTP──▶  arena server: referee · scoring · dashboard
  3D cockpit (browser)          ─MAVLink▶  ArduPlane SITL × N  (+ PX4 nodes)
referee browser                 ──HTTP──▶  referee console: start · pause · penalise · eject
guests                          ──/watch▶  3D live view (10 s delay)</div>
      </div>
      <div style="display:grid; gap:14px; align-content:start">
        <div class="stats">{stats}</div>
        <div class="panel" style="padding:16px">
          <div class="h">{L['rehearsal']}</div>
          <table><tr><th>#</th><th>{L['th_setup']}</th><th>{L['th_outcome']}</th></tr>{rows}</table>
        </div>
      </div>
    </div>
    <div class="lessons">{lessons}</div>
  </section>

  <section class="block reveal" id="projects">
    <div class="sec-head"><span class="num">02</span><h2>{L['proj_title']}</h2><p>{L['proj_sub']}</p></div>
    <div class="grid">
      {"".join(cards)}
    </div>
  </section>

  <section class="block reveal" id="research">
    <div class="sec-head"><span class="num">03</span><h2>{L['res_title']}</h2><p>{L['res_sub']}</p></div>
    <div class="rtop">
      <div class="panel"><div class="h">{L['chart_title']}</div>{chart(PUBS)}
        <div class="legend"><span><span class="sw" style="background:var(--accent)"></span>{L['pub_journal']}</span><span><span class="sw" style="background:color-mix(in srgb, var(--accent) 40%, var(--panel))"></span>{L['pub_conf']}</span></div></div>
      <div class="panel">
        <div class="big3"><div><b data-count>{len(PUBS['journal'])}</b><span>{L['pub_journal']}</span></div><div><b data-count>{len(PUBS['conf'])}</b><span>{L['pub_conf']}</span></div><div><b data-count>{len(PUBS['thesis'])}</b><span>{L['pub_thesis']}</span></div></div>
        <div class="profiles">{profiles(L, hl)}</div>
      </div>
    </div>
      {pub_html(L)}
  </section>

  <section class="block reveal" id="about">
    <div class="sec-head"><span class="num">04</span><h2>{L['about_title']}</h2><p>{L['journey_title']}</p></div>
    <div class="timeline">{timeline}</div>
    <div class="two">
      <div class="panel">
        <h3>{L['bg_title']}</h3>
        {L['bg']}
        <h3 style="margin-top:18px">{L['edu_title']}</h3>
        <ul class="edu">{edu}</ul>
      </div>
      <div class="panel">
        <h3>{L['teach_title']}</h3>
        {courses}
      </div>
    </div>
  </section>

</main>

<footer id="footer">
  <div class="wrap">
    <div><b style="color:var(--ink)">{L['name']}</b> · {L['footer_loc']}</div>
    <div class="contact">
      <a class="btn" href="mailto:amr.abdelbari@neu.edu.tr">{L['email']}</a>
      <a class="btn" href="{LINKS['scholar'].format(hl=hl)}" {EXT}>Google Scholar</a>
      <a class="btn" href="{LINKS['linkedin']}" {EXT}>LinkedIn</a>
      <a class="btn" href="{LINKS['github']}" {EXT}>GitHub</a>
    </div>
  </div>
</footer>

<script>window.ARENA_TEXT = {json.dumps(L['arena_js'], ensure_ascii=False)};</script>
<script src="{a}arena.js"></script>
<script src="{a}site.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for code, L in LANGS.items():
        path = os.path.join(ROOT, "index.html" if code == "en" else os.path.join(code, "index.html"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(code, L))
        print("wrote", os.path.relpath(path, ROOT))
