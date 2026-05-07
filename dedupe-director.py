#!/usr/bin/env python3
"""
Remove the duplicate Dr. Kim Myung-hwan section from about.html.
Keeps the first one, removes any subsequent duplicates.
"""
import re
from pathlib import Path

f = Path('en/about.html')
content = f.read_text(encoding='utf-8')

# Find all Kim Myung-hwan section blocks
pattern = r"<!-- Director's Message — Dr\. Kim Myung-hwan -->.*?</section>"
matches = list(re.finditer(pattern, content, re.DOTALL))

print(f"Found {len(matches)} Dr. Kim Myung-hwan sections")

if len(matches) <= 1:
    print("No duplicates to remove. Exiting.")
else:
    # Remove all duplicates after the first one (work from last to first to keep offsets stable)
    for m in reversed(matches[1:]):
        content = content[:m.start()] + content[m.end():]
        print(f"Removed duplicate at position {m.start()}")
    
    # Clean up any trailing empty lines between sections
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    f.write_text(content, encoding='utf-8')
    print(f"\nDone. Kept 1, removed {len(matches) - 1} duplicate(s).")

# Verify
after = f.read_text(encoding='utf-8')
print("")
print("=== After ===")
kh = after.count("Dr. Kim Hye-won")
km = after.count("Dr. Kim Myung-hwan")
print(f"Kim Hye-won section markers: {kh}")
print(f"Kim Myung-hwan section markers: {km}")
print(f"(Each should be 1 in the comment markers)")
