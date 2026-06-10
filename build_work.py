import os

base_dir = r'C:\Users\thear\OneDrive\Desktop\bleedmargins'

with open(os.path.join(base_dir, '_bg_rules.tmp'), 'r', encoding='utf-8') as f:
    bg_css = f.read()

html_before = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Work — Bleed &amp; Margins</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet"/>
<style>
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-55Roman-Trial.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-45Light-Trial.otf') format('opentype');font-weight:300;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-65Medium-Trial.otf') format('opentype');font-weight:500;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-75Bold-Trial.otf') format('opentype');font-weight:700;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-95Black-Trial.otf') format('opentype');font-weight:900;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-55Roman-Trial.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-65Medium-Trial.otf') format('opentype');font-weight:500;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-75Bold-Trial.otf') format('opentype');font-weight:700;font-style:normal;font-display:swap;}
</style>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
:root{--ink:#1a1510;--paper:#f7f2e8;--off:#f0e8d8;--dim:#e8dfc8;--muted:#8a7d6a;--border:rgba(26,21,16,0.15);--accent:#d6c8ae;}
body{background:var(--paper);color:var(--ink);font-family:'JetBrains Mono',monospace;overflow-x:hidden;cursor:none;background-image:linear-gradient(rgba(26,21,16,0.065) 1px,transparent 1px),linear-gradient(90deg,rgba(26,21,16,0.065) 1px,transparent 1px),linear-gradient(rgba(26,21,16,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(26,21,16,0.025) 1px,transparent 1px);background-size:80px 80px,80px 80px,20px 20px,20px 20px;}
body::after{content:'';position:fixed;inset:0;z-index:9990;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");opacity:0.035;pointer-events:none;mix-blend-mode:multiply;}
.cursor-dot{position:fixed;z-index:9999;width:10px;height:10px;background:var(--ink);border-radius:0;pointer-events:none;transform:translate(-50%,-50%);}
.cursor-ring{position:fixed;z-index:9998;width:32px;height:32px;border:1.5px solid var(--ink);border-radius:0;pointer-events:none;transform:translate(-50%,-50%);transition:width .2s,height .2s,opacity .2s;opacity:0.4;}
body:has(a:hover) .cursor-ring,body:has(button:hover) .cursor-ring{width:48px;height:48px;opacity:1;}
.crop{position:fixed;inset:0;z-index:9980;pointer-events:none;}
.crop::before,.crop::after,.crop span::before,.crop span::after{content:'';position:absolute;background:rgba(26,21,16,0.12);}
.crop::before{top:22px;left:6px;width:18px;height:1px;}.crop::after{top:6px;left:22px;width:1px;height:18px;}
.crop span:first-child::before{top:22px;right:6px;width:18px;height:1px;}.crop span:first-child::after{top:6px;right:22px;width:1px;height:18px;}
.crop span:last-child::before{bottom:22px;left:6px;width:18px;height:1px;}.crop span:last-child::after{bottom:6px;left:22px;width:1px;height:18px;}
.crop-br-h{position:fixed;bottom:22px;right:6px;width:18px;height:1px;background:rgba(26,21,16,0.2);z-index:9981;pointer-events:none;}
.crop-br-v{position:fixed;bottom:6px;right:22px;width:1px;height:18px;background:rgba(26,21,16,0.2);z-index:9981;pointer-events:none;}
.hl{background:linear-gradient(104deg,transparent 0%,rgba(201,240,75,0) 1%,rgba(201,240,75,0.42) 2.5%,rgba(201,240,75,0.38) 96%,rgba(201,240,75,0) 99%,transparent 100%);padding:0.04em 0.3em;margin:0 -0.08em;-webkit-box-decoration-break:clone;box-decoration-break:clone;}
nav{position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:stretch;border-bottom:1px solid var(--ink);background:var(--paper);height:64px;}
.nav-wordmark{text-decoration:none;display:flex;flex-direction:column;justify-content:center;line-height:1;gap:0;padding:0 24px;border-right:1px solid var(--ink);min-width:140px;}
.nav-wordmark .wm-top{font-family:'NHG Text',sans-serif;font-size:18px;color:var(--ink);line-height:1.05;}
.nav-wordmark .wm-bot{font-family:'NHG Display',sans-serif;font-weight:500;font-size:13px;color:var(--ink);letter-spacing:0.22em;text-transform:uppercase;line-height:1;}
.nav-logo-img{height:34px;width:auto;display:block;}
.nav-links{display:flex;flex:1;list-style:none;}
.nav-links li{border-right:1px solid var(--ink);}
.nav-links a{display:flex;align-items:center;padding:0 28px;height:100%;font-family:'NHG Display',sans-serif;font-weight:500;font-size:13px;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;color:var(--ink);opacity:0.45;transition:opacity .15s,background .15s;}
.nav-links a:hover{opacity:1;background:rgba(26,21,16,0.04);}.nav-links a.active{opacity:1;}
.nav-cta{margin-left:auto;display:flex;align-items:center;padding:0 28px;border-left:1px solid var(--ink);font-family:'NHG Display',sans-serif;font-weight:500;font-size:13px;letter-spacing:0.14em;text-transform:uppercase;text-decoration:none;color:var(--ink);transition:background .15s,color .15s;white-space:nowrap;}
.nav-cta:hover{background:var(--ink);color:var(--paper);}
.page-header{margin-top:64px;display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--ink);min-height:56vh;}
.ph-left{padding:80px 72px;border-right:1px solid var(--ink);display:flex;flex-direction:column;justify-content:space-between;}
.ph-eyebrow{font-size:10px;letter-spacing:0.24em;text-transform:uppercase;color:var(--muted);margin-bottom:32px;}
.ph-title{font-family:'NHG Display',sans-serif;font-weight:500;font-size:clamp(64px,9vw,136px);line-height:0.85;text-transform:uppercase;letter-spacing:-0.02em;flex:1;display:block;padding-top:16px;color:var(--ink);}
.ph-meta{padding-top:40px;border-top:1px solid var(--border);}
.ph-count-label{font-family:'NHG Text',sans-serif;font-size:15px;line-height:1.7;color:var(--muted);}
.ph-right{background:var(--ink);padding:80px 64px;display:flex;flex-direction:column;justify-content:space-between;}
.ph-statement{font-family:'NHG Display',sans-serif;font-weight:500;font-size:clamp(28px,3.5vw,52px);text-transform:uppercase;line-height:0.9;letter-spacing:-0.01em;color:var(--paper);margin-bottom:48px;}
.ph-disclaimer{font-family:'NHG Text',sans-serif;font-size:15px;line-height:1.75;color:rgba(247,242,232,0.5);max-width:420px;border-top:1px solid rgba(247,242,232,0.1);padding-top:28px;}
.filter-bar{border-bottom:1px solid var(--ink);display:flex;align-items:stretch;flex-wrap:wrap;}
.filter-label{display:flex;align-items:center;padding:0 28px;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:var(--muted);border-right:1px solid var(--ink);white-space:nowrap;}
.filter-btn{display:flex;align-items:center;padding:0 28px;height:52px;font-family:'NHG Display',sans-serif;font-weight:500;font-size:13px;letter-spacing:0.1em;text-transform:uppercase;border:none;border-right:1px solid var(--ink);background:transparent;color:var(--muted);cursor:none;transition:all .15s;}
.filter-btn:hover{background:rgba(26,21,16,0.04);color:var(--ink);}.filter-btn.active{background:var(--ink);color:var(--paper);}
.projects-grid{display:grid;grid-template-columns:repeat(2,1fr);}
.project-card{position:relative;overflow:hidden;border-bottom:1px solid var(--ink);border-right:1px solid var(--ink);min-height:480px;display:flex;flex-direction:column;justify-content:flex-end;transition:opacity .3s;}
.project-card:nth-child(even){border-right:none;}
.project-card.hidden{display:none;}
.proj-bg{position:absolute;inset:0;background-size:cover;background-position:center;transition:transform .7s ease;}
.project-card:hover .proj-bg{transform:scale(1.025);}
.proj-overlay{position:absolute;inset:0;background:linear-gradient(to top,rgba(26,21,16,0.92) 0%,rgba(26,21,16,0.3) 55%,transparent 100%);}
.proj-num{position:absolute;top:28px;right:28px;font-family:'JetBrains Mono',monospace;font-size:10px;color:rgba(247,242,232,0.18);letter-spacing:0.1em;z-index:2;}
.proj-content{position:relative;z-index:2;padding:40px 48px;}
.proj-tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px;}
.proj-tag{font-size:8px;letter-spacing:0.14em;text-transform:uppercase;border:1px solid rgba(247,242,232,0.2);padding:4px 10px;color:rgba(247,242,232,0.5);}
.proj-tag.accent{background:var(--accent);border-color:var(--accent);color:var(--ink);}
.proj-title{font-family:'NHG Display',sans-serif;font-weight:500;font-size:clamp(36px,4.5vw,64px);text-transform:uppercase;line-height:0.88;letter-spacing:-0.01em;color:var(--paper);margin-bottom:12px;}
.proj-sub{font-family:'NHG Text',sans-serif;font-size:15px;line-height:1.6;color:rgba(247,242,232,0.55);max-width:380px;margin-bottom:24px;}
.proj-link{display:inline-flex;flex-direction:column;gap:3px;font-family:'NHG Display',sans-serif;font-weight:500;font-size:12px;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;color:rgba(247,242,232,0.6);transition:color .2s;}
.proj-link .ul{height:1px;background:rgba(247,242,232,0.25);transition:background .2s;}
.proj-link:hover{color:var(--accent);}.proj-link:hover .ul{background:var(--accent);}
"""

html_middle = """
.bottom-strip{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--ink);}
.bs-left{padding:88px 72px;border-right:1px solid var(--ink);display:flex;flex-direction:column;justify-content:space-between;gap:40px;}
.bs-heading{font-family:'NHG Display',sans-serif;font-weight:500;font-size:clamp(48px,6vw,88px);text-transform:uppercase;line-height:0.88;letter-spacing:-0.01em;}
.bs-body{font-family:'NHG Text',sans-serif;font-size:16px;line-height:1.75;color:rgba(26,21,16,0.65);max-width:420px;}
.btn-primary{display:inline-flex;align-items:center;gap:8px;margin-top:8px;padding:14px 28px;font-family:'NHG Display',sans-serif;font-weight:500;font-size:13px;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;color:var(--paper);background:var(--ink);border:1px solid var(--ink);transition:background .15s,color .15s;width:fit-content;}
.btn-primary:hover{background:transparent;color:var(--ink);}
.bs-right{padding:88px 72px;display:flex;flex-direction:column;gap:64px;}
.bs-nda{border-left:2px solid var(--accent);padding-left:24px;}
.nda-label{font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:12px;}
.nda-text{font-family:'NHG Display',sans-serif;font-weight:500;font-size:clamp(20px,2.2vw,30px);text-transform:uppercase;line-height:0.92;letter-spacing:-0.01em;margin-bottom:16px;}
.nda-sub{font-family:'NHG Text',sans-serif;font-size:14px;line-height:1.7;color:var(--muted);max-width:380px;}
.bs-services{display:flex;flex-direction:column;gap:0;}
.bs-service-row{display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1px solid var(--border);}
.bs-service-row:first-child{border-top:1px solid var(--border);}
.bs-service-name{font-family:'NHG Display',sans-serif;font-weight:500;font-size:14px;letter-spacing:0.04em;text-transform:uppercase;}
.bs-service-tag{font-size:8px;letter-spacing:0.14em;text-transform:uppercase;border:1px solid var(--border);padding:4px 10px;color:var(--muted);}
footer{background:var(--ink);display:grid;grid-template-columns:1fr 1fr 1fr;}
.footer-col{padding:40px;border-right:1px solid rgba(247,242,232,0.1);display:flex;flex-direction:column;justify-content:space-between;}
.footer-col:last-child{border-right:none;}
.footer-wordmark{text-decoration:none;display:flex;flex-direction:column;line-height:1;gap:1px;}
.footer-logo-img{height:38px;width:auto;display:block;filter:brightness(0) invert(1);opacity:0.75;}
.footer-copy{font-size:9px;color:rgba(247,242,232,0.22);letter-spacing:0.1em;margin-top:32px;}
.footer-label{font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:rgba(247,242,232,0.2);margin-bottom:20px;}
.footer-links{display:flex;flex-direction:column;gap:12px;list-style:none;}
.footer-links a{font-family:'NHG Display',sans-serif;font-weight:500;font-size:14px;letter-spacing:0.12em;text-transform:uppercase;color:rgba(247,242,232,0.38);text-decoration:none;transition:color .15s;}
.footer-links a:hover{color:var(--accent);}
.footer-contact a{display:block;font-family:'JetBrains Mono',monospace;font-size:11px;color:rgba(247,242,232,0.45);text-decoration:none;transition:color .15s;margin-bottom:10px;}
.footer-contact a:hover{color:var(--accent);}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .7s ease,transform .7s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}
.d1{transition-delay:.06s;}.d2{transition-delay:.12s;}.d3{transition-delay:.18s;}.d4{transition-delay:.24s;}
@media(max-width:900px){.page-header,.bottom-strip{grid-template-columns:1fr;}.ph-left{border-right:none;border-bottom:1px solid var(--ink);}footer{grid-template-columns:1fr;}.footer-col{border-right:none;border-bottom:1px solid rgba(247,242,232,0.1);}.footer-col:last-child{border-bottom:none;}.bs-left{border-right:none;border-bottom:1px solid var(--ink);}}
@media(max-width:768px){nav{height:52px;}.nav-wordmark{padding:0 16px;min-width:auto;}.nav-links a{padding:0 16px;}.nav-cta{padding:0 16px;}.ph-left,.ph-right{padding:48px 24px;}.ph-title{font-size:clamp(52px,13vw,88px);}.projects-grid{grid-template-columns:1fr;}.project-card{border-right:none;min-height:80vw;}.proj-content{padding:28px 24px;}.proj-title{font-size:clamp(32px,9vw,52px);}.filter-bar{overflow-x:auto;flex-wrap:nowrap;-webkit-overflow-scrolling:touch;}.filter-btn{white-space:nowrap;flex-shrink:0;}.bs-left,.bs-right{padding:48px 24px;}.bs-heading{font-size:clamp(36px,10vw,64px);}footer .footer-col{padding:32px 24px;}}
@media(hover:none),(pointer:coarse){body{cursor:auto !important;}.cursor-dot,.cursor-ring{display:none !important;}a,button{cursor:pointer !important;}}
*{max-width:100%;}img,svg{max-width:100%;height:auto;}
</style>
</head>
<body>

<div class="cursor-dot" id="cd"></div>
<div class="cursor-ring" id="cr"></div>
<div class="crop"><span></span><span></span></div>
<div class="crop-br-h"></div><div class="crop-br-v"></div>

<nav>
  <a href="index.html" class="nav-wordmark">
    <img src="bm-logo.svg" alt="Bleed &amp; Margins" class="nav-logo-img">
  </a>
  <ul class="nav-links">
    <li><a href="index.html#services">Services</a></li>
    <li><a href="work.html" class="active">Work</a></li>
    <li><a href="index.html#approach">Approach</a></li>
  </ul>
  <a href="index.html#contact" class="nav-cta">Start a Project</a>
</nav>

<div class="page-header">
  <div class="ph-left">
    <p class="ph-eyebrow reveal">Portfolio &middot; India &amp; UAE &middot; Est. 2024</p>
    <div class="ph-title reveal d1">All<br/>the<br/>work.</div>
    <div class="ph-meta reveal d2">
      <p class="ph-count-label">These are the projects<br/>we&#x27;re allowed to talk about.</p>
    </div>
  </div>
  <div class="ph-right">
    <p class="ph-statement reveal">A few of them<br/>changed how<br/>we work.</p>
    <p class="ph-disclaimer reveal d2">Some of the best work we&#x27;ve done isn&#x27;t here - NDAs have a way of keeping things interesting. What is here should give you a fair idea of how we think. The rest is better explained over a conversation.</p>
  </div>
</div>

<div class="filter-bar">
  <span class="filter-label">Filter &mdash;</span>
  <button class="filter-btn active" data-filter="all">Everything</button>
  <button class="filter-btn" data-filter="branding">Branding</button>
  <button class="filter-btn" data-filter="shopify">Shopify</button>
  <button class="filter-btn" data-filter="growth">Growth</button>
  <button class="filter-btn" data-filter="uiux">UI/UX</button>
</div>

<div class="projects-grid" id="grid">
  <div class="project-card p-boit reveal d1" data-tags="branding growth">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">01</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Social Growth</span><span class="proj-tag">Shopify</span><span class="proj-tag">Luxury Automotive</span></div>
      <h2 class="proj-title">Boit Club</h2>
      <p class="proj-sub">India&#x27;s only supercar registry - built from nothing into a category.</p>
      <a href="boit-club.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-bizotico reveal d2" data-tags="shopify growth">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">02</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Growth Retainer</span><span class="proj-tag">Shopify</span><span class="proj-tag">Luxury Watches</span></div>
      <h2 class="proj-title">Bizotico</h2>
      <p class="proj-sub">25 years offline. We fixed that. 7.85x ROAS as a thank you.</p>
      <a href="bizotico.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-zeroed reveal d1" data-tags="branding">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">03</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Branding</span><span class="proj-tag">All-Black Apparel</span></div>
      <h2 class="proj-title">Zeroed Out</h2>
      <p class="proj-sub">An identity built entirely in the absence of colour.</p>
      <a href="zeroed-out.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-vist reveal d2" data-tags="shopify uiux">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">04</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Shopify</span><span class="proj-tag">UI/UX</span><span class="proj-tag">Cannabis Tech</span></div>
      <h2 class="proj-title">VIST Labs</h2>
      <p class="proj-sub">Cannabis packaging - where science had to do the selling.</p>
      <a href="vist-labs.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-koodai reveal d1" data-tags="shopify uiux branding">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">05</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Campaign Photography</span><span class="proj-tag">Shopify</span><span class="proj-tag">Heritage</span></div>
      <h2 class="proj-title">Koodai Kind</h2>
      <p class="proj-sub">A cultural artefact made shoppable. Heritage without the dust.</p>
      <a href="koodai-kind.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-oxy reveal d2" data-tags="branding shopify growth">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">06</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Branding</span><span class="proj-tag">Shopify</span><span class="proj-tag">Campaigns</span></div>
      <h2 class="proj-title">Oxy99</h2>
      <p class="proj-sub">India&#x27;s oxygen brand. We made people actually want to buy it.</p>
      <a href="oxy99.html" class="proj-link">Read the story <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-tkc reveal d1" data-tags="branding uiux">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">07</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Branding</span><span class="proj-tag">UI/UX</span><span class="proj-tag">Architecture</span></div>
      <h2 class="proj-title">The Kriya Collective</h2>
      <p class="proj-sub">Luxury architecture studio - a brand as considered as the spaces they design.</p>
      <a href="kriya-collective.html" class="proj-link">View Case Study <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-kutty reveal d2" data-tags="branding shopify uiux">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">08</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">Branding</span><span class="proj-tag">Shopify</span><span class="proj-tag">Kidswear</span></div>
      <h2 class="proj-title">Kutty Jetty</h2>
      <p class="proj-sub">South Indian kidswear - regional, playful, unapologetically itself.</p>
      <a href="kutty-jetty.html" class="proj-link">View Case Study <span class="ul"></span></a>
    </div>
  </div>
  <div class="project-card p-bossini reveal d1" data-tags="uiux">
    <div class="proj-bg"></div><div class="proj-overlay"></div><span class="proj-num">09</span>
    <div class="proj-content">
      <div class="proj-tags"><span class="proj-tag accent">UI/UX</span><span class="proj-tag">Framer</span><span class="proj-tag">Salesforce</span></div>
      <h2 class="proj-title">Bossini Technologies</h2>
      <p class="proj-sub">Salesforce consulting - made to look as sharp as the service they sell.</p>
      <a href="https://bossinitech.com/" target="_blank" class="proj-link">View Site <span class="ul"></span></a>
    </div>
  </div>
</div>

<div class="bottom-strip">
  <div class="bs-left reveal">
    <div>
      <h2 class="bs-heading">Seen enough?<br/>Let&#x27;s talk.</h2>
      <p class="bs-body">You&#x27;ve looked at the work. You&#x27;ve made up your mind. The next move is yours - and it&#x27;s a simple one.</p>
    </div>
    <a href="index.html#contact" class="btn-primary">Start a Project &rarr;</a>
  </div>
  <div class="bs-right">
    <div class="bs-nda reveal d1">
      <span class="nda-label">A note on the rest</span>
      <p class="nda-text">The work we can&#x27;t show<br/>is usually the most interesting.</p>
      <p class="nda-sub">NDAs exist for a reason. If you&#x27;re in a niche that requires discretion - luxury, legal, finance, cannabis - you probably already know the drill. Ask us about it over a call.</p>
    </div>
    <div class="bs-services reveal d2">
      <div class="bs-service-row"><span class="bs-service-name">Branding Strategy &amp; Design</span><span class="bs-service-tag">Available</span></div>
      <div class="bs-service-row"><span class="bs-service-name">Shopify E-Commerce</span><span class="bs-service-tag">Available</span></div>
      <div class="bs-service-row"><span class="bs-service-name">Web Design &amp; Development</span><span class="bs-service-tag">Available</span></div>
      <div class="bs-service-row"><span class="bs-service-name">Video Production</span><span class="bs-service-tag">Collab</span></div>
      <div class="bs-service-row"><span class="bs-service-name">Social Media Growth</span><span class="bs-service-tag">Available</span></div>
    </div>
  </div>
</div>

<footer>
  <div class="footer-col">
    <a href="index.html" class="footer-wordmark">
      <img src="bm-logo.svg" alt="Bleed &amp; Margins" class="footer-logo-img">
    </a>
    <p class="footer-copy">&copy; 2026 Bleed &amp; Margins.<br/>All rights reserved.</p>
  </div>
  <div class="footer-col">
    <p class="footer-label">Navigation</p>
    <ul class="footer-links">
      <li><a href="index.html#services">Services</a></li>
      <li><a href="work.html">Work</a></li>
      <li><a href="index.html#approach">Approach</a></li>
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
  </div>
  <div class="footer-col">
    <p class="footer-label">Get in Touch</p>
    <div class="footer-contact">
      <a href="mailto:bleedandmargins@gmail.com">bleedandmargins@gmail.com</a>
      <a href="#">Book a Call &rarr;</a>
    </div>
  </div>
</footer>

<script>
const cd=document.getElementById('cd'),cr=document.getElementById('cr');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;cd.style.left=mx+'px';cd.style.top=my+'px';});
(function loop(){rx+=(mx-rx)*0.1;ry+=(my-ry)*0.1;cr.style.left=rx+'px';cr.style.top=ry+'px';requestAnimationFrame(loop);})();
const obs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:0.08});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
if('ontouchstart'in window||navigator.maxTouchPoints>0){
  const dot=document.getElementById('cd'),ring=document.getElementById('cr');
  if(dot)dot.style.display='none';
  if(ring)ring.style.display='none';
  document.body.style.cursor='auto';
}
const btns=document.querySelectorAll('.filter-btn');
const cards=document.querySelectorAll('.project-card');
btns.forEach(btn=>{
  btn.addEventListener('click',()=>{
    btns.forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const f=btn.dataset.filter;
    cards.forEach(card=>{
      const match=f==='all'||card.dataset.tags.includes(f);
      card.classList.toggle('hidden',!match);
    });
  });
});
</script>
</body>
</html>"""

content = html_before + bg_css + html_middle

out_path = os.path.join(base_dir, 'work.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done. work.html written: {len(content):,} chars")
