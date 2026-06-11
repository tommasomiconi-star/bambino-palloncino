# Giallo Schiacciato — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Creare una pagina `index.html` auto-contenuta che mostri l'animazione della pressa che schiaccia Giallo e fa apparire GialloSchiacciato.

**Architecture:** File HTML singolo con SVG inline combinato dal poster esistente + pressa importata, CSS embedded per animazioni `@keyframes`, JS inline per sincronizzazione temporale dei cambi di visibilità.

**Tech Stack:** HTML5, CSS3 Animations, Vanilla JS, SVG inline. Nessuna dipendenza esterna.

---

### Task 1: Struttura HTML base con poster SVG inline

**Files:**
- Create: `index.html`

**Note:** Il poster SVG (`poster bambini.svg`) è ~873 linee. Lo inseriremo integralmente inline tramite comandi bash, poi modificheremo.

- [ ] **Step 1: Creare il wrapper HTML5**

```html
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Giallo Schiacciato</title>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: #000;
    }
    #stage {
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    svg {
      max-height: 100vh;
      max-width: 100vw;
    }
  </style>
</head>
<body>
  <div id="stage">
    <!-- SVG verrà inserito qui -->
  </div>
</body>
</html>
```

- [ ] **Step 2: Inserire il poster SVG inline**

Leggere il contenuto di `poster bambini.svg` e inserirlo dentro `<div id="stage">`, sostituendo il commento.

Comandi bash (esempio):
```bash
# Estrarre contenuto SVG (senza la prima riga <?xml...)
tail -n +2 "poster bambini.svg" > poster_content.svg
```

Poi inserire il contenuto dentro il wrapper HTML tra `<div id="stage">` e `</div>`.

- [ ] **Step 3: Verificare visualizzazione statica**

Aprire `index.html` nel browser. Deve mostrare il poster completo con Giallo visibile.

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: base HTML with poster SVG inline"
```

---

### Task 2: Nascondere GialloSchiacciato e aggiungere la pressa

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Nascondere `giallo_schiacciato` all'avvio**

Trovare nel SVG:
```xml
<g id="giallo_schiacciato" data-name="giallo schiacciato">
```

Modificare in:
```xml
<g id="giallo_schiacciato" data-name="giallo schiacciato" style="visibility:hidden">
```

- [ ] **Step 2: Estrarre la pressa dal file lattina**

Leggere `bambino lattina [Recuperato].svg`. I path principali sono:
- Path grigio (`cls-1`): il corpo principale della lattina
- Path nero: la parte superiore
- Polygon gialli (`cls-2`): i dettagli della pressa

- [ ] **Step 3: Inserire la pressa come nuovo gruppo SVG**

Aggiungere un nuovo `<g id="pressa">` dentro il SVG del poster, posizionato sopra Giallo.

**Posizionamento target:**
- Giallo è centrato approssimativamente a x≈867, y≈850-1100
- La pressa deve essere centrata orizzontalmente su Giallo
- Offset verticale iniziale: la pressa parte da y≈-400 (fuori schermo superiore)
- Scala: la lattina originale è larga ~1464px, va scalata a ~200px per coprire Giallo

Codice da inserire (dopo il gruppo `giallo`, dentro l'SVG):

```xml
<g id="pressa" style="transform: translateY(-1200px); transform-origin: 867px 0;">
  <!-- Scala ~0.14 per adattare la lattina alle dimensioni di Giallo -->
  <g transform="translate(720, 600) scale(0.14)">
    <!-- Copia i path dalla lattina qui -->
    <path fill="#636363" d="M1016.81,1463.37h0c-70.77,37-155.18,37-225.95,0h0V161.62h225.95v1301.75Z"/>
    <g>
      <path d="M1016.81,1326.16h0c-72.03,11.56-145.41,11.98-217.56,1.25l-8.38-1.25v-23.49l10.56,1.54c70.73,10.31,142.61,9.9,213.23-1.2l2.16-.34v23.49Z"/>
      <polygon fill="#ffda00" points="819.97 1330.06 800.75 1327.68 811.55 1305.35 830.78 1307.73 819.97 1330.06"/>
      <polygon fill="#ffda00" points="859.49 1333.75 840.15 1332.67 849.43 1309.67 868.78 1310.74 859.49 1333.75"/>
      <polygon fill="#ffda00" points="900.98 1335.15 881.71 1334.8 889.67 1311.57 909.04 1311.62 900.98 1335.15"/>
      <polygon fill="#ffda00" points="939.3 1334.4 919.98 1335 927.06 1311.29 946.35 1310.39 939.3 1334.4"/>
      <polygon fill="#ffda00" points="981.64 1330.91 962.71 1332.73 969.2 1308.56 988.78 1306.61 981.64 1330.91"/>
      <polygon fill="#ffda00" points="1016.81 1302.67 1010.27 1303.54 1004.7 1328 1016.81 1326.16 1016.81 1302.67"/>
    </g>
  </g>
</g>
```

**Nota:** Le coordinate di `translate(720, 600)` e `scale(0.14)` sono iniziali e potrebbero necessitare di aggiustamento in base al test visivo. Il centro di Giallo è approssimativamente x≈867, y≈950.

- [ ] **Step 4: Verificare posizionamento**

Aprire `index.html` nel browser. La pressa deve essere:
- Inizialmente fuori schermo (in alto)
- Dimensionata per coprire Giallo quando scende
- Visibile come elemento sopra il poster

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add pressa (lattina) and hide giallo_schiacciato"
```

---

### Task 3: CSS Animations

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Aggiungere `@keyframes` per la pressa**

Inserire nel `<style>` nel `<head>`:

```css
@keyframes pressaAnim {
  0%   { transform: translateY(-1200px); }
  28%  { transform: translateY(0); }       /* arrivo su Giallo ~1.5s */
  34%  { transform: translateY(0); }       /* pausa sul fondo ~0.3s */
  100% { transform: translateY(-1200px); } /* risalita lenta fino a 5.3s */
}

#pressa {
  animation: pressaAnim 5.3s ease-in-out infinite;
}
```

**Spiegazione timing:**
- 0% → 28% = discesa rapida (~1.5s), ease-in accelera
- 28% → 34% = pausa ferma sul fondo (~0.3s)
- 34% → 100% = risalita lenta (~3.5s), ease-out decelera
- `ease-in-out` fornisce ease-in nella prima metà e ease-out nella seconda

- [ ] **Step 2: Verificare animazione**

Aprire `index.html` nel browser. La pressa deve:
- Scendere velocemente dall'alto
- Fermarsi brevemente sul fondo
- Risalire lentamente
- Ricominciare in loop infinito

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add CSS animation for pressa movement"
```

---

### Task 4: JS Sincronizzazione visibilità

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Aggiungere script di sincronizzazione**

Aggiungere prima del tag di chiusura `</body>`:

```javascript
<script>
(function() {
  const giallo = document.getElementById('giallo');
  const gialloSchiacciato = document.getElementById('giallo_schiacciato');
  const pressa = document.getElementById('pressa');
  
  if (!giallo || !gialloSchiacciato || !pressa) {
    console.error('Elementi non trovati');
    return;
  }
  
  // Sincronizzazione per ogni ciclo di animazione
  function syncVisibility() {
    // Stato iniziale: Giallo visibile, schiacciato nascosto
    giallo.style.visibility = 'visible';
    gialloSchiacciato.style.visibility = 'hidden';
    
    // Al ~24.5% del ciclo (1.3s su 5.3s): Giallo scompare quando la pressa copre
    setTimeout(() => {
      giallo.style.visibility = 'hidden';
    }, 1300);
    
    // Al ~81% del ciclo (4.3s su 5.3s): GialloSchiacciato appare dopo risalita
    setTimeout(() => {
      gialloSchiacciato.style.visibility = 'visible';
    }, 4300);
  }
  
  // Avvia sincronizzazione all'inizio
  syncVisibility();
  
  // Sincronizza ad ogni iterazione dell'animazione CSS
  pressa.addEventListener('animationiteration', syncVisibility);
})();
</script>
```

- [ ] **Step 2: Verificare sincronizzazione**

Nel browser:
- Giallo è visibile all'inizio
- Quando la pressa scende e copre Giallo (1.3s), Giallo scompare
- La pressa risale lentamente
- Quando la pressa è risalita (4.3s), GialloSchiacciato appare
- Il ciclo ricomincia correttamente

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: add JS sync for giallo visibility states"
```

---

### Task 5: Test Finale e Polish

**Files:**
- Modify: `index.html` (se necessario aggiustamenti)

- [ ] **Step 1: Verificare timing e loop**

Osservare 3 cicli completi dell'animazione. Controllare:
- La pressa scende velocemente (non troppo lenta)
- La pausa sul fondo è breve ma percettibile
- La risalita è chiaramente più lenta della discesa
- Giallo scompare al momento giusto (quando la pressa lo copre)
- GialloSchiacciato appare quando la pressa è tornata su
- Nessun flicker o flash visivo durante i cambi di stato

- [ ] **Step 2: Verificare funzionamento senza server**

Aprire il file direttamente nel browser:
- macOS: `open index.html`
- Oppure doppio click sul file

Deve funzionare perfettamente da `file://` senza alcun server.

- [ ] **Step 3: Verificare responsive / viewport**

Il poster deve:
- Occupare l'intera altezza dello schermo
- Mantenere le proporzioni
- Centrarsi orizzontalmente e verticalmente
- Non mostrare scrollbars

- [ ] **Step 4: Aggiustamenti finali (se necessario)**

Se i tempi non sono perfetti:
- Modificare le percentuali nel `@keyframes`
- Modificare i millisecondi nei `setTimeout` del JS
- La durata totale è 5.3s = 5300ms
  - 24.5% = 1300ms (scomparsa Giallo)
  - 81% = 4300ms (comparsa GialloSchiacciato)

- [ ] **Step 5: Commit finale**

```bash
git add index.html
git commit -m "feat: complete animation with final timing adjustments"
```

---

## Spec Coverage Check

| Requisito Spec | Task che lo implementa |
|----------------|------------------------|
| Pagina singola HTML | Task 1 |
| Nessun server richiesto | Task 1, Task 5 |
| Pressa scende veloce | Task 3 (CSS keyframes, 28% ease-in) |
| Giallo scompare quando coperto | Task 4 (JS setTimeout a 1300ms) |
| Pressa risale lenta | Task 3 (CSS keyframes, 66% ease-out) |
| GialloSchiacciato appare dopo | Task 4 (JS setTimeout a 4300ms) |
| Loop infinito | Task 3 (infinite), Task 4 (animationiteration) |
| Pressa centrata su Giallo | Task 2 (translate 720, scale 0.14) |
| File autonomo | Tutti i task (inline SVG/CSS/JS) |

## Placeholder Scan

- Nessun TBD, TODO, o placeholder
- Nessun "implement later" o "fill in details"
- Ogni step contiene codice completo o comandi esatti
- Nessun riferimento a funzioni non definite

## Type Consistency

- ID elementi: `giallo`, `giallo_schiacciato`, `pressa` — consistenti in tutto il piano
- Durata animazione: 5.3s = 5300ms — usata in CSS e JS
- Timing percentuali: 28%, 34% — corrispondenti ai millisecondi del JS

---

*Piano pronto per l'esecuzione.*
