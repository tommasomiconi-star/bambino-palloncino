# Sintesi Animazione — Bambini Schiacciati

> File di riepilogo per riprendere il lavoro in una nuova sessione.

---

## Output

- `index.html` — file unico auto-contenuto (~157 KB)
- Funziona con `file://` (nessun server richiesto)

---

## Stack

- Inline SVG da `definitivo.svg`
- CSS: solo `transition: transform` sulla pressa
- JavaScript: `setTimeout` sequenziale che guida ogni movimento

---

## Coordinate Attuali della Pressa

La pressa viene spostata con `transform: translate(Xpx, Ypx)` via JavaScript.
La transition CSS è `transform 1.2s ease-in-out`.

### Posizione iniziale (CSS)

```css
#pressa {
  transform: translate(-5px, 0px);
}
```

### Coordinate per personaggio

| Personaggio | X | Y scesa | Y riposo |
|-------------|---|---------|----------|
| **Giallo** | -5px | **900px** | 0px |
| **Viola** | -322px | **900px** | 0px |
| **Verde** | -637px | **900px** | 0px |
| **Blu** | -5px | **460px** | 0px |
| **Arancione** | -322px | **460px** | 0px |
| **Rosso** | -637px | **460px** | 0px |

**Y=0** = pressa visibile nella parte alta dello schermo (posizione di riposo)
**Y=900** = copre completamente personaggi della riga bassa
**Y=460** = copre completamente personaggi della riga alta

---

## Timeline JavaScript (22.6s ciclo)

```
 0.0s  → Pressa visibile in alto sopra Giallo
 1.0s  → Inizia scesa su Giallo (1.2s)
 2.2s  → Crush Giallo
 2.4s  → Risale in alto
 3.4s  → Si sposta su Viola (in alto)
 4.6s  → Scende su Viola
 6.0s  → Crush Viola
 6.2s  → Risale in alto
 7.4s  → Si sposta su Verde
 8.6s  → Scende su Verde
 9.8s  → Crush Verde
10.0s  → Risale in alto
11.2s  → Si sposta su Blu
12.4s  → Scende su Blu
13.6s  → Crush Blu
13.8s  → Risale in alto
15.0s  → Si sposta su Arancione
16.2s  → Scende su Arancione
17.4s  → Crush Arancione
17.6s  → Risale in alto
18.8s  → Si sposta su Rosso
20.0s  → Scende su Rosso
21.2s  → Crush Rosso
21.4s  → Risale in alto e resta
22.6s  → Loop riavvia (resetAll)
```

---

## Logica di Visibilità

### Elementi nascosti permanentemente
- `sparafoglie` (`style="visibility:hidden"` inline)

### Elementi gestiti da JavaScript
| Normale | Schiacciato |
|---------|-------------|
| `giallo` | `giallo_schiacciato` |
| `viola` | `viola_schiacciato` |
| `verde` | `verde_schiacciato` |
| `blu` | `blu_schiacciato` |
| `arancione` | `arancione_schiacciato` |
| `rosso` | `rosso_schiacciato` |

**Inizio**: tutti normali visibili, tutti schiacciati nascosti (`resetAll()`)
**Crush**: normale diventa `visibility:hidden`, schiacciato diventa `visibility:visible`

---

## Struttura SVG

Ordine z-index (dal basso verso l'alto):
1. Sfondo
2. Personaggi schiacciati (inizialmente nascosti)
3. Personaggi normali
4. **Pressa** (in cima, dipinge sopra tutto)

---

## File Sorgente

| File | Uso |
|------|-----|
| `index.html` | File finale con animazione |
| `definitivo.svg` | SVG base con personaggi + pressa |
| `AGENTS.md` | Documentazione storica |

---

## Come Modificare

### Spostare la pressa più a destra/sinistra
Modificare tutti i valori X nelle chiamate `movePressa()` nel blocco `runCycle()`.

### Cambiare quanto in basso scende
Modificare Y=900 (riga bassa) e Y=460 (riga alta).

### Rallentare/accelerare
Modificare:
- `transition: transform 1.2s ease-in-out;` nel CSS
- `duration` parametro di `movePressa()` (es. `movePressa(x, y, 1.5)`)
- I tempi dei `setTimeout` in `runCycle()`

### Aggiungere pausa extra
Aumentare i millisecondi tra un `setTimeout` e il successivo.

---

## Ultima Modifica

Sessione del 12 giugno 2026
- Sostituito sfondo con `definitivo.svg`
- Calibrata pressa su tutti i 6 personaggi
- Implementata animazione JS-driven con CSS transitions
- Pressa parte visibile in alto, scende, schiaccia, risale, si sposta
- Loop infinito ogni 22.6 secondi
