# scales.py
"""
MusicForge
Scale Generator
"""

NOTES = [
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#",
    "A",
    "A#",
    "B"
]

SCALES = {

    "major": [0,2,4,5,7,9,11],

    "minor": [0,2,3,5,7,8,10],

    "harmonic_minor": [0,2,3,5,7,8,11],

    "melodic_minor": [0,2,3,5,7,9,11],

    "major_pentatonic": [0,2,4,7,9],

    "minor_pentatonic": [0,3,5,7,10]

}


class ScaleGenerator:

    def __init__(self):

        self.notes = NOTES


    def generate(self, root, scale):

        root = root.upper()

        if root not in self.notes:
            raise Exception("Unknown note")

        if scale not in SCALES:
            raise Exception("Unknown scale")

        root_index = self.notes.index(root)

        result = []

        for interval in SCALES[scale]:

            result.append(
                self.notes[(root_index + interval) % 12]
            )

        return result