# PGHRT

Das hier ist die Version des deutschen Quellcodes von [Katie's pghrt](https://github.com/Juicysteak117/pghrt/) Repo. Reviews und pull requests sind willkommen. :) 

Wenn du Interesse hast, eine Übersetzung oder eine andere Version zu machen, melde dich einfach bei [Katie](https://katea.gay/)!

## Setup
Dieses Projekt benötigt `LaTeXML` und Katie ist echt dankbar dafür, dass es existiert. Installier es [hier](https://math.nist.gov/~BMiller/LaTeXML/get.html) und unterstütz es bitte, wenn du kannst!

Möglicherweise musst du auch „texlive-latex-extra” mit deinem bevorzugten Paketmanager installieren oder bestimmte fehlende Pakete über „MiKTeX”, wenn du eine schlankere LaTeX-Installation bevorzugst.
### Linux

```bash
cd pghrt
python3 -m venv .venv
.venv/bin/pip install beautifulsoup4
```

### Windows

```bash
cd pghrt
python -m venv .venv
.venv/scripts/pip install beautifulsoup4
```

## Build Instruktionen

Im Moment hat `/export` die komplette Build-Ausgabe. Wenn du den Quellcode selbst kompilieren und bauen willst, findest du die Anleitung unten. Denk dran, dass der Fehler `\DTMNow` in der Ausgabe von `latexmlc` ignoriert werden kann, weil er von `soup.py` behandelt wird.

### Linux

```bash
latexmlc --destination=export/index.html pghrt
.venv/bin/python soup.py
```

### Windows

```bash
latexmlc --destination=export/index.html pghrt
.venv/scripts/python soup.py
```

## Lizenz

Zitat Katie:

`Ich weiß es nicht. Bitte gib die Quelle an, wenn es sicher und sinnvoll ist. Du kannst das hier gerne als Vorlage benutzen (wenn du den Inhalt der .tex-Datei löschen möchtest), wenn es dir beim Schreiben deines eigenen Dokuments über den Transitionsprozess hilft. Wir brauchen mehr hochwertige Ressourcen.`