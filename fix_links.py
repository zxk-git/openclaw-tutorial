#!/usr/bin/env python3
"""Fix broken links across all tutorial .md files."""
import os, re

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Build filename map
actual_files = [f for f in os.listdir(PROJECT_DIR) if f.endswith(".md")]
print(f"Found {len(actual_files)} .md files")

def normalize(name):
    name = name.replace("%20", " ")
    name = re.sub(r"\s+", " ", name)
    return name.strip()

file_map = {}
for f in actual_files:
    file_map[normalize(f)] = f

# Track fixes
all_fixes = []

def process_file(fname):
    filepath = os.path.join(PROJECT_DIR, fname)
    with open(filepath, encoding="utf-8") as fh:
        text = fh.read()
    
    original = text
    fixes = []
    
    # Fix 1: .md links with %20 encoding / extra space issues
    def fix_md_link(m):
        full = m.group(0)
        prefix = m.group(1)
        target = m.group(2)
        suffix = m.group(3)
        
        if target.startswith("http") or target.startswith("mailto:"):
            return full
        
        # Split anchor
        anchor = ""
        file_part = target
        if "#" in target and not target.startswith("#"):
            idx = target.index("#")
            file_part = target[:idx]
            anchor = target[idx:]
        
        norm = normalize(file_part)
        if norm in file_map and file_map[norm] != file_part:
            new_file = file_map[norm]
            fixes.append(f"  FILE: {file_part} → {new_file}")
            return f"{prefix}{new_file}{anchor}{suffix}"
        
        return full
    
    text = re.sub(r'(\[[^\]]*\]\()([^)]+?)(\))', fix_md_link, text)
    
    # Fix 2: Anchor-only links: spaces → hyphens
    def fix_anchor(m):
        prefix = m.group(1)
        anchor = m.group(2)
        if " " in anchor:
            fixed = anchor.replace(" ", "-")
            fixes.append(f"  ANCHOR: #{anchor} → #{fixed}")
            return f"{prefix}{fixed})"
        return m.group(0)
    
    text = re.sub(r'(\[[^\]]*\]\(#)([^)]+)\)', fix_anchor, text)
    
    # Fix 3: Also fix anchors in file+anchor links
    def fix_file_anchor(m):
        prefix = m.group(1)
        file_part = m.group(2)
        anchor = m.group(3)
        suffix = m.group(4)
        if " " in anchor:
            fixed = anchor.replace(" ", "-")
            fixes.append(f"  FILE+ANCHOR: #{anchor} → #{fixed}")
            return f"{prefix}{file_part}#{fixed}{suffix}"
        return m.group(0)
    
    text = re.sub(r'(\[[^\]]*\]\()([^)#]+)#([^)]+)(\))', fix_file_anchor, text)
    
    # Fix 4: Reddit links missing domain
    def fix_reddit(m):
        path = m.group(1)
        fixes.append(f"  REDDIT: /{path} → https://reddit.com/{path}")
        return f"](https://reddit.com/{path})"
    
    text = re.sub(r'\]\(/(r/[^)]+)\)', fix_reddit, text)
    text = re.sub(r'\]\(/(user/[^)]+)\)', fix_reddit, text)
    
    if text != original:
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"\n✅ {fname}: {len(fixes)} fixes")
        for f in fixes[:8]:
            print(f)
        if len(fixes) > 8:
            print(f"  ... and {len(fixes) - 8} more")
        all_fixes.extend(fixes)

for fname in sorted(actual_files):
    process_file(fname)

print(f"\n{'='*50}")
print(f"Total fixes applied: {len(all_fixes)}")
