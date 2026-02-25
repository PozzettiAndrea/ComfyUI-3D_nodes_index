# Whykiki ComfyUI Toolset

A collection of useful nodes for ComfyUI that provide various workflow enhancements.

## Installation

1. Clone the repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/TheWhykiki/Whykiki-ComfyUIToolset.git
```

2. Install the required dependencies:

```bash
cd Whykiki-ComfyUIToolset
pip install -r requirements.txt
```

3. Restart ComfyUI.

## Included Nodes

### Sequential Image Loader (V8)

A node for sequentially loading and processing images from a folder with integrated mask support.

#### Features:

- Loads images sequentially from a folder
- Applies a mask to all images
- Returns the filename and total number of images
- Versatile interpolation options for both image and mask
- Option to binarize the mask

#### Usage:

The node appears in the "image" category in the node browser.

##### Inputs:
- **folder_path**: Path to the folder with images to be processed
- **mask**: A mask in ComfyUI MASK format
- **current_index**: The current image index (starting at 0)
- **resize_width/resize_height**: Target resolution for the images
- **image_interpolation**: Interpolation method for image resizing
- **mask_interpolation**: Interpolation method for mask resizing
- **binarize_mask**: Whether to convert the mask to binary values (0/1)

##### Outputs:
- **image**: The loaded image
- **mask**: The adjusted mask
- **filename**: The filename of the current image
- **total_images**: The total number of images in the folder

## Planned Features

- Additional useful nodes for image processing
- Workflow automation tools
- Batch processing functions

## Contributing

Contributions are welcome! Please create an issue or pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# Whykiki ComfyUI Toolset (Deutsch)

Eine Sammlung nützlicher Nodes für ComfyUI, die verschiedene Workflow-Erweiterungen bieten.

## Installation

1. Klonen Sie das Repository in Ihr ComfyUI `custom_nodes` Verzeichnis:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/TheWhykiki/Whykiki-ComfyUIToolset.git
```

2. Installieren Sie die erforderlichen Abhängigkeiten:

```bash
cd Whykiki-ComfyUIToolset
pip install -r requirements.txt
```

3. Starten Sie ComfyUI neu.

## Enthaltene Nodes

### Sequential Image Loader (V8)

Ein Node zum sequentiellen Laden und Verarbeiten von Bildern aus einem Ordner mit integrierter Maskenunterstützung.

#### Funktionen:

- Lädt Bilder sequentiell aus einem Ordner
- Wendet eine Maske auf alle Bilder an
- Gibt den Dateinamen und die Gesamtzahl der Bilder zurück
- Vielseitige Interpolationsoptionen für Bild und Maske
- Option zum Binarisieren der Maske

#### Verwendung:

Der Node erscheint in der Kategorie "image" im Node-Browser.

##### Eingaben:
- **folder_path**: Pfad zum Ordner mit den zu verarbeitenden Bildern
- **mask**: Eine Maske im ComfyUI MASK-Format
- **current_index**: Der aktuelle Bildindex (beginnend bei 0)
- **resize_width/resize_height**: Zielauflösung für die Bilder
- **image_interpolation**: Interpolationsmethode für Bildgrößenänderungen
- **mask_interpolation**: Interpolationsmethode für Maskengrößenänderungen
- **binarize_mask**: Ob die Maske zu binären Werten (0/1) umgewandelt werden soll

##### Ausgaben:
- **image**: Das geladene Bild
- **mask**: Die angepasste Maske
- **filename**: Der Dateiname des aktuellen Bildes
- **total_images**: Die Gesamtzahl der Bilder im Ordner

## Geplante Features

- Weitere nützliche Nodes für die Bildverarbeitung
- Workflow-Automatisierungstools
- Batch-Verarbeitungsfunktionen

## Mitwirken

Beiträge sind willkommen! Bitte erstellen Sie einen Issue oder Pull Request auf GitHub.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die Datei [LICENSE](LICENSE) für Details.
