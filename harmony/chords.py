# chords.py
"""
MusicForge
Chord Generator
"""

CHORD_TYPES = [

    "",

    "m",

    "m",

    "",

    "",

    "m",

    "dim"

]


class ChordGenerator:

    def generate(self, scale):

        chords = []

        for note, chord in zip(scale, CHORD_TYPES):

            chords.append(note + chord)

        return chords