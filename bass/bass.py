"""
MusicForge
Advanced Bass Generator
"""

import random

from bass.groove import GrooveGenerator


NOTE_TO_MIDI = {

    "C": 36,
    "C#": 37,
    "D": 38,
    "D#": 39,
    "E": 40,
    "F": 41,
    "F#": 42,
    "G": 43,
    "G#": 44,
    "A": 45,
    "A#": 46,
    "B": 47

}


class BassGenerator:

    def __init__(self):

        self.groove = GrooveGenerator()

    # --------------------------------------------------

    def chord_root(self, chord):

        if chord.endswith("dim"):
            return chord[:-3]

        if chord.endswith("m"):
            return chord[:-1]

        return chord

    # --------------------------------------------------

    def octave_jump(self, note):

        if random.random() < 0.30:
            return note + 12

        return note

    # --------------------------------------------------

    def walking(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            midi = NOTE_TO_MIDI[root]

            bass.extend([

                midi,

                midi + 2,

                midi + 4,

                midi + 5

            ])

        return bass

    # --------------------------------------------------

    def rock(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            midi = NOTE_TO_MIDI[root]

            bass.extend([

                midi,

                midi,

                self.octave_jump(midi),

                midi

            ])

        return bass

    # --------------------------------------------------

    def edm(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            midi = NOTE_TO_MIDI[root]

            bass.extend([

                midi,

                midi,

                midi,

                midi

            ])

        return bass

    # --------------------------------------------------

    def phonk(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            midi = NOTE_TO_MIDI[root]

            bass.extend([

                midi,

                midi + 12,

                midi,

                midi + 7

            ])

        return bass

    # --------------------------------------------------

    def intro(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            bass.append(

                NOTE_TO_MIDI[root]

            )

        return bass

    # --------------------------------------------------

    def build(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            midi = NOTE_TO_MIDI[root]

            bass.extend([

                midi,

                midi,

                midi + 2,

                midi + 4

            ])

        return bass

    # --------------------------------------------------

    def drop(self, progression):

        style = random.choice([

            self.rock,

            self.edm,

            self.phonk

        ])

        return style(progression)

    # --------------------------------------------------

    def outro(self, progression):

        bass = []

        for chord in progression:

            root = self.chord_root(chord)

            bass.extend([

                NOTE_TO_MIDI[root],

                NOTE_TO_MIDI[root]

            ])

        return bass

    # --------------------------------------------------

    def generate(

        self,

        progression,

        style="rock",

        section="verse"

    ):

        if section == "intro":

            return self.intro(progression)

        elif section == "build":

            return self.build(progression)

        elif section == "drop":

            return self.drop(progression)

        elif section == "outro":

            return self.outro(progression)

        # Verse

        if style == "rock":

            return self.rock(progression)

        elif style == "edm":

            return self.edm(progression)

        elif style == "phonk":

            return self.phonk(progression)

        elif style == "walking":

            return self.walking(progression)

        return self.rock(progression)