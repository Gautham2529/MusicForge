# 🎵 MusicForge

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-v0.1--alpha-yellow)

MusicForge is a modular procedural music generation engine written entirely in Python.

It generates melodies, basslines, drum patterns, harmony, chord progressions and exports complete MIDI songs that can be played inside any DAW such as LMMS.

## 📚 Table of Contents

- [Features](#-features)
- [Current Status](#-current-status)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example](#-example)
- [Roadmap](#-roadmap)
- [Technologies Used](#-technologies-used)
- [License](#-license)
---

# ✨ Features

- 🎼 Music Theory Engine
- 🎹 Melody Generator
- 🎸 Bass Generator
- 🥁 Drum Generator
- 🎵 Chord Progressions
- 🎧 MIDI Export
- 🎼 Song Arranger
- ⚡ Modular Architecture
- 🤖 AI Ready

---

# 📌 Current Status

MusicForge is currently in **Alpha (v0.1)**.

### ✅ Implemented

- Scale Generation
- Chord Generation
- Chord Progressions
- Melody Generator
- Bass Generator
- Drum Engine
- MIDI Export
- Song Arrangement

### 🚧 Under Development

- Humanization Engine
- Swing Engine
- AI Composer
- Neural Melody Generator
- WAV Export
- Real-Time Playback
- GUI Interface

---

# 📁 Project Structure

```
MusicForge/
│
├── main.py
├── config.py
├── midi_export.py
├── song.py
├── README.md
├── requirements.txt
│
├── drums/
│   ├── kick.py
│   ├── snare.py
│   ├── hats.py
│   └── patterns.py
│
├── harmony/
│   ├── chords.py
│   ├── scales.py
│   └── progression.py
│
├── melody/
│   ├── melody.py
│   ├── motifs.py
│   └── arp.py
│
├── bass/
│   ├── bass.py
│   └── groove.py
│
├── arranger/
│   ├── intro.py
│   ├── verse.py
│   ├── build.py
│   ├── drop.py
│   ├── outro.py
│   └── structure.py
│
├── effects/
│   ├── velocity.py
│   ├── humanize.py
│   └── swing.py
│
├── ai/
│   ├── generator.py
│   └── trainer.py
│
└── output/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Gautham2529/MusicForge.git
```

Move into the project

```bash
cd MusicForge
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

Run the project

```bash
python main.py
```

---

# 🎼 Example

```python
from song import Song

song = Song(
    key="E",
    scale="minor",
    bpm=140,
    style="rock"
)

song.generate()

song.export()
```

---

# 📷 Example Output

```
============================================================
Song Information
============================================================

Key          : E
Scale        : minor
BPM          : 140
Style        : rock

============================================================
Scale
============================================================

E → F# → G → A → B → C → D

============================================================
Chord Progression
============================================================

E → A → B → E

============================================================
Melody
============================================================

G - C B - - C B

============================================================
Bass
============================================================

[40, 40, 40, 40, 45, 45, 57, 45]

============================================================
Kick
============================================================

[1,0,0,0,1,0,1,0]

============================================================
Export
============================================================

output/song.mid
```

The generated MIDI can be imported into **LMMS**, **FL Studio**, **Ableton Live**, **Reaper**, or any MIDI-compatible Digital Audio Workstation (DAW).

---

# 🛠 Technologies Used

- Python 3.13
- MIDIUtil
- Music Theory
- Object-Oriented Programming
- Modular Software Architecture

---

# 🚀 Roadmap

## Version 0.2

- [ ] Humanization
- [ ] Swing Engine
- [ ] Better Drum Variations
- [ ] Better Bass Grooves

## Version 0.3

- [ ] AI Melody Generator
- [ ] AI Chord Suggestions
- [ ] Genre Detection
- [ ] Dynamic Song Structure

## Version 0.4

- [ ] WAV Export
- [ ] Neural Melody Generator

---

## 🛠 Built With

- Python
- MIDIUtil

---

## 📜 License

MIT License

---

Made with ❤️ by Gautham