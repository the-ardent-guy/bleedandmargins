import os

BASE = r'C:\Users\thear\OneDrive\Desktop\bleedmargins'

CORRECT_FONTS = """@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-45Light-Trial.otf') format('opentype');font-weight:300;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-55Roman-Trial.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-65Medium-Trial.otf') format('opentype');font-weight:500;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-55Roman-Trial.otf') format('opentype');font-weight:400;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-65Medium-Trial.otf') format('opentype');font-weight:500;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Text';src:url('fonts/NeueHaasGrotText-75Bold-Trial.otf') format('opentype');font-weight:700;font-style:normal;font-display:swap;}"""

WRONG_FONTS_A = """@font-face{font-family:'NHG Display';src:url('fonts/NHGDisplay-Light.otf') format('opentype');font-weight:300;font-style:normal;}
@font-face{font-family:'NHG Display';src:url('fonts/NHGDisplay-Regular.otf') format('opentype');font-weight:400;font-style:normal;}
@font-face{font-family:'NHG Display';src:url('fonts/NHGDisplay-Medium.otf') format('opentype');font-weight:500;font-style:normal;}
@font-face{font-family:'NHG Text';src:url('fonts/NHGText-Regular.otf') format('opentype');font-weight:400;font-style:normal;}
@font-face{font-family:'NHG Text';src:url('fonts/NHGText-Medium.otf') format('opentype');font-weight:500;font-style:normal;}
@font-face{font-family:'NHG Text';src:url('fonts/NHGText-Bold.otf') format('opentype');font-weight:700;font-style:normal;}"""

WRONG_FONTS_B = """@font-face{font-family:'NHG Display';font-weight:300;font-style:normal;font-display:swap;src:url('fonts/NHGDisplay-Light.woff2') format('woff2');}
@font-face{font-family:'NHG Display';font-weight:400;font-style:normal;font-display:swap;src:url('fonts/NHGDisplay-Regular.woff2') format('woff2');}
@font-face{font-family:'NHG Display';font-weight:500;font-style:normal;font-display:swap;src:url('fonts/NHGDisplay-Medium.woff2') format('woff2');}
@font-face{font-family:'NHG Text';font-weight:400;font-style:normal;font-display:swap;src:url('fonts/NHGText-Regular.woff2') format('woff2');}
@font-face{font-family:'NHG Text';font-weight:500;font-style:normal;font-display:swap;src:url('fonts/NHGText-Medium.woff2') format('woff2');}
@font-face{font-family:'NHG Text';font-weight:700;font-style:normal;font-display:swap;src:url('fonts/NHGText-Bold.woff2') format('woff2');}"""

# Also remove non-existent bold/black NHG Display weights from work.html / kriya-collective.html
WRONG_BOLD_DISP = """@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-75Bold-Trial.otf') format('opentype');font-weight:700;font-style:normal;font-display:swap;}
@font-face{font-family:'NHG Display';src:url('fonts/NeueHaasGrotDisp-95Black-Trial.otf') format('opentype');font-weight:900;font-style:normal;font-display:swap;}"""

# ── Per-file dash and copy fixes ─────────────────────────────────────────────

FIXES = {

'index.html': [
    ('<span class="hero-slide-project">Boit Club - Branding &amp; Positioning</span>',
     '<span class="hero-slide-project">Boit Club · Branding &amp; Positioning</span>'),
    ('<span class="hero-slide-project">VIST Labs - Shopify Design &amp; Dev</span>',
     '<span class="hero-slide-project">VIST Labs · Shopify Design &amp; Dev</span>'),
    ('<span class="hero-slide-project">Oxy99 - Shopify &amp; Campaigns</span>',
     '<span class="hero-slide-project">Oxy99 · Shopify &amp; Campaigns</span>'),
    ('Most studios miss this - they apply one aesthetic to every brief and call it craft.',
     'Most studios miss this. They apply one aesthetic to every brief and call it craft.'),
    ("What's left is execution - and that's where the taste lives.",
     "What's left is execution. That's where the taste lives."),
    ('<h3 class="eng-name">Flagship Build <em> -  most picked</em></h3>',
     '<h3 class="eng-name">Flagship Build <em>· most picked</em></h3>'),
    ('Clinical restraint as the luxury signal - white space that earns trust.',
     'Clinical restraint as the luxury signal: white space that earns trust.'),
    ('Performance, accessibility, motion, and conversion treated as constraints - not afterthoughts.',
     'Performance, accessibility, motion, and conversion treated as constraints, not afterthoughts.'),
    ('we read the room - competitors, conventions, blind spots - then we build',
     'we read the room: competitors, conventions, blind spots. Then we build'),
    ('<option>Not sure yet - let\'s talk</option>',
     '<option>Not sure yet, let\'s talk</option>'),
],

'work.html': [
    ("isn&#x27;t here - NDAs have a way of keeping things interesting.",
     "isn&#x27;t here. NDAs have a way of keeping things interesting."),
    ("India&#x27;s only supercar registry - built from nothing into a category.",
     "India&#x27;s only supercar registry. Built from nothing into a category."),
    ('Cannabis packaging - where science had to do the selling.',
     'Cannabis packaging. Where science had to do the selling.'),
    ('Luxury architecture studio - a brand as considered as the spaces they design.',
     'Luxury architecture studio. A brand as considered as the spaces they design.'),
    ('South Indian kidswear - regional, playful, unapologetically itself.',
     'South Indian kidswear. Regional, playful, unapologetically itself.'),
    ('Salesforce consulting - made to look as sharp as the service they sell.',
     'Salesforce consulting. Made to look as sharp as the service they sell.'),
    ("The next move is yours - and it&#x27;s a simple one.",
     "The next move is yours. A simple one."),
    ('discretion - luxury, legal, finance, cannabis - you probably already know the drill.',
     'discretion: luxury, legal, finance, cannabis. You probably already know the drill.'),
],

'boit-club.html': [
    ('<span class="cs-stat-label">Digital showroom - India\'s first for supercars</span>',
     '<span class="cs-stat-label">Digital showroom · India\'s first for supercars</span>'),
    ('crossed 51,200 units in 2024 - the first time past 50,000.',
     'crossed 51,200 units in 2024, the first time past 50,000.'),
    ('<span class="find-stat">1% of India\'s car market is luxury - the lowest among major economies.</span>',
     '<span class="find-stat">1% of India\'s car market is luxury, the lowest among major economies.</span>'),
    ('The market runs almost entirely on personal networks - brokers, WhatsApp groups, and word of mouth.',
     'The market runs almost entirely on personal networks: brokers, WhatsApp groups, and word of mouth.'),
    ('<span class="find-stat">70% of India\'s used car market is unorganised - trust is the single biggest barrier.</span>',
     '<span class="find-stat">70% of India\'s used car market is unorganised. Trust is the single biggest barrier.</span>'),
    ('Cars24, Spinny, Droom - all chasing the mass market.',
     'Cars24, Spinny, Droom. All chasing the mass market.'),
    ("India's first verified supercar registry - a place to buy and sell supercars",
     "India's first verified supercar registry: a place to buy and sell supercars"),
    ('they needed to establish authority and exclusivity - digitally - before anyone would take them seriously.',
     'they needed to establish authority and exclusivity, digitally, before anyone would take them seriously.'),
    ('Every touchpoint - the registry, the content, the social presence - was designed to communicate one thing: this is where serious collectors come.',
     'Every touchpoint: the registry, the content, the social presence. All designed to communicate one thing: this is where serious collectors come.'),
    ("Built India's first supercar storefront - not a listing page, a digital forecourt.",
     "Built India's first supercar storefront: not a listing page, a digital forecourt."),
    ('<h3 class="del-title">The Registry - India\'s Supercar Marketplace</h3>',
     '<h3 class="del-title">The Registry</h3>'),
    ('NDTV and Hindustan Times - earned, not bought.',
     'NDTV and Hindustan Times. Earned, not bought.'),
    ('Serious collectors, enthusiasts, and high-net-worth buyers - an audience that belongs in the registry.',
     'Serious collectors, enthusiasts, and high-net-worth buyers. An audience that belongs in the registry.'),
    ('Cannabis packaging &amp; preservation, Illinois - where science needed to do the selling.',
     'Cannabis packaging &amp; preservation, Illinois. Where science needed to do the selling.'),
],

'zeroed-out.html': [
    ('<span class="cs-stat-label">The hex code for true black - embedded in the name itself</span>',
     '<span class="cs-stat-label">The hex code for true black, embedded in the name itself</span>'),
    ('<span class="cs-stat-label">Golden ratio - the mathematical principle the logo is built on</span>',
     '<span class="cs-stat-label">Golden ratio. The mathematical principle the logo is built on.</span>'),
    ("one of the fastest-growing segments in Indian fashion - driven by a young",
     "one of the fastest-growing segments in Indian fashion, driven by a young"),
    ('<span class="find-stat">India\'s streetwear market growing at 10%+ CAGR through 2025 - but the loudest brands aren\'t winning long-term.</span>',
     '<span class="find-stat">India\'s streetwear market growing at 10%+ CAGR through 2025. The loudest brands aren\'t winning long-term.</span>'),
    ('a clear emerging segment - buyers who wanted quality over noise.',
     'a clear emerging segment: buyers who wanted quality over noise.'),
    ('Supima cotton as the foundational asset - grown exclusively in the US',
     'Supima cotton as the foundational asset, grown exclusively in the US'),
    ('a comprehensive analysis of India\'s streetwear landscape - emerging trends, consumer behaviour',
     'a comprehensive analysis of India\'s streetwear landscape: emerging trends, consumer behaviour'),
    ('reinforced it rather than working around it - making the restraint',
     'reinforced it rather than working around it, making the restraint'),
    ('<span class="result-label">Identity system - from naming to logo to visual language</span>',
     '<span class="result-label">Identity system</span>'),
    ('and a complete visual identity - delivered as a system',
     'and a complete visual identity, delivered as a system'),
],

'koodai-kind.html': [
    ('It was also deeply patronising - to the craft, to the buyer, and to the object.',
     'It was also deeply patronising: to the craft, to the buyer, and to the object.'),
    ("The koodai's heritage doesn't need announcing - it's visible in every weave.",
     "The koodai's heritage doesn't need announcing. It's visible in every weave."),
    ('The product itself is the best thing on every page - so we built a UI',
     'The product itself is the best thing on every page, so we built a UI'),
    ('in a different conversation than every other brand in the space - not because',
     'in a different conversation than every other brand in the space. Not because'),
],

'kutty-jetty.html': [
    ('Kutty Jetty came with the product and the brand already figured out - export-quality',
     'Kutty Jetty came with the product and the brand already figured out: export-quality'),
    ('energy of a bold, South Indian kidswear brand - without getting in its way.',
     'energy of a bold, South Indian kidswear brand, without getting in its way.'),
    ("The storefront doesn't announce its regional identity - it just expresses it.",
     "The storefront doesn't announce its regional identity. It just expresses it."),
],

'kriya-collective.html': [
    ('<span class="cs-stat-label">Primary market - MENA luxury property</span>',
     '<span class="cs-stat-label">Primary market · MENA luxury property</span>'),
    ("MENA's luxury property clients - developers, private landowners, hospitality groups - shortlist on reputation",
     "MENA's luxury property clients: developers, private landowners, hospitality groups. They shortlist on reputation"),
    ("The website isn't a portfolio - it's a pitch.",
     "The website isn't a portfolio. It's a pitch."),
    ('Their portfolio was compelling - residential and commercial projects in Dubai',
     'Their portfolio was compelling: residential and commercial projects in Dubai'),
    ('for the next tier of projects - the ones where the studio',
     'for the next tier of projects: the ones where the studio'),
    ('Every decision - the type, the spacing, the palette, the way the portfolio is presented - communicates the same thing: this studio knows exactly what it\'s doing, and it doesn\'t need to prove it by being loud.',
     'Every decision: the type, the spacing, the palette, the way the portfolio is presented. All of it communicating the same thing: this studio knows exactly what it\'s doing, and it doesn\'t need to prove it by being loud.'),
    ('Contact was made frictionless - a high-value client should never have to hunt',
     'Contact was made frictionless. A high-value client should never have to hunt'),
    ('the level of work TKC produces - clean, considered, and built to convert',
     'the level of work TKC produces: clean, considered, and built to convert'),
    ("we weren't just building a website - we were building a position.",
     "we weren't just building a website. We were building a position."),
    ('South Indian kidswear - regional, playful, unapologetically itself.',
     'South Indian kidswear. Regional, playful, unapologetically itself.'),
],

'oxy99.html': [
    ("Portable oxygen is not a niche product - it's a category that spans",
     "Portable oxygen is not a niche product. It's a category that spans"),
    ('suddenly had five distinct consumer segments - each requiring different messaging',
     'suddenly had five distinct consumer segments, each requiring different messaging'),
    ('performance marketing, and branding - with a brief to sharpen',
     'performance marketing, and branding, with a brief to sharpen'),
    ('Website, commerce, brand - in that order.',
     'Website, commerce, brand. In that order.'),
    ('Oxy99 already had it - three decades of it.',
     'Oxy99 already had it. Three decades of it.'),
    ('conversion-focused navigation - designed so someone',
     'conversion-focused navigation, designed so someone'),
    ("India's most trusted portable oxygen brand - now with a website",
     "India's most trusted portable oxygen brand, now with a website"),
    ('working in parallel - search intent captured at the top',
     'working in parallel: search intent captured at the top'),
],

}

def fix_file(filename, replacements):
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix fonts
    if WRONG_FONTS_A in content:
        content = content.replace(WRONG_FONTS_A, CORRECT_FONTS)
        print(f"  [FONTS-A fixed]")
    if WRONG_FONTS_B in content:
        content = content.replace(WRONG_FONTS_B, CORRECT_FONTS)
        print(f"  [FONTS-B fixed]")
    if WRONG_BOLD_DISP in content:
        content = content.replace(WRONG_BOLD_DISP, '')
        print(f"  [Non-existent bold/black NHG Display removed]")

    # Fix dashes and copy
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"  fixed: {old[:60]}...")
        else:
            print(f"  MISS: {old[:60]}...")

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  => SAVED {filename}")
    else:
        print(f"  => no changes in {filename}")

for filename, replacements in FIXES.items():
    print(f"\n=== {filename} ===")
    fix_file(filename, replacements)

# Fix font-only files (no copy fixes needed but fonts are wrong)
for filename in ['bizotico.html', 'zeroed-out.html', 'koodai-kind.html', 'oxy99.html', 'kutty-jetty.html']:
    if filename not in FIXES:
        path = os.path.join(BASE, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        if WRONG_FONTS_A in content:
            content = content.replace(WRONG_FONTS_A, CORRECT_FONTS)
            print(f"\n{filename}: fonts fixed")
        if WRONG_FONTS_B in content:
            content = content.replace(WRONG_FONTS_B, CORRECT_FONTS)
            print(f"\n{filename}: fonts fixed (woff2)")
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print("\nDone.")
