#!/usr/bin/env python3
"""
Update Sinchon about.html to feature two directors: Kim Hye-won and Kim Myung-hwan.
Replaces the single Shin Dong-ha section with two separate director sections.
"""
import re
from pathlib import Path

# New section block: two director sections + director-grid-reverse CSS injection
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
                    The patient first,
                    <span class="line-2">the procedure second.</span>
                </h2>
                <p class="first-letter">
                    Aesthetic medicine sits at an unusual intersection — clinical precision on one side, deeply personal hopes on the other. My responsibility, as I understand it, is to honor both.
                </p>
                <p class="mobile-hide">
                    I treat the skin with the rigor it deserves, and the person sitting in front of me with the attention they deserve. Every consultation begins with listening — what brings you here, what you hope for, and just as importantly, what you do not want.
                </p>
                <p class="mobile-hide">
                    I do not believe in pushing what isn't needed. I believe in clear conversation, conservative judgment, and results that age gracefully. The treatments we offer at Mili Sinchon are the ones I would choose for the people closest to me.
                </p>
                <p>
                    To everyone who chooses Mili Clinic Sinchon, my commitment is simple: <strong>nothing less than what I would want for myself</strong> — and nothing for the sake of it.
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
                    Medicine that earns
                    <span class="line-2">its results.</span>
                </h2>
                <p class="first-letter">
                    The technology in dermatology has advanced remarkably in the past decade — but technology alone does not make a treatment work. What makes it work is judgment.
                </p>
                <p class="mobile-hide">
                    Knowing when to use which tool, how to layer protocols, when to wait, and when not to treat at all. That judgment comes from clinical experience — from years of seeing what works, what fades, and what holds up over time.
                </p>
                <p class="mobile-hide">
                    My approach is grounded in this discipline. I would rather under-promise and let the result speak than the reverse. When you choose Mili Sinchon, you are choosing a practice that takes the long view.
                </p>
                <p>
                    Your skin five years from now matters as much as how it looks tomorrow — and <strong>the best aesthetic outcomes are cultivated, not delivered</strong>.
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

# CSS additions: director-grid-reverse and director-alt
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
        print("ERROR: en/about.html not found")
        return

    content = f.read_text(encoding='utf-8')

    # 1. Replace the entire single director section with the two-director block
    pattern = r'<!-- Director\'s Message -->.*?</section>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, NEW_DIRECTOR_BLOCK, content, count=1, flags=re.DOTALL)
        print("OK   Replaced director section with two-director block")
    else:
        print("WARN Director section pattern not found")

    # 2. Inject director-grid-reverse and director-alt CSS into the main <style> block
    # Find the last director-related rule and add new rules right after the closing brace section
    if '.director-grid-reverse' not in content:
        # Insert after .director-portrait img{...} block, before media queries for director
        # Find the @media line that contains director rules
        media_pattern = r'(@media \(max-width: 900px\)\{\s*.director-grid\{grid-template-columns: 1fr)'
        if re.search(media_pattern, content):
            content = re.sub(
                media_pattern,
                CSS_ADDITIONS + r'\1',
                content,
                count=1
            )
            print("OK   Injected director-grid-reverse CSS")
        else:
            # Fallback: inject before closing </style>
            content = content.replace('</style>', CSS_ADDITIONS + '</style>', 1)
            print("OK   Injected director-grid-reverse CSS (fallback location)")

    f.write_text(content, encoding='utf-8')
    print("\n=== Done ===")

    # Verification
    new_content = f.read_text(encoding='utf-8')
    print(f"Kim Hye-won mentions: {new_content.count('Kim Hye-won')}")
    print(f"Kim Myung-hwan mentions: {new_content.count('Kim Myung-hwan')}")
    print(f"director-grid-reverse: {new_content.count('director-grid-reverse')}")

if __name__ == '__main__':
    main()
