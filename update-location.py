#!/usr/bin/env python3
"""Update Sinchon location.html with Google Maps iframe + Bipoworks Sinchon info."""
import re
from pathlib import Path

NEW_BODY = '''<!-- Map -->
<section class="map-section">
    <div class="map-wrap">
        <div class="map-frame">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3163.024113127698!2d126.93475307620145!3d37.55449567204171!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357c9895dd9c7d71%3A0x31369a418b3105f7!2z7Iug7LSMIOuwgOumrO2BtOumrOuLiS_jg5_jg6rjg7zjgq_jg6rjg4vjg4Pjgq_mlrDmnZEvTUlMSeearuiGmuenkeaWsOadkeW6ly9TaW5jaG9uIE1pbGljbGluaWM!5e0!3m2!1sen!2skr!4v1778159238344!5m2!1sen!2skr" width="100%" height="500" style="border:0;display:block;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mili Clinic Sinchon Location"></iframe>
        </div>
        <div class="map-buttons">
            <a href="https://naver.me/GTn3wG6l" target="_blank" rel="noopener" class="map-btn">
                <div>
                    <div class="map-btn-label">Open in Naver Map</div>
                    <div class="map-btn-sub">Mapo-gu, Seoul</div>
                </div>
                <svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
            </a>
            <a href="https://maps.app.goo.gl/Q3ZdtE2xqPsaon4d7" target="_blank" rel="noopener" class="map-btn">
                <div>
                    <div class="map-btn-label">Open in Google Maps</div>
                    <div class="map-btn-sub">Mapo-gu, Seoul</div>
                </div>
                <svg viewBox="0 0 16 16"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
            </a>
        </div>
    </div>
</section>

<!-- Info Grid -->
<section class="info-section">
    <div class="container">
        <div class="info-grid">
            <div class="info-block">
                <div class="info-block-head"><span class="num">01</span><span>Getting Here</span></div>
                <h2>How to reach us.</h2>

                <div class="info-row">
                    <div class="label">Address</div>
                    <div class="value">
                        2F, 104 Sinchon-ro,<br>
                        Mapo-gu, Seoul, Korea
                        <small>&#49436;&#50872;&#53945;&#48324;&#49884; &#47560;&#54252;&#44396; &#49888;&#52768;&#47196; 104, 2&#52793;</small>
                    </div>
                </div>
                <div class="info-row">
                    <div class="label">Parking</div>
                    <div class="value">
                        Sinchon Rotary Building parking lot
                        <small>Dedicated outdoor parking behind the building</small>
                    </div>
                </div>
                <div class="info-row">
                    <div class="label">Subway</div>
                    <div class="value">
                        Sinchon Station (Line 2)<br>
                        Right in front of Exit 6
                    </div>
                </div>
                <div class="info-row">
                    <div class="label">Directions</div>
                    <div class="value">
                        <a href="https://naver.me/GTn3wG6l" target="_blank" rel="noopener">Naver Map &rarr;</a>
                        <a href="https://maps.app.goo.gl/Q3ZdtE2xqPsaon4d7" target="_blank" rel="noopener" style="margin-left:16px">Google Maps &rarr;</a>
                    </div>
                </div>
            </div>

            <div class="info-block">
                <div class="info-block-head"><span class="num">02</span><span>Clinic Hours</span></div>
                <h2>Hours of operation.</h2>

                <div class="info-row">
                    <div class="label">Mon &middot; Tue &middot; Wed &middot; Thu &middot; Fri</div>
                    <div class="value">10:00 &mdash; 20:00</div>
                </div>
                <div class="info-row">
                    <div class="label">Saturday</div>
                    <div class="value">10:00 &mdash; 16:00</div>
                </div>
                <div class="info-row">
                    <div class="label">Lunch</div>
                    <div class="value">13:00 &mdash; 14:00
                        <small>Daily</small>
                    </div>
                </div>
                <div class="info-row closed">
                    <div class="label">Sunday &middot; Holidays</div>
                    <div class="value">Closed</div>
                </div>
            </div>
        </div>
    </div>
</section>
'''

CSS_FIX = '''
.map-frame iframe{width:100%;height:500px;border:0;display:block}
@media (max-width:768px){.map-frame iframe{height:360px}}
'''


def main():
    f = Path('en/location.html')
    if not f.exists():
        print("ERROR: en/location.html not found")
        return

    content = f.read_text(encoding='utf-8')

    pat = r'<!-- Map -->.*?<section class="info-section">.*?</section>\s*</section>'
    if not re.search(pat, content, re.DOTALL):
        pat = r'<!-- Map -->.*?(?=<!-- Footer -->|<footer)'

    if re.search(pat, content, re.DOTALL):
        content = re.sub(pat, NEW_BODY.strip() + '\n\n', content, count=1, flags=re.DOTALL)
        print("OK   Body replaced")
    else:
        print("WARN Could not match body pattern")
        return

    if '.map-frame iframe' not in content:
        content = content.replace('</style>', CSS_FIX + '</style>', 1)
        print("OK   Iframe CSS fix injected")

    f.write_text(content, encoding='utf-8')
    print("\nDone")


if __name__ == '__main__':
    main()
