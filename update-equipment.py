#!/usr/bin/env python3
"""
Replace equipment.html main content with Sinchon's 22 devices in 6 categories.
- Uses Bipoworks Sinchon's headline: "We promise the best results with latest medical equipment"
- Keeps Dosan's category-based grid design
- Flat image folder: /assets/images/equipment/{slug}.jpg
"""
import re
from pathlib import Path

# Sinchon equipment, organized into Dosan's 6 categories
EQUIPMENT = {
    'Lifting': {
        'cat_num': '01',
        'desc': 'Ultrasound and radiofrequency platforms that restore foundational structure — each targeting a different skin layer for a cumulative, natural result.',
        'devices': [
            ('Ulthera', 'HIFU Lifting · Merz', 'ulthera.jpg'),
            ('TuneFace / TuneLiner / TuneBody', 'RF Lifting · ALMA', 'tuneface.jpg'),
            ('Oligio X', 'Monopolar RF · Jeisys', 'oligio-x.jpg'),
            ('InMode', 'Bipolar RF · InMode', 'inmode.jpg'),
            ('Shurink', 'HIFU Lifting · Classys', 'shurink.jpg'),
            ('Titanium', 'Multi-Wave Lifting', 'titanium.jpg'),
        ],
    },
    'Laser': {
        'cat_num': '02',
        'desc': 'Wavelength-specific lasers for pigmentation, vascular concerns, and overall tone refinement — calibrated for Asian skin.',
        'devices': [
            ('GentleMax Pro Plus', 'Alexandrite & Nd:YAG · Candela', 'gentlemax-pro-plus.jpg'),
            ('PicoPlus', 'Picosecond Laser · Lutronic', 'picoplus.jpg'),
            ('Spectra Plus', 'Q-Switched Nd:YAG · Lutronic', 'spectra-plus.jpg'),
            ('Capri', 'Fractional Laser · Alma', 'capri.jpg'),
        ],
    },
    'Booster & MTS': {
        'cat_num': '03',
        'desc': 'Microneedling and energy-based delivery systems that drive active ingredients deep into the dermis for sustained skin renewal.',
        'devices': [
            ('Secret RF', 'RF Microneedling · Cutera', 'secret.jpg'),
            ('DUET RF', 'Dual RF · Jeisys', 'duet-rf.jpg'),
            ('Potenza', 'Multi-Mode RF · Jeisys', 'potenza.jpg'),
            ('Action 2', 'Plasma & MTS', 'action-2.jpg'),
        ],
    },
    'Body': {
        'cat_num': '04',
        'desc': 'Non-invasive body contouring platforms — from cryolipolysis to focused ultrasound — for measured, lasting reshaping.',
        'devices': [
            ('NobleShape', 'Body Lifting & Contouring', 'nobleshape.jpg'),
            ('CryoCell', 'Cryolipolysis Fat Reduction', 'cryocell.jpg'),
            ('Fascella', 'Body Tightening', 'fascella.jpg'),
        ],
    },
    'Diagnostic': {
        'cat_num': '05',
        'desc': 'Precision skin diagnostics that ground every treatment plan in objective data, not assumption.',
        'devices': [
            ('Meta-view', 'Advanced Skin Analysis', 'meta-view.jpg'),
        ],
    },
    'Skin Care': {
        'cat_num': '06',
        'desc': 'Gentle, regenerative platforms that complement clinical treatments — for daily skin health and post-procedure recovery.',
        'devices': [
            ('Derma S Ultra', 'Ultrasonic Skincare', 'derma-s-ultra.jpg'),
            ('LDM', 'Local Dynamic Micromassage', 'ldm.jpg'),
            ('Plasonic', 'Plasma Skin Care', 'plasonic.jpg'),
            ('Aqua Peel', 'Hydra Cleansing', 'aqua-peel.jpg'),
        ],
    },
}


def build_category_section(name, info):
    cat_id = name.lower().replace(' ', '').replace('&', '')
    cards_html = []
    for device_name, sub, filename in info['devices']:
        cards_html.append(f'''            <article class="eq-card">
                <div class="eq-card-img"><img src="/assets/images/equipment/{filename}" alt="{device_name}"></div>
                <div class="eq-card-meta">
                    <div>
                        <div class="eq-card-name">{device_name}</div>
                        <div class="eq-card-sub">{sub}</div>
                    </div>
                </div>
            </article>''')
    cards = '\n'.join(cards_html)

    return f'''<!-- {name.upper()} -->
<section id="{cat_id}" class="category">
    <div class="container">
        <div class="category-head">
            <div>
                <div class="cat-num">— Category {info['cat_num']}</div>
                <h2>{name}.</h2>
            </div>
            <p>{info['desc']}</p>
        </div>
        <div class="eq-grid">
{cards}
        </div>
    </div>
</section>'''


def build_category_nav():
    items = []
    for name, info in EQUIPMENT.items():
        cat_id = name.lower().replace(' ', '').replace('&', '')
        items.append(f'                <a href="#{cat_id}" class="cat-nav-link">{name}</a>')
    return '\n'.join(items)


def main():
    f = Path('en/equipment.html')
    if not f.exists():
        print("ERROR: en/equipment.html not found.")
        return

    content = f.read_text(encoding='utf-8')

    # Build the new main body (everything between <!-- Category Nav --> and <!-- Footer -->)
    nav_links = build_category_nav()
    sections_html = '\n\n'.join(build_category_section(name, info) for name, info in EQUIPMENT.items())

    new_body = f'''<!-- Hero -->
<section class="eq-hero">
    <div class="container">
        <div class="eq-hero-eyebrow">Equipment</div>
        <h1>We promise the best results<br>with the latest medical equipment.</h1>
        <p>Mili Clinic Sinchon operates with twenty-two clinical-grade platforms — each selected for a specific purpose, each maintained to manufacturer standards. We use authentic equipment imported through official channels, calibrated regularly, and operated only by trained physicians and staff.</p>
    </div>
</section>

<!-- Category Nav -->
<nav class="cat-nav">
    <div class="container">
        <div class="cat-nav-inner">
{nav_links}
        </div>
    </div>
</nav>

{sections_html}

<!-- Principle Band -->
<section class="principle">
    <div class="container">
        <p>Equipment alone does not make a treatment work. <strong>Judgment does.</strong> Every device at Mili Sinchon is paired with a physician's reading of your skin — what it needs, when, and how much.</p>
    </div>
</section>'''

    # Replace from <!-- Hero --> (or <!-- Top Bar --> end) through end of last category
    # Strategy: find the section that starts after </header> closing or after <!-- Header --> block, ends before <!-- Footer -->
    pat = r'(<!-- Hero -->.*?)(<!-- Footer -->)'
    match = re.search(pat, content, re.DOTALL)
    if match:
        content = content.replace(match.group(1), new_body + '\n\n')
        print("OK   Replaced equipment body with Sinchon 22 devices in 6 categories")
    else:
        # Fallback: try Category Nav section
        pat2 = r'(<!-- Category Nav -->.*?)(<!-- Footer -->)'
        match2 = re.search(pat2, content, re.DOTALL)
        if match2:
            content = content.replace(match2.group(1), new_body + '\n\n')
            print("OK   Replaced equipment body (fallback path)")
        else:
            print("WARN Could not locate equipment body. No changes made.")
            return

    # Update <title> and meta description
    content = re.sub(
        r'<title>[^<]*</title>',
        '<title>Equipment | Mili Clinic Sinchon</title>',
        content, count=1
    )
    content = re.sub(
        r'<meta name="description" content="[^"]*"',
        '<meta name="description" content="Mili Clinic Sinchon operates 22 clinical-grade platforms across lifting, laser, booster, body, diagnostic, and skin care categories."',
        content, count=1
    )

    f.write_text(content, encoding='utf-8')

    print("\n=== Verification ===")
    after = f.read_text(encoding='utf-8')
    for cat in EQUIPMENT.keys():
        print(f"  {cat}: count {after.count('<h2>' + cat + '.</h2>')}")
    print(f"  Total eq-card: {after.count('eq-card-img')}")
    print(f"  Expected: 22")


if __name__ == '__main__':
    main()
