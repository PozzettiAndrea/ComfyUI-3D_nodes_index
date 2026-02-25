# ComfyUI Fixed Seed Controller

Eine Custom Node für ComfyUI, die es ermöglicht, zufällige Seeds zu generieren und diese über mehrere Generierungen hinweg beizubehalten, bis explizit eine neue Seed angefordert wird.

## Features

- 🎲 **Zufällige Seed-Generierung**: Erstellt eine neue zufällige Seed auf Knopfdruck
- 📌 **Feste Seed**: Behält die aktuelle Seed bei, bis du eine neue generierst
- 💾 **Persistenz**: Speichert die letzte Seed automatisch (überlebt ComfyUI-Neustarts)
- 🎯 **Manuelle Seed-Eingabe**: Optional kannst du auch eine spezifische Seed eingeben
- ⚙️ **Anpassbarer Bereich**: Definiere Min/Max-Werte für die Seed-Generierung

## Installation

### Methode 1: Git Clone (Empfohlen)

Navigiere in dein ComfyUI `custom_nodes` Verzeichnis und clone das Repository:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Slartibart23/ComfyUI-FixedSeedController.git
```

### Methode 2: Manuelle Installation

1. Lade das Repository als ZIP herunter
2. Entpacke es in `ComfyUI/custom_nodes/ComfyUI-FixedSeedController`
3. Starte ComfyUI neu

## Verwendung

### Grundlegende Verwendung

1. Füge die Node "Fixed Seed Controller" zu deinem Workflow hinzu
2. Verbinde den `seed` Output mit dem Seed-Input deines Samplers/Generator-Nodes
3. **Erste Generierung**: Setze `generate_new_seed` auf `True` (Generate New)
4. **Weitere Generierungen mit gleicher Seed**: Setze `generate_new_seed` auf `False` (Keep Current)
5. Wenn du ein neues Bild mit anderer Seed möchtest: Wieder auf `True` setzen

### Typischer Workflow

```
Fixed Seed Controller → KSampler
                     ↓
                  SaveImage
```

**Arbeitsablauf:**
1. Setze `generate_new_seed` auf `True` und generiere ein Bild
2. Wenn dir das Ergebnis nicht gefällt: Lasse `generate_new_seed` auf `True` für neue Seed
3. Wenn dir das Ergebnis gefällt: Setze `generate_new_seed` auf `False`
4. Aktiviere deine SaveImage-Node und generiere erneut (gleiche Seed = gleiches Bild)
5. Für das nächste neue Bild: Wieder auf `True` setzen

### Parameter

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|--------------|
| `generate_new_seed` | BOOLEAN | False | `True`: Neue Seed generieren<br>`False`: Aktuelle Seed beibehalten |
| `seed_min` | INT | 0 | Minimaler Wert für zufällige Seeds |
| `seed_max` | INT | 18446744073709551615 | Maximaler Wert für zufällige Seeds |
| `manual_seed` | INT (optional) | -1 | Setze auf `-1` für automatische Generierung<br>Oder gib eine spezifische Seed ein |

### Outputs

| Output | Typ | Beschreibung |
|--------|-----|--------------|
| `seed` | INT | Die aktuelle Seed (zum Verbinden mit Sampler) |
| `seed_info` | STRING | Info-Text über den aktuellen Status |

## Beispiel-Workflow

### Szenario: Iteratives Arbeiten mit SaveImage auf Bypass

**Problem**: Du generierst Bilder mit fester Seed, aber SaveImage ist auf Bypass. Wenn dir ein Bild gefällt und du SaveImage aktivierst, wird beim erneuten Generieren eine neue Seed verwendet.

**Lösung mit Fixed Seed Controller**:

1. **Setup**:
   - Fixed Seed Controller → KSampler (seed input)
   - KSampler → SaveImage Plus (auf Bypass)

2. **Erste Generierung**:
   - `generate_new_seed` = `True`
   - Queue Prompt → Bild wird generiert

3. **Bild gefällt nicht**:
   - `generate_new_seed` = `True` (lassen)
   - Queue Prompt → Neue Seed, neues Bild

4. **Bild gefällt**:
   - `generate_new_seed` = `False` (wichtig!)
   - SaveImage auf Bypass deaktivieren
   - Queue Prompt → Gleiches Bild wird gespeichert

5. **Nächstes Bild**:
   - `generate_new_seed` = `True`
   - SaveImage wieder auf Bypass
   - Queue Prompt → Neue Seed, neues Bild

## Kompatibilität

- **ComfyUI**: Alle aktuellen Versionen
- **Python**: 3.8+, getestet mit 3.13.9
- **Abhängigkeiten**: Keine (nur Python Standard-Bibliothek)

## Technische Details

- Die aktuelle Seed wird in `last_seed.json` im Node-Verzeichnis gespeichert
- Verwendet Python's `random.randint()` für Seed-Generierung
- Kompatibel mit allen Standard-ComfyUI Sampler-Nodes

## Troubleshooting

**Problem**: Seed ändert sich trotz `generate_new_seed = False`

**Lösung**: Stelle sicher, dass du nicht mehrere Fixed Seed Controller Nodes im gleichen Workflow verwendest. Jede Node hat ihren eigenen Seed-Speicher.

**Problem**: Node wird nach Installation nicht angezeigt

**Lösung**: 
1. Starte ComfyUI komplett neu
2. Überprüfe die Konsole auf Fehlermeldungen
3. Stelle sicher, dass die Node im richtigen Verzeichnis liegt: `custom_nodes/ComfyUI-FixedSeedController/`

## Lizenz

MIT License - Siehe LICENSE Datei

## Beiträge

Beiträge sind willkommen! Öffne gerne ein Issue oder Pull Request.

## Changelog

### Version 1.0.0
- Initial Release
- Zufällige Seed-Generierung
- Fixed Seed Modus
- Persistente Seed-Speicherung
- Manuelle Seed-Eingabe
- Anpassbarer Seed-Bereich
