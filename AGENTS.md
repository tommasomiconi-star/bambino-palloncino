# AGENTS.md — Tutti i Bambini Schiacciati

## Context

- **Format**: Single HTML page (`index.html`)
- **Base file**: `poster bambini.svg` (1080×1920) containing multiple colored characters
- **Press source**: `nuovo.svg` (contains the press/lattina element)
- **Goal**: Auto-playing animation of a press visiting all 6 characters in sequence, crushing each one and leaving all crushed versions visible at the end
- **Constraint**: Must work without any development server (`file://` compatible)
- **Stack**: Inline HTML5, SVG, CSS Animations, Vanilla JavaScript

## Characters (6 total)

All characters have a normal version and a crushed (`*_schiacciato`) version.

| Color | Normal ID | Crushed ID | Position (rough) |
|-------|-----------|------------|------------------|
| **Giallo** (Yellow) | `giallo` | `giallo_schiacciato` | Bottom-center |
| **Viola** (Purple) | `viola` | `viola_schiacciato` | Right of Giallo |
| **Verde** (Green) | `verde` | `verde_schiacciato` | Left of Giallo |
| **Blu** (Blue) | `blu` | `blu_schiacciato` | Above Giallo |
| **Arancione** (Orange) | `arancione` | `arancione_schiacciato` | Above-Verde (left) |
| **Rosso** (Red) | `rosso` | `rosso_schiacciato` | Above-Viola (right) |

**Press horizontal offsets** (relative to Giallo at x=0):
- Giallo: `translateX(0)`
- Viola: `translateX(-320px)` — press moves LEFT 320px
- Verde: `translateX(-640px)` — press moves LEFT 640px
- Blu: `translateX(0)` — same column as Giallo but higher up
- Arancione: `translateX(-320px)` — same column as Viola, higher up
- Rosso: `translateX(-640px)` — same column as Verde, higher up

## Animation Sequence (Full Cycle: 15s)

| Time | Action | Character |
|------|--------|-----------|
| **0.0s** | All normal characters visible, all crushed hidden, press at top | — |
| **0.0s → 0.8s** | Press descends to Giallo | Giallo |
| **0.8s** | Crush: Giallo hides → `giallo_schiacciato` appears | Giallo |
| **0.8s → 1.0s** | Brief pause | — |
| **1.0s → 2.0s** | Press rises back to top | — |
| **2.0s → 3.0s** | Pause + move LEFT 320px to Viola | — |
| **3.0s → 3.8s** | Press descends to Viola | Viola |
| **3.8s** | Crush: Viola hides → `viola_schiacciato` appears | Viola |
| **3.8s → 4.0s** | Brief pause | — |
| **4.0s → 5.0s** | Press rises | — |
| **5.0s → 6.0s** | Pause + move LEFT 320px more to Verde | — |
| **6.0s → 6.8s** | Press descends to Verde | Verde |
| **6.8s** | Crush: Verde hides → `verde_schiacciato` appears | Verde |
| **6.8s → 7.0s** | Brief pause | — |
| **7.0s → 8.0s** | Press rises | — |
| **8.0s → 9.0s** | Pause + move RIGHT 640px to Blu column | — |
| **9.0s → 9.8s** | Press descends to Blu | Blu |
| **9.8s** | Crush: Blu hides → `blu_schiacciato` appears | Blu |
| **9.8s → 10.0s** | Brief pause | — |
| **10.0s → 11.0s** | Press rises | — |
| **11.0s → 12.0s** | Pause + move LEFT 320px to Arancione | — |
| **12.0s → 12.8s** | Press descends to Arancione | Arancione |
| **12.8s** | Crush: Arancione hides → `arancione_schiacciato` appears | Arancione |
| **12.8s → 13.0s** | Brief pause | — |
| **13.0s → 14.0s** | Press rises | — |
| **14.0s → 15.0s** | Pause + move LEFT 320px to Rosso | — |
| **15.0s → 15.8s** | Press descends to Rosso | Rosso |
| **15.8s** | Crush: Rosso hides → `rosso_schiacciato` appears | Rosso |
| **15.8s → 16.0s** | Brief pause | — |
| **16.0s → 17.0s** | Press rises | — |
| **17.0s → 18.0s** | Pause at top | — |
| **~18.0s** | Loop restarts — all reset to normal, press returns to Giallo start | — |

## Design Decisions

- **Approach**: CSS `@keyframes` + JS `setTimeout` synchronization
- **Press positioning**: `translate(x, y)` within the SVG — moves both horizontally and vertically
- **Z-order**: Press is placed after ALL characters in DOM order so it paints on top
- **Visibility method**: JavaScript toggles `element.style.visibility` (not `display`) to preserve layout
- **Crushed characters source**: Extracted from `nuovocon tutto.svg` and pasted as inline SVG groups
- **Animation restarts**: After all 6 are crushed, the animation loops infinitely

## SVG Structure in index.html

- **Base**: `poster bambini.svg` with all its `<defs>` (gradients, patterns, CSS classes)
- **Crushed characters**: Extracted from `nuovocon tutto.svg`, inserted before normal characters
- **Normal characters**: `giallo`, `viola`, `verde`, `blu`, `arancione`, `rosso`
- **Press**: `<g id="pressa">` with inline `fill` attributes, positioned via `transform`

## CSS Animation

```css
@keyframes pressaAnim {
  /* Giallo */
  0%      { transform: translate(0, -1200px); }
  5.3%    { transform: translate(0, 10px); }
  6.7%    { transform: translate(0, 10px); }
  13.3%   { transform: translate(0, -1200px); }
  /* Move to Viola */
  15.3%   { transform: translate(-320px, -1200px); }
  /* Viola */
  20.7%   { transform: translate(-320px, 10px); }
  22.0%   { transform: translate(-320px, 10px); }
  28.7%   { transform: translate(-320px, -1200px); }
  /* Move to Verde */
  30.7%   { transform: translate(-640px, -1200px); }
  /* Verde */
  36.0%   { transform: translate(-640px, 10px); }
  37.3%   { transform: translate(-640px, 10px); }
  44.0%   { transform: translate(-640px, -1200px); }
  /* Move to Blu */
  46.0%   { transform: translate(0, -1200px); }
  /* Blu */
  51.3%   { transform: translate(0, -440px); }
  52.7%   { transform: translate(0, -440px); }
  59.3%   { transform: translate(0, -1200px); }
  /* Move to Arancione */
  61.3%   { transform: translate(-320px, -1200px); }
  /* Arancione */
  66.7%   { transform: translate(-320px, -440px); }
  68.0%   { transform: translate(-320px, -440px); }
  74.7%   { transform: translate(-320px, -1200px); }
  /* Move to Rosso */
  76.7%   { transform: translate(-640px, -1200px); }
  /* Rosso */
  82.0%   { transform: translate(-640px, -440px); }
  83.3%   { transform: translate(-640px, -440px); }
  90.0%   { transform: translate(-640px, -1200px); }
  /* Stay at top */
  100%    { transform: translate(-640px, -1200px); }
}
#pressa {
  animation: pressaAnim 15s ease-in-out infinite;
}
```

## JavaScript Synchronization

```javascript
const chars = {
  giallo: { normal: 'giallo', crushed: 'giallo_schiacciato' },
  viola: { normal: 'viola', crushed: 'viola_schiacciato' },
  verde: { normal: 'verde', crushed: 'verde_schiacciato' },
  blu: { normal: 'blu', crushed: 'blu_schiacciato' },
  arancione: { normal: 'arancione', crushed: 'arancione_schiacciato' },
  rosso: { normal: 'rosso', crushed: 'rosso_schiacciato' }
};

// Initial state: all normal visible, all crushed hidden
function resetAll() { ... }

// Crush a character (hide normal, show crushed)
function crush(name) { ... }

// Sequence timing (ms, matching CSS animation):
// Giallo @ 0.8s, Viola @ 3.0s, Verde @ 6.0s, Blu @ 9.0s, Arancione @ 12.0s, Rosso @ 15.0s
```

## Input Files

| File | Purpose | Status |
|------|---------|--------|
| `poster bambini.svg` | Base poster with all characters + `giallo` + `giallo_schiacciato` | **Used as base** |
| `nuovo.svg` | Contains the press (`id="pressa"`) | **Used for press element** |
| `nuovocon tutto.svg` | Contains all crushed versions (blu, arancione, rosso, viola, verde) | **Used for crushed characters** |
| `bambino lattina [Recuperato].svg` | Alternative press asset | Not used in final |

## Output File

- `index.html` — Self-contained single file with inline SVG, CSS, and JS (~122 KB)

## Viewport

- `viewBox="0 0 1080 1920"` (portrait, matching the poster)
- Fullscreen centered display with `max-height: 100vh; max-width: 100vw`
- Black background

## How to Modify the Animation

### Adjusting press position for a character:
1. Find the character's `<g>` in the SVG
2. Note its approximate x/y coordinates
3. Adjust the `translate(x, y)` values in the CSS `@keyframes`
4. Update the corresponding `setTimeout` timing in JavaScript

### Adding a new character:
1. Create both normal and `_schiacciato` versions in the SVG
2. Add entries to the `chars` object in JavaScript
3. Add keyframe steps to the CSS animation
4. Add a `setTimeout` call in the JS sequence

## Designer Notes

- This is a designer-led project — no technical questions were asked to the user
- The designer confirmed: automatic playback, loop, single file, no server
- All positioning and timing were adjusted visually based on designer feedback
- The animation loops infinitely: after crushing all 6, everything resets and starts over

---

*Document updated after extending animation to all 6 characters.*
