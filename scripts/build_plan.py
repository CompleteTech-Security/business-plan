"""Render business-plan.md as a self-contained, brand-neutral HTML page.

Uses neutral blue accent tokens (light and dark). The output has no remote resources, so it can be opened
offline or printed to PDF.
"""

import base64
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
TITLE = "AI-Era Technology Services Business Plan"
SUBTITLE = "An open template: security assessment, managed services, and AI business automation"
TAGLINE = "Open template. Adapt it, credit it, build your own."
META = [
    ("Date", "October 29, 2026"),
    ("Worked example", '<a href="https://github.com/orgs/CompleteTech-Security/repositories">CompleteTech-Security</a> tool portfolio'),
    ("Example market", "Local B2B, expanding regionally"),
    ("Planning period", "12 months"),
    ("License", '<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> (brand assets excluded)'),
]
STATS = [
    ("51", "Example tool repositories"),
    ("5", "Revenue streams"),
    ("12", "Month roadmap"),
    ("$53,570", "Illustrative Year 1 revenue (6 clients/mo)"),
    ("$6,029", "Illustrative year-end MRR"),
]

CSS = """
:root{--accent:#1E3A8A;--sky:#0B7BEA;--gold:#F5B800;--bg:#F4F7FB;--surface:#FFFFFF;--surface-2:#EEF2FF;--ink:#0F172A;--ink-2:#1E293B;--ink-3:#64748B;--line:#E2E8F0;--line-2:#CBD5E1;--link:#1E3A8A;--shadow:0 1px 2px rgba(15,23,42,.06),0 8px 24px rgba(30,58,138,.08)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--accent:#7C9CF0;--sky:#4DA3FF;--gold:#FFC83D;--bg:#0B1220;--surface:#16213A;--surface-2:#1C2A4A;--ink:#F1F5F9;--ink-2:#CBD5E1;--ink-3:#94A3B8;--line:#26334F;--line-2:#3A4A6B;--link:#9DB6F7;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35)}}
:root[data-theme="dark"]{--accent:#7C9CF0;--sky:#4DA3FF;--gold:#FFC83D;--bg:#0B1220;--surface:#16213A;--surface-2:#1C2A4A;--ink:#F1F5F9;--ink-2:#CBD5E1;--ink-3:#94A3B8;--line:#26334F;--line-2:#3A4A6B;--link:#9DB6F7;--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35)}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--ink-2);font:16px/1.6 "Segoe UI",Arial,Helvetica,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--link);text-underline-offset:3px}
.wrap{max-width:900px;margin:0 auto;padding:0 20px}

/* top bar */
.bar{position:fixed;inset:0 0 auto 0;z-index:20;height:52px;display:flex;align-items:center;justify-content:space-between;padding:0 18px;background:color-mix(in srgb,var(--surface) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);transform:translateY(-100%);transition:transform .25s}
.bar.on{transform:none}
.bar b{font-size:.78rem;letter-spacing:.16em;color:var(--accent)}
.bar i{position:absolute;left:0;bottom:-1px;height:3px;width:0;background:linear-gradient(90deg,var(--gold),var(--sky))}
.theme{padding:6px 14px;background:var(--surface);color:var(--ink);border:1px solid var(--line-2);border-radius:999px;font:600 .78rem "Segoe UI",Arial,sans-serif;cursor:pointer}
.theme.float{position:fixed;top:14px;right:16px;z-index:21;background:rgba(255,255,255,.14);color:#fff;border-color:rgba(255,255,255,.35)}
.bar.on~.theme.float{display:none}

/* hero */
.hero{position:relative;overflow:hidden;color:#fff;padding:44px 0 96px;background:radial-gradient(circle at 85% 15%,rgba(11,123,234,.55),transparent 45%),linear-gradient(135deg,#0A1740 0%,#1E3A8A 60%,#0B5BD3 100%)}
.hero::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.14) 1.2px,transparent 1.4px);background-size:26px 26px;mask-image:linear-gradient(120deg,transparent 30%,#000 100%);-webkit-mask-image:linear-gradient(120deg,transparent 30%,#000 100%)}
.hero::after{content:"";position:absolute;left:0;right:0;bottom:0;height:5px;background:linear-gradient(90deg,var(--gold),#F5B800 18%,#0B7BEA 60%,#38A0FF)}
.hero .wrap{position:relative;display:grid;grid-template-columns:1fr;gap:32px;align-items:center}
.eyebrow{margin:0 0 12px;font-size:.78rem;letter-spacing:.22em;font-weight:700;color:var(--gold)}
h1.title{margin:0;font-size:clamp(2.1rem,5.4vw,3.4rem);line-height:1.08;letter-spacing:-.01em;color:#fff}
.subtitle{margin:12px 0 0;font-size:1.15rem;line-height:1.5;color:rgba(255,255,255,.82);max-width:34ch}
.tag{display:inline-block;margin-top:18px;padding:7px 16px;border:1px solid rgba(255,255,255,.35);border-radius:999px;font-size:.88rem;letter-spacing:.04em;background:rgba(255,255,255,.08)}
.logo-card{padding:16px;background:#F8FAFC;border-radius:20px;box-shadow:0 20px 50px rgba(2,8,32,.45)}
.logo-card img{display:block;width:100%;height:auto}
.hero .wrap.cw{display:block}
.chips{position:relative;display:flex;flex-wrap:wrap;gap:8px;margin-top:28px}
.chip{flex:1 1 auto;padding:8px 14px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.22);border-radius:10px;font-size:.84rem;line-height:1.35}
.chip span{display:block;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.6)}
.chip a{color:#fff}

/* stats */
.stats{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin:-54px 0 0;position:relative}
.stat{padding:14px 10px;text-align:center;background:var(--surface);border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:12px;box-shadow:var(--shadow)}
.stat:nth-child(even){border-top-color:var(--sky)}
.stat b{display:block;font-size:1.65rem;line-height:1.1;color:var(--ink);letter-spacing:-.01em}
.stat span{display:block;margin-top:6px;font-size:.76rem;line-height:1.3;color:var(--ink-3)}

.notice{margin:22px 0 0;padding:14px 20px;background:var(--surface);border:1px solid var(--line);border-left:5px solid var(--gold);border-radius:0 12px 12px 0;font-size:.88rem;line-height:1.55;color:var(--ink-2)}
.notice b{color:var(--ink)}

/* contents */
nav.toc{margin:22px 0 0;padding:18px 24px;background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow)}
nav.toc h2{margin:0 0 12px;font-size:.78rem;letter-spacing:.18em;color:var(--accent)}
nav.toc ol{list-style:none;counter-reset:t;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(10,auto);grid-auto-flow:column;column-gap:36px}
nav.toc li{counter-increment:t;break-inside:avoid;padding:3px 0;font-size:.93rem}
nav.toc li::before{content:counter(t,decimal-leading-zero);display:inline-block;width:2.1em;font-weight:700;font-size:.78rem;color:var(--sky)}
nav.toc a{color:var(--ink-2);text-decoration:none}
nav.toc a:hover{color:var(--accent);text-decoration:underline}

/* headings */
main h1{display:flex;align-items:center;gap:16px;margin:2.4em 0 .7em;color:var(--ink);font-size:1.75rem;line-height:1.2;letter-spacing:-.01em}
main h1 .num{flex:none;display:grid;place-items:center;min-width:52px;height:52px;padding:0 6px;border-radius:14px;background:linear-gradient(135deg,#1E3A8A,#0B7BEA);color:#fff;font-size:1.05rem;letter-spacing:.02em;box-shadow:0 6px 16px rgba(30,58,138,.35)}
main h1::after{content:"";flex:1;height:2px;margin-left:6px;background:linear-gradient(90deg,var(--line-2),transparent)}
main h2{position:relative;margin:1.6em 0 .45em;padding-left:16px;color:var(--ink);font-size:1.28rem;line-height:1.3}
main h2::before{content:"";position:absolute;left:0;top:.18em;bottom:.18em;width:5px;border-radius:3px;background:linear-gradient(var(--gold),var(--sky))}
main h3{margin:1.2em 0 .3em;color:var(--accent);font-size:1.02rem;letter-spacing:.01em}
p{margin:.65em 0}
strong{color:var(--ink)}
code{padding:.12em .42em;background:var(--surface-2);border:1px solid var(--line);border-radius:5px;font:.86em Consolas,"Cascadia Mono",monospace;color:var(--ink)}

/* lists */
main ul{list-style:none;padding-left:0;margin:.7em 0}
main ul li{position:relative;padding:1px 0 1px 26px}
main ul li::before{content:"";position:absolute;left:5px;top:.82em;width:8px;height:8px;border-radius:2px;background:var(--sky);transform:rotate(45deg)}
main ol:not(.flow){padding-left:0;list-style:none;counter-reset:o;margin:.7em 0}
main ol:not(.flow)>li{counter-increment:o;position:relative;padding:2px 0 2px 38px}
main ol:not(.flow)>li::before{content:counter(o);position:absolute;left:0;top:3px;width:26px;height:26px;border-radius:50%;background:var(--surface-2);border:1px solid var(--line-2);color:var(--accent);font-weight:700;font-size:.8rem;line-height:24px;text-align:center}

/* quote + callout */
blockquote{margin:1.2em 0;padding:16px 24px 16px 28px;background:var(--surface);border:1px solid var(--line);border-left:5px solid var(--sky);border-radius:0 12px 12px 0;box-shadow:var(--shadow);font-style:italic;color:var(--ink-2)}
blockquote p{margin:0}
.callout{position:relative;margin:1.3em 0;padding:18px 26px;color:#fff;background:linear-gradient(135deg,#1E3A8A,#0B5BD3);border-radius:14px;box-shadow:0 12px 30px rgba(30,58,138,.3);font-size:1.08rem;line-height:1.55}
.callout::before{content:"";position:absolute;left:0;top:18px;bottom:18px;width:5px;border-radius:0 3px 3px 0;background:var(--gold)}
.callout strong{color:#fff}

/* tables */
.tablewrap{overflow-x:auto;margin:1.1em 0;border:1px solid var(--line);border-radius:12px;background:var(--surface);box-shadow:var(--shadow)}
table{width:100%;border-collapse:collapse;font-size:.9rem;line-height:1.5}
th{background:#1E3A8A;color:#fff;text-align:left;padding:10px 14px;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}
td{padding:8px 14px;border-top:1px solid var(--line);vertical-align:top}
td:first-child{color:var(--ink);font-weight:600}
tbody tr:nth-child(even) td{background:color-mix(in srgb,var(--surface-2) 70%,transparent)}
tbody tr:last-child td{border-bottom:0}

/* workflow */
ol.flow{list-style:none;counter-reset:s;margin:1.1em 0;padding:0}
ol.flow li{counter-increment:s;position:relative;margin:0 0 0 20px;padding:0 0 14px 50px;border-left:3px solid var(--line-2)}
ol.flow li:last-child{border-left-color:transparent;padding-bottom:0}
ol.flow li::before{content:counter(s);position:absolute;left:-21px;top:0;width:39px;height:39px;border-radius:50%;background:linear-gradient(135deg,#1E3A8A,#0B7BEA);color:#fff;font-weight:700;font-size:.92rem;line-height:39px;text-align:center;border:3px solid var(--bg);box-shadow:0 4px 10px rgba(30,58,138,.3)}
ol.flow strong{display:block;margin-bottom:2px;font-size:1.02rem}

/* stage cards, segments, phases */
.stage{margin:.9em 0;padding:2px 24px 12px;background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:var(--shadow);counter-increment:stage}
.stages{counter-reset:stage}
.stage h3{margin-top:1.1em;color:var(--ink);font-size:1.12rem}
.stage h3::before{content:"0" counter(stage);display:inline-block;margin-right:12px;padding:2px 10px;border-radius:8px;background:var(--surface-2);border:1px solid var(--line-2);color:var(--accent);font-size:.82rem;vertical-align:2px}
h2.phase{margin-top:1.8em;padding:9px 18px 9px 22px;background:var(--surface);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow)}
h2.phase::before{top:0;bottom:0;border-radius:12px 0 0 12px;width:7px}
h2.segment{padding:10px 18px 10px 22px;background:var(--surface-2);border-radius:10px}
h2.segment::before{top:0;bottom:0;border-radius:10px 0 0 10px}

p.closing{margin:2em 0 .8em;padding:24px 20px;text-align:center;font-size:1.2rem;color:#fff;background:radial-gradient(circle at 80% 0,rgba(11,123,234,.6),transparent 55%),linear-gradient(135deg,#0A1740,#1E3A8A);border-radius:16px;box-shadow:0 14px 34px rgba(10,23,64,.35);border-bottom:5px solid var(--gold)}
p.closing strong{color:#fff;letter-spacing:.01em}
main>p>em:only-child{display:block;padding:14px 18px;border-top:1px solid var(--line);font-size:.86rem;color:var(--ink-3)}

footer{margin-top:28px;padding:18px 0 30px;border-top:1px solid var(--line);color:var(--ink-3);font-size:.84rem;text-align:center;letter-spacing:.03em}
footer b{color:var(--accent)}

@media (max-width:760px){
main h1{margin-top:2em}
.hero{padding:32px 0 88px}.hero .wrap{grid-template-columns:1fr 150px;gap:16px}.logo-card{padding:10px;border-radius:14px}.subtitle{font-size:1rem}.chips{margin-top:20px}
main h1{font-size:1.4rem}main h1 .num{min-width:44px;height:44px}
}
@media (max-width:560px){.stats{grid-template-columns:repeat(6,1fr);gap:10px}.stat{grid-column:span 2}.stat:nth-child(n+4){grid-column:span 3}.stat b{font-size:1.3rem}nav.toc{padding:14px 16px}nav.toc ol{column-gap:14px}nav.toc li{font-size:.82rem;padding:2px 0}nav.toc li::before{width:1.8em}.hero .wrap{grid-template-columns:1fr}.logo-card{max-width:200px;order:-1}}
@page{size:Letter;margin:10mm}
@media print{
:root{--accent:#1E3A8A;--sky:#0B7BEA;--bg:#fff;--surface:#fff;--surface-2:#EEF2FF;--ink:#0F172A;--ink-2:#1E293B;--ink-3:#64748B;--line:#E2E8F0;--line-2:#CBD5E1;--link:#1E3A8A;--shadow:none}
.bar,.theme{display:none!important}
body{font-size:10.5pt;line-height:1.55;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.hero{padding:16px 0 52px;border-radius:14px;break-after:avoid}h1.title{font-size:2.2rem}.hero .wrap{gap:12px}.subtitle{margin-top:6px;font-size:1rem}.tag{margin-top:8px}.chips{margin-top:12px;gap:6px}.chip{padding:5px 10px;font-size:.78rem}.stats{margin-top:-36px;gap:10px}.stat{padding:8px 6px}.stat b{font-size:1.3rem}.notice{margin-top:12px;padding:8px 14px;font-size:.78rem;line-height:1.4}body{background:#fff}
nav.toc{break-inside:avoid;margin-top:12px;padding:10px 20px}nav.toc h2{margin-bottom:6px}nav.toc li{padding:0;font-size:.84rem;white-space:nowrap}main{break-before:page}
main h1{break-after:avoid;margin-top:2.4em}main h2,main h3{break-after:avoid}
.stage,.callout,blockquote,ol.flow li,h2.phase,tr{break-inside:avoid}thead{display:table-header-group}
.tablewrap{overflow:visible}
}
"""

JS = """
(function(){
var r=document.documentElement,b=document.querySelectorAll('.theme'),bar=document.getElementById('bar'),p=bar.querySelector('i');
try{var s=localStorage.getItem('plan-theme');if(s)r.setAttribute('data-theme',s)}catch(e){}
b.forEach(function(x){x.addEventListener('click',function(){
var dark=r.getAttribute('data-theme')?r.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme:dark)').matches;
var n=dark?'light':'dark';r.setAttribute('data-theme',n);
try{localStorage.setItem('plan-theme',n)}catch(e){}
})});
function f(){var h=document.documentElement,t=h.scrollHeight-h.clientHeight;
bar.classList.toggle('on',h.scrollTop>320);p.style.width=(t>0?h.scrollTop/t*100:0)+'%'}
addEventListener('scroll',f,{passive:true});f();
})();
"""


def data_uri(name):
    raw = (ROOT / "assets" / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii")


def decorate(body):
    """Add the structural hooks the stylesheet styles (numbers, cards, classes)."""
    body = re.sub(
        r'<h1 id="([^"]+)">(\d+)\.\s*(.*?)</h1>',
        lambda m: f'<h1 id="{m.group(1)}"><span class="num">{int(m.group(2)):02d}</span><span>{m.group(3)}</span></h1>',
        body,
    )
    body = re.sub(r"<table>.*?</table>", lambda m: f'<div class="tablewrap">{m.group(0)}</div>', body, flags=re.S)
    body = body.replace('<h2 id="phase', '<h2 class="phase" id="phase').replace('<h2 id="segment', '<h2 class="segment" id="segment')
    stage = re.compile(r"(<h3[^>]*>Stage \d.*?</h3>.*?)(?=<h3|<h1)", re.S)
    body = stage.sub(lambda m: f'<div class="stage">{m.group(1)}</div>', body)
    first = body.find('<div class="stage">')
    last = body.rfind("</div>", 0, body.find("<h1", first))
    if first != -1 and last != -1:
        body = body[:first] + '<div class="stages">' + body[first : last + 6] + "</div>" + body[last + 6 :]
    return body


def main():
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "md_in_html"], extension_configs={"toc": {"permalink": False}})
    body = decorate(md.convert((ROOT / "business-plan.md").read_text(encoding="utf-8")))
    toc_items = "".join(
        f'<li><a href="#{t["id"]}">{html.escape(re.sub(r"^\d+\.\s*", "", t["name"]))}</a></li>'
        for t in md.toc_tokens
    )
    chips = "".join(f'<div class="chip"><span>{k}</span>{v}</div>' for k, v in META)
    stats = "".join(f'<div class="stat"><b>{v}</b><span>{k}</span></div>' for v, k in STATS)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data:; style-src 'unsafe-inline'; script-src 'unsafe-inline'">
<title>{TITLE}</title>
<style>{CSS}</style>
</head>
<body>
<div class="bar" id="bar"><b>OPEN BUSINESS PLAN TEMPLATE</b><button class="theme" type="button" aria-label="Toggle light and dark theme">Theme</button><i></i></div>
<button class="theme float" type="button" aria-label="Toggle light and dark theme">Theme</button>
<header class="hero">
<div class="wrap">
<div>
<p class="eyebrow">OPEN BUSINESS PLAN TEMPLATE</p>
<h1 class="title">AI-Era Technology Services<br>Business Plan</h1>
<p class="subtitle">{SUBTITLE}</p>
<span class="tag">{TAGLINE}</span>
</div>
</div>
<div class="wrap cw"><div class="chips">{chips}</div></div>
</header>
<div class="wrap">
<div class="stats">{stats}</div>
<nav class="toc" aria-label="Contents"><h2>CONTENTS</h2><ol>{toc_items}</ol></nav>
<aside class="notice" role="note"><b>Please read:</b> This is general business-planning information, not legal, financial, tax, or security advice. All figures are illustrative assumptions, not forecasts or promises of income, and you may lose money. Only test systems you own or have written permission to test. Verify everything with qualified professionals. See <a href="#19-notice-disclaimers-and-license">Section 19</a> and <a href="#17-legal-and-compliance">Section 17</a>.</aside>
<main>
{body}
</main>
<footer><b>Open Business Plan Template</b> · Originally published by CompleteTech LLC · © 2026 · Text licensed CC BY 4.0 · Not professional advice</footer>
</div>
<script>{JS}</script>
</body>
</html>
"""
    out = ROOT / "business-plan.html"
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
