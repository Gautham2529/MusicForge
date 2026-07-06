# motifs.py
"""
MusicForge
Melodic Motifs
"""

import random


class MotifLibrary:

    def __init__(self):

        self.patterns = [

            [0, 2, 4, 2],

            [0, 1, 2, 4],

            [4, 2, 1, 0],

            [0, 4, 2, 5],

            [0, 3, 4, 2],

            [2, 4, 5, 4],

            [0, 2, 5, 4],

            [5, 4, 2, 0]

        ]

    def random(self):

        return random.choice(self.patterns)