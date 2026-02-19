# Lowpoly Easter Bunny Generator

Dieses Projekt generiert einen **Low-Poly 3D-Osterhasen** als STL-Datei, der 3D-druckbar ist.

## Beschreibung

Das Python-Skript `generate_bunny.py` erstellt programmatisch einen geometrischen, facettierten Osterhasen im Low-Poly-Stil. Der Hase besteht aus mehreren Komponenten:

- **Körper**: Eine abgeflachte Ellipsoid-Form
- **Kopf**: Eine kleinere Kugel oben auf dem Körper
- **Ohren**: Zwei längliche Formen, die vom Kopf nach oben ragen
- **Füße**: Zwei kleine ellipsoide Formen als Füße
- **Schwanz**: Eine kleine Kugel hinten am Körper

Alle Teile werden zu einem einzigen, geschlossenen und wasserdichten Mesh kombiniert, das für den 3D-Druck geeignet ist.

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Manager)

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Dies installiert:
- `numpy` - Für mathematische Berechnungen und Array-Operationen
- `numpy-stl` - Für die Erstellung und Speicherung von STL-Dateien

## Verwendung

### Osterhasen generieren

Führen Sie das Skript aus, um den Low-Poly-Osterhasen zu generieren:

```bash
python generate_bunny.py
```

Das Skript erstellt eine Datei namens `easter_bunny_lowpoly.stl` im aktuellen Verzeichnis.

### Ausgabe

Nach erfolgreicher Ausführung sehen Sie eine Ausgabe wie:

```
Generating low-poly Easter bunny...
✓ Low-poly Easter bunny saved to 'easter_bunny_lowpoly.stl'
  - Vertices: XXX
  - Faces: XXX

Done! You can now open the STL file with any 3D viewer or slicer.
```

## STL-Datei anzeigen

Die generierte STL-Datei kann mit verschiedenen Programmen geöffnet werden:

### 3D-Viewer
- **Windows**: 3D Viewer (vorinstalliert in Windows 10/11)
- **macOS**: Preview oder [MeshLab](https://www.meshlab.net/)
- **Linux**: [MeshLab](https://www.meshlab.net/), Blender
- **Online**: [3D Viewer Online](https://3dviewer.net/)

### 3D-Druck Slicer
- [Cura](https://ultimaker.com/software/ultimaker-cura)
- [PrusaSlicer](https://www.prusa3d.com/page/prusaslicer_424/)
- [Simplify3D](https://www.simplify3d.com/)

## Technische Details

### Low-Poly-Stil
Der Hase wird mit wenigen Vertices und Faces erstellt, sodass die einzelnen Polygone sichtbar sind. Dies verleiht dem Modell einen charakteristischen, geometrischen Look.

### 3D-Druckbarkeit
Das generierte Mesh ist:
- **Geschlossen**: Keine Löcher oder offenen Kanten
- **Wasserdicht**: Geeignet für STL-Verarbeitung in Slicern
- **Manifold**: Jede Kante wird von genau zwei Dreiecken geteilt

### Geometrische Primitive
Das Skript verwendet:
- **Icosphären**: Geodätische Kugeln basierend auf einem Ikosaeder
- **Ellipsoide**: Skalierte Icosphären für ovale Formen
- **Boxen**: Einfache Quader für die Ohren

## Projektstruktur

```
Lowpoly/
├── generate_bunny.py          # Hauptskript zur Generierung
├── requirements.txt           # Python-Abhängigkeiten
├── README.md                  # Diese Datei
└── easter_bunny_lowpoly.stl   # Generierte STL-Datei (nach Ausführung)
```

## Lizenz

Dieses Projekt steht zur freien Verfügung.

## Anpassungen

Sie können das Skript anpassen, um:
- Die Größe des Hasen zu ändern (Radien der Ellipsoide anpassen)
- Die Position der Körperteile zu verändern (center-Parameter)
- Die Detailstufe zu erhöhen/verringern (subdivisions-Parameter)
- Zusätzliche Teile hinzuzufügen (z.B. Arme, Nase, Augen)