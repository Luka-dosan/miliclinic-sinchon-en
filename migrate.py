#!/usr/bin/env python3
"""
Mili Clinic Sinchon - Final migration script
- Maps Dosan treatment links to Sinchon equivalents
- Updates titles for new treatment pages
"""
import re
from pathlib import Path

NEW_PAGES = {
    'oligio-x.html': ('OligioX', 'Oligio X next-generation monopolar RF lifting'),
    'inmode.html': ('InMode', 'InMode RF microneedling and lifting'),
    'shurink.html': ('Shurink', 'Shurink non-invasive HIFU lifting'),
    'botox.html': ('Botox', 'Botox wrinkle and contour treatment'),
    'filler.html': ('Filler', 'Filler volume restoration'),
    'collagen-booster.html': ('Collagen Booster', 'Collagen Booster biostimulator injection'),
    'thread-lifting.html': ('Thread Lifting', 'Thread Lifting PDO PCL absorbable threads'),
    'acne-pore.html': ('Acne and Pore', 'Acne and Pore targeted skin clarity program'),
    'body-shaping.html': ('Body Shaping', 'Body Shaping non-surgical contouring'),
}

DOSAN_TO_SINCHON_LINKS = [
    ('thermage.html', 'oligio-x.html'),
    ('reborn-cell.html', 'collagen-booster.html'),
    ('fit-culptra.html', 'collagen-booster.html'),
    ('silhouette-soft.html', 'thread-lifting.html'),
    ('sculptra.html', 'collagen-booster.html'),
    ('juvelook.html', 'collagen-booster.html'),
    ('juvederm.html', 'filler.html'),
    ('derma-renewal.html', 'acne-pore.html'),
    ('anti-trouble.html', 'acne-pore.html'),
    ('highend-medispa.html', 'medi-spa.html'),
    ('medispa.html', 'medi-spa.html'),
]

DOSAN_TO_SINCHON_NAMES = [
    ('>Thermage<', '>OligioX<'),
    ('>Reborn Cell<', '>Collagen Booster<'),
    ('>Fit&middot;Culptra<', '>Collagen Booster<'),
    ('>Silhouette Soft<', '>Thread Lifting<'),
    ('>Sculptra<', '>Collagen Booster<'),
    ('>Juvelook<', '>Collagen Booster<'),
    ('>Juv&eacute;derm<', '>Filler<'),
    ('>Derma Renewal<', '>Acne and Pore<'),
    ('>Anti-Trouble<', '>Acne and Pore<'),
    ('>High-end Medi-Spa<', '>Medi-Spa<'),
    ('>Medi-Spa for Face<', '>Medi-Spa<'),
]

def main():
    en_dir = Path('en')
    if not en_dir.exists():
        print("ERROR: en/ directory not found. Run this from the repo root.")
        return
    
    all_html = list(en_dir.glob('*.html'))
    print(f"Found {len(all_html)} HTML files\n")
    
    # Step 1: Map Dosan links and names to Sinchon equivalents
    print("=== Step 1: Mapping Dosan links and names to Sinchon ===")
    count = 0
    for f in all_html:
        content = f.read_text(encoding='utf-8')
        orig = content
        
        for dosan, sinchon in DOSAN_TO_SINCHON_LINKS:
            content = content.replace('/en/' + dosan, '/en/' + sinchon)
        
        for old_name, new_name in DOSAN_TO_SINCHON_NAMES:
            content = content.replace(old_name, new_name)
        
        if content != orig:
            f.write_text(content, encoding='utf-8')
            count += 1
    print(f"Updated {count} files\n")
    
    # Step 2: Set titles and descriptions for new treatment pages
    print("=== Step 2: Setting titles for new treatment pages ===")
    for filename, (display, desc) in NEW_PAGES.items():
        f = en_dir / filename
        if not f.exists():
            print(f"  SKIP {filename} (not found)")
            continue
        
        content = f.read_text(encoding='utf-8')
        content = re.sub(
            r'<title>[^<]*</title>',
            f'<title>{display} | Mili Clinic Sinchon</title>',
            content, count=1
        )
        content = re.sub(
            r'<meta name="description" content="[^"]*"',
            f'<meta name="description" content="{desc}"',
            content, count=1
        )
        f.write_text(content, encoding='utf-8')
        print(f"  OK   {filename} -> {display}")
    
    print("\n=== Done ===")

if __name__ == '__main__':
    main()
