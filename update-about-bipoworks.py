#!/usr/bin/env python3
"""
Update Sinchon about.html with Bipoworks copy + two-director structure.
- Philosophy: Bipoworks "Becoming more beautiful with a mere 1mm change" copy
- Dr. Kim Hye-won: Bipoworks original 5-paragraph message verbatim
- Dr. Kim Myung-hwan: New section in same Bipoworks tone (1mm philosophy maintained)
"""
import re
from pathlib import Path

# ---- Philosophy section: replace text with Bipoworks copy ----
NEW_PHILOSOPHY = '''<!-- Philosophy -->
<section class="philosophy">
    <div class="container">
        <div class="philosophy-image">
            <img src="/assets/images/about/philosophy.jpg" alt="Mili Clinic Sinchon">
        </div>
        <div class="philosophy-grid">
            <div class="philosophy-left">
                <div class="section-eyebrow">About Miliclinic</div>
                <h2>Becoming more beautiful with a mere 1mm change.</h2>
            </div>
            <div class="philosophy-right">
                <p class="lead">
                    Based on years of clinical experience, Miliclinic sincerely considers each customer's concerns as if they were our own family's.
                </p>
                <p>
                    The beauty of Miliclinic begins with a tiny 1mm — a point, a line, a surface, a dimension. Every detail is shaped to bring forward what is already there, refining rather than transforming, restoring rather than redesigning.
                </p>
                <p class="mobile-hide">
                    At Mili Clinic Sinchon, we are committed to the work most clinics overlook: the careful, meticulous attention to a single millimeter of change. The kind of change that no one else notices, but that you feel — every time you look in the mirror.
                </p>
            </div>
        </div>
    </div>
</section>'''

# ---- Two director sections: Bipoworks copy for Dr. Kim Hye-won + new for Dr. Kim Myung-hwan ----
NEW_DIRECTOR_BLOCK = '''<!-- Director's Message — Dr. Kim Hye-won -->
<section class="director">
    <div class="container">
        <div class="director-grid">
            <div class="director-portrait">
                <img src="/assets/images/about/director-kimhyewon.png" alt="Director Kim Hye-won">
            </div>
            <div class="director-content">
                <div class="section-eyebrow">Director's Message</div>
                <h2>
                    Beyond healing,
                    <span class="line-2">towards relaxation.</span>
                </h2>
                <p class="first-letter">
                    Based on extensive clinical experience, Miliclinic approaches each client's concerns as if they were those of our own family.
                </p>
                <p class="mobile-hide">
                    From the moment you walk through our doors, our goal is to offer comfort and lasting satisfaction — becoming a trusted companion and lifelong partner in your journey toward a healthy body and appearance.
                </p>
                <p class="mobile-hide">
                    We pay close attention to every detail of your treatment, carefully uncovering and refining even the subtlest 1mm changes that others might overlook.
                </p>
                <p>
                    We understand the courage it takes to choose Miliclinic. That's why every step — from preparation to aftercare — is approached with the utmost sincerity and <strong>without compromise</strong>.
                </p>
                <p>
                    Our commitment is to continue creating unique beauty for everyone who visits Miliclinic Sinchon. We are dedicated to offering you our very best — always.
                </p>

                <div class="director-sign">
                    <div class="director-sign-label">— Director</div>
                    <div class="director-sign-name">Kim Hye-won, M.D.</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Director's Message — Dr. Kim Myung-hwan -->
<section class="director director-alt">
    <div class="container">
        <div class="director-grid director-grid-reverse">
            <div class="director-content">
                <div class="section-eyebrow">Director's Message</div>
                <h2>
                    A single millimeter,
                    <span class="line-2">looked after with care.</span>
                </h2>
                <p class="first-letter">
                    The 1mm philosophy that guides Miliclinic is not a slogan — it is a clinical discipline. It is the practice of looking longer, listening more carefully, and intervening only where intervention is truly needed.
                </p>
                <p class="mobile-hide">
                    Every face is different, and every concern carries its own history. Before any treatment begins, we take the time to understand what brings you here and what you hope for — and just as importantly, what you do not want.
                </p>
                <p class="mobile-hide">
                    My approach is grounded in this discipline. Conservative judgment over aggressive promises. Layered, considered protocols over one-size-fits-all packages. Outcomes that age gracefully over results that simply impress in week one.
                </p>
                <p>
                    When you choose Miliclinic Sinchon, you are choosing a practice that takes the long view — <strong>your skin five years from now matters as much as how it looks tomorrow</strong>.
                </p>

                <div class="director-sign">
                    <div class="director-sign-label">— Director</div>
                    <div class="director-sign-name">Kim Myung-hwan, M.D.</div>
                </div>
            </div>
            <div class="director-portrait">
                <img src="/assets/images/about/director-kimmyunghwan.png" alt="Director Kim Myung-hwan">
            </div>
        </div>
    </div>
</section>'''

# ---- Pull quote: replace with Bipoworks-aligned copy ----
NEW_PULL_QUOTE = '''<!-- Pull Quote -->
<section class="pull-quote">
    <div class="pull-quote-inner">
        <div class="pull-quote-mark">"</div>
        <div class="pull-quote-text">
            <span class="emphasis">At Miliclinic Sinchon,</span> beauty begins with a single, <span class="emphasis">honest millimeter</span>.
        </div>
    </div>
</section>'''

# ---- CSS additions for two-director layout ----
CSS_ADDITIONS = '''
/* Two-director layout additions */
.director-alt{background: var(--bone)}
.director-grid-reverse{direction: rtl}
.director-grid-reverse > *{direction: ltr}
@media (max-width: 900px){
    .director-grid-reverse{direction: ltr}
}
'''


def main():
    f = Path('en/about.html')
    if not f.exists():
        print("ERROR: en/about.html not found. Run from repo root.")
        return

    content = f.read_text(encoding='utf-8')

    # 1. Replace Philosophy section
    pat1 = r'<!-- Philosophy -->.*?</section>'
    if re.search(pat1, content, re.DOTALL):
        content = re.sub(pat1, NEW_PHILOSOPHY, content, count=1, flags=re.DOTALL)
        print("OK   Philosophy section replaced (Bipoworks copy)")
    else:
        print("WARN Philosophy section not found")

    # 2. Replace Director section with two-director block
    pat2 = r"<!-- Director's Message.*?-->.*?</section>"
    if re.search(pat2, content, re.DOTALL):
        content = re.sub(pat2, NEW_DIRECTOR_BLOCK, content, count=1, flags=re.DOTALL)
        print("OK   Director section replaced with two-director block")
    else:
        print("WARN Director section not found")

    # 3. Replace Pull Quote with Bipoworks-aligned copy
    pat3 = r'<!-- Pull Quote -->.*?</section>'
    if re.search(pat3, content, re.DOTALL):
        content = re.sub(pat3, NEW_PULL_QUOTE, content, count=1, flags=re.DOTALL)
        print("OK   Pull Quote section replaced")

    # 4. Inject CSS additions if not already present
    if '.director-grid-reverse' not in content:
        content = content.replace('</style>', CSS_ADDITIONS + '</style>', 1)
        print("OK   Injected director-grid-reverse + director-alt CSS")
    else:
        print("SKIP director-grid-reverse CSS already present")

    f.write_text(content, encoding='utf-8')

    # Verify
    after = f.read_text(encoding='utf-8')
    print("")
    print("=== Verification ===")
    print(f"Kim Hye-won: {after.count('Kim Hye-won')}")
    print(f"Kim Myung-hwan: {after.count('Kim Myung-hwan')}")
    print(f"Bipoworks key phrase 'Beyond healing': {'Beyond healing' in after}")
    print(f"Bipoworks key phrase '1mm': {after.count('1mm')}")
    print(f"director-grid-reverse: {after.count('director-grid-reverse')}")
    print(f"Shin Dong-ha residual (should be 0): {after.count('Shin Dong-ha') + after.count('Shin Dongha')}")


if __name__ == '__main__':
    main()
