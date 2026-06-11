# Design: Animazione "Giallo Schiacciato" — Pressa che scende

**Data:** 2026-06-11  
**Argomento:** Animazione SVG della pressa che schiaccia Giallo  
**Stato:** ✅ Approvato  

---

## 1. Contesto

Progetto esistente con un file SVG principale `poster bambini.svg` (1080×1920) che contiene due livelli chiave:
- **`giallo`** — il personaggio Giallo intero (visibile all'inizio)
- **`giallo_schiacciato`** — il personaggio Giallo dopo essere stato schiacciato (nascosto all'inizio)

Asset aggiuntivo: `bambino lattina [Recuperato].svg` — una lattina/pressa meccanica che fungerà da oggetto che scende dall'alto.

## 2. Obiettivo

Creare una pagina `index.html` singola che:
1. Mostri il poster completo con Giallo visibile
2. Faccia scendere la pressa (lattina) dall'alto in modo rapido
3. Quando la pressa copre Giallo, questo scompare
4. La pressa risale lentamente
5. Appare GialloSchiacciato (nascosto all'inizio)
6. Funzioni senza server di sviluppo (apri e basta)

## 3. Architettura

### File unico
Un solo file `index.html` auto-contenuto con:
- SVG inline del poster + pressa
- CSS embedded per animazioni
- JS inline per sincronizzazione stati

### Layout
- Viewport: `1080×1920` (stesso del poster originale)
- La pressa è un `<g>` posizionato sopra il poster, fuori dall'area visibile iniziale
- Coordinate di riferimento: sistema originale del poster SVG

## 4. Componenti

### 4.1 Livello Giallo (personaggio intero)
- **ID:** `giallo`
- **Stato iniziale:** `visibility: visible`
- **Stato finale:** `visibility: hidden`
- **Trigger:** scompare quando la pressa lo copre

### 4.2 Livello GialloSchiacciato
- **ID:** `giallo_schiacciato`
- **Stato iniziale:** `visibility: hidden`
- **Stato finale:** `visibility: visible`
- **Trigger:** appare dopo che la pressa è risalita

### 4.3 Pressa (lattina)
- **Asset:** `bambino lattina [Recuperato].svg`
- **Stato iniziale:** posizionata sopra il viewport (y ≈ -200)
- **Movimento:** `transform: translateY()` con CSS `@keyframes`
- **Nota:** la lattina ha viewBox proprio, verrà scalata e posizionata per coprire Giallo

## 5. Sequenza Animazione (Timeline)

| Step | Durata | Azione |
|------|--------|--------|
| 0.0s | — | Giallo visibile, pressa fuori schermo in alto, GialloSchiacciato nascosto |
| 0.0s | 1.5s | Pressa scende velocemente (`ease-in`) |
| 1.3s | istantaneo | Giallo scompare (quando pressa lo copre) |
| 1.5s | 0.3s | Pausa — pressa ferma sul fondo |
| 1.8s | 2.5s | Pressa risale lentamente (`ease-out`) |
| 4.3s | istantaneo | GialloSchiacciato appare |
| 4.3s | 1.0s | Pausa in alto — pressa ferma fuori schermo |
| 5.3s | — | Loop ricomincia (opzionale, configurabile) |

**Nota:** i tempi sono configurabili tramite variabili CSS o proprietà JS.

## 6. Implementazione Tecnica

### 6.1 CSS
```css
@keyframes pressaDiscesa {
  0%   { transform: translateY(-1200px); }
  30%  { transform: translateY(0); }       /* impatto */
  36%  { transform: translateY(0); }       /* pausa */
  100% { transform: translateY(-1200px); } /* risalita lenta */
}

#pressa {
  animation: pressaDiscesa 5.3s ease-in-out infinite;
  /* ease-in nella prima metà, ease-out nella seconda */
}
```

### 6.2 JavaScript (sincronizzazione)
- Usa `setTimeout()` o `requestAnimationFrame()` con checkpoint temporali
- Al timestamp ~1.3s: `document.getElementById('giallo').style.visibility = 'hidden'`
- Al timestamp ~4.3s: `document.getElementById('giallo_schiacciato').style.visibility = 'visible'`
- Al termine: resetta stati e ricomincia (se loop)

### 6.3 Posizionamento Pressa
- La lattina originale ha viewBox `0 0 1464.04 1670.71`
- Nel poster, Giallo è posizionato approssimativamente tra y=800 e y=1100
- La pressa dovrà essere scalata per coprire la larghezza di Giallo (~150px → larghezza pressa ~200px scalata)
- Posizionamento centrale: `x ≈ 850` (centrata su Giallo che ha cx ≈ 867)
- Offset verticale iniziale: y ≈ -400 (fuori dal viewport superiore)

## 7. Error Handling / Fallback

- Se JavaScript è disabilitato: si vede solo il poster statico con Giallo visibile (graceful degradation)
- Se CSS animation non è supportato: fallback con `transition` o statico
- Il file funziona aprendolo direttamente nel browser (`file://`)

## 8. Variabili Configurabili

| Variabile | Default | Descrizione |
|-----------|---------|-------------|
| `--durata-discesa` | 1.5s | Tempo di discesa rapida |
| `--durata-risalita` | 2.5s | Tempo di risalita lenta |
| `--pausa-fondo` | 0.3s | Pausa quando la pressa è giù |
| `--pausa-alto` | 1.0s | Pausa quando la pressa è su |
| `--loop` | true | Se true, l'animazione riparte automaticamente |

## 9. Scale della Soluzione

Questo è un progetto piccolo e focalizzato: una singola pagina HTML con un'animazione sincronizzata. Non richiede decomposizione in sottoprogetti. Il design è intenzionalmente minimalista per mantenere la pagina auto-contenuta e leggibile.

## 10. Dipendenze

- Nessuna. File autonomo.
- Browser supportati: tutti i moderni browser con supporto CSS animations (Chrome, Firefox, Safari, Edge)

---

*Approvato per implementazione.*
