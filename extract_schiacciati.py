#!/usr/bin/env python3
import re

# Read the source file with all crushed characters
with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/nuovocon tutto.svg', 'r') as f:
    source = f.read()

# Read current index.html
with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/index.html', 'r') as f:
    index = f.read()

# Extract schiacciato groups
schiacciati = []
for name in ['blu_schiacciato', 'arancione_schiacciato', 'rosso_schiacciato', 'viola_schiacciato', 'verde_schiacciato']:
    pattern = f'<g id="{name}"[^>]*>.*?</g>'
    match = re.search(pattern, source, re.DOTALL)
    if match:
        schiacciati.append(match.group(0))
        print(f"Found {name}: {len(match.group(0))} chars")
    else:
        print(f"NOT FOUND: {name}")

# Find position after giallo_schiacciato in index.html
giallo_end = index.find('</g>\n\n  <g id="viola">')
if giallo_end == -1:
    print("ERROR: Could not find insertion point")
    exit(1)

# Insert all schiacciati after giallo_schiacciato
insertion = '\n\n'.join(schiacciati)
new_index = index[:giallo_end + 4] + '\n\n' + insertion + index[giallo_end + 4:]

# Write updated index.html
with open('/Users/tommyfrostmiconi/Documents/GitHub/bambino palloncino/index.html', 'w') as f:
    f.write(new_index)

print(f"\nInserted {len(schiacciati)} schiacciati groups")
print(f"New file size: {len(new_index)} chars")
