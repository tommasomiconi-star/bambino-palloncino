# AGENTS.md — Giallo Schiacciato

## Context

- **Format**: Single HTML page (`index.html`)
- **Base file**: `poster bambini.svg` (1080×1920) containing multiple colored characters
- **Press source**: `nuovo.svg` (contains the press/lattina element)
- **Goal**: Auto-playing animation of a press descending to crush Giallo
- **Constraint**: Must work without any development server (`file://` compatible)
- **Stack**: Inline HTML5, SVG, CSS Animations, Vanilla JavaScript

## Animation Sequence

1. **0.0s** — `giallo` is visible, `giallo_schiacciato` is hidden (`visibility:hidden`), press starts off-screen at top
2. **0.0s → 0.8s** — Press descends rapidly from `translateY(-1200px)` to `translateY(0)` (ease-in)
3. **0.8s** — Press covers Giallo → Giallo instantly hides AND `giallo_schiacciato` appears immediately underneath
4. **0.8s → 1.0s** — Brief pause with press stationary
5. **1.0s → 4.2s** — Press rises slowly back to top (ease-out)
6. **4.2s → 5.3s** — Pause at top before loop restarts
7. **Loop**: Infinite animation cycle

## Design Decisions

- **Approach**: CSS `@keyframes` + JS `setTimeout` synchronization
- **Press positioning**: `translate(-50, 0) scale(1)` within the SVG — perfectly centered over Giallo
- **Z-order**: Press is placed after `giallo` in DOM order so it paints on top
- **Visibility method**: JavaScript toggles `element.style.visibility` (not `display`) to preserve layout

## SVG Structure in index.html

- **Base**: `poster bambini.svg` with all its `<defs>` (gradients, patterns, CSS classes)
- **Press**: Extracted from `nuovo.svg`, paths inserted as `<g id="pressa">` with inline `fill` attributes
- **Characters**: `giallo` (visible), `giallo_schiacciato` (initially hidden via inline `style`)

## CSS Animation

```css
@keyframes pressaAnim {
  0%   { transform: translateY(-1200px); }
  15%  { transform: translateY(0); }
  20%  { transform: translateY(0); }
  80%  { transform: translateY(-1200px); }
  100% { transform: translateY(-1200px); }
}
#pressa {
  animation: pressaAnim 5.3s ease-in-out infinite;
}
```

## JavaScript Synchronization

```javascript
function syncVisibility() {
  giallo.style.visibility = 'visible';
  gialloSchiacciato.style.visibility = 'hidden';

  setTimeout(() => {
    giallo.style.visibility = 'hidden';
    gialloSchiacciato.style.visibility = 'visible'; // appears immediately
  }, 800);
}

syncVisibility();
pressa.addEventListener('animationiteration', syncVisibility);
```

## Input Files

| File | Purpose | Status |
|------|---------|--------|
| `poster bambini.svg` | Base poster with all characters + `giallo` + `giallo_schiacciato` | **Used as base** |
| `nuovo.svg` | Contains the press (`id="pressa"`) | **Used for press element** |
| `bambino lattina [Recuperato].svg` | Alternative press asset | Not used in final |
| `nuovocon tutto.svg` | Contains press + crushed versions | Not used in final |

## Output File

- `index.html` — Self-contained single file with inline SVG, CSS, and JS

## Viewport

- `viewBox="0 0 1080 1920"` (portrait, matching the poster)
- Fullscreen centered display with `max-height: 100vh; max-width: 100vw`
- Black background

## Designer Notes

- This is a designer-led project — no technical questions were asked to the user
- The designer confirmed: automatic playback, loop, single file, no server
- All positioning and timing were adjusted visually based on designer feedback

---

*Document automatically generated from conversation history.*
