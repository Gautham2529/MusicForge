# progression.py
"""
MusicForge
Chord Progressions
"""

import random


PROGRESSIONS = [

    [1,5,6,4],

    [6,4,1,5],

    [1,4,5,1],

    [1,6,4,5],

    [2,5,1,6]

]


class ProgressionGenerator:

    def generate(self, chords):

        pattern = random.choice(PROGRESSIONS)

        progression = []

        for degree in pattern:

            progression.append(chords[degree-1])

        return progression