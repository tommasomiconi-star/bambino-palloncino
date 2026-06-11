#!/usr/bin/env python3
import re

with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/nuovocon tutto.svg', 'r') as f:
    source = f.read()

with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/index.html', 'r') as f:
    index = f.read()

# Extract each schiacciato group properly
# We need to handle nested <g> elements
def extract_group(text, group_id):
    start = text.find(f'<g id="{group_id}"')
    if start == -1:
        return None
    
    # Find the matching closing </g>
    pos = start + len(f'<g id="{group_id}"')
    depth = 1
    while pos < len(text) and depth > 0:
        if text[pos:pos+2] == '<g':
            depth += 1
            pos += 2
        elif text[pos:pos+3] == '</g':
            depth -= 1
            pos += 3
        else:
            pos += 1
    
    return text[start:pos] if depth == 0 else None

# Extract all schiacciati
names = ['blu_schiacciato', 'arancione_schiacciato', 'rosso_schiacciato', 'viola_schiacciato', 'verde_schiacciato']
extracted = []
for name in names:
    group = extract_group(source, name)
    if group:
        # Add style="visibility:hidden"
        # Replace data-name with standard format
        group = group.replace('>', ' style="visibility:hidden">', 1)
        extracted.append(group)
        print(f"✓ {name}: {len(group)} chars")
    else:
        print(f"✗ {name}: NOT FOUND")

# Find insertion point: after giallo_schiacciato closing tag
# Look for the pattern: </g> followed by blank line then <g id="viola">
insert_marker = '</g>\n\n  <g id="viola"'
insert_pos = index.find(insert_marker)
if insert_pos == -1:
    print("ERROR: Could not find insertion point")
    exit(1)

# Insert all groups
insertion = '\n\n  ' + '\n\n  '.join(extracted)
new_index = index[:insert_pos + 4] + '\n\n' + insertion + '\n\n  ' + index[insert_pos + 6:]

with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/index.html', 'w') as f:
    f.write(new_index)

print(f"\n✓ Updated index.html with {len(extracted)} groups")
print(f"  Total size: {len(new_index)} chars")
