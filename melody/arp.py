# arp.py
"""
MusicForge
Arpeggiator Engine

Generates arpeggios from chord progressions.
"""

import random


CHORD_INTERVALS = {
    "": [0, 4, 7],       # Major
    "m": [0, 3, 7],      # Minor
    "dim": [0, 3, 6]     # Diminished
}


NOTE_TO_MIDI = {
    "C": 60,
    "C#": 61,
    "D": 62,
    "D#": 63,
    "E": 64,
    "F": 65,
    "F#": 66,
    "G": 67,
    "G#": 68,
    "A": 69,
    "A#": 70,
    "B": 71
}


class Arpeggiator:

    def __init__(self):

        self.patterns = [

            [0, 1, 2, 1],          # Up
            [2, 1, 0, 1],          # Down
            [0, 2, 1, 2],          # Jump
            [0, 1, 2, 2],          # Hold
            [0, 2, 0, 2],          # Octave feel
            [0, 1, 0, 2]

        ]

    # -------------------------------------------------

    def parse_chord(self, chord):

        if chord.endswith("dim"):

            root = chord[:-3]
            quality = "dim"

        elif chord.endswith("m"):

            root = chord[:-1]
            quality = "m"

        else:

            root = chord
            quality = ""

        return root, quality

    # -------------------------------------------------

    def generate(self, progression):

        arp = []

        pattern = random.choice(self.patterns)

        for chord in progression:

            root, quality = self.parse_chord(chord)

            root_note = NOTE_TO_MIDI[root]

            intervals = CHORD_INTERVALS[quality]

            chord_notes = []

            for interval in intervals:

                chord_notes.append(root_note + interval)

            for step in pattern:

                arp.append(chord_notes[step])

        return arp