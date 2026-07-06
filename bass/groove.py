# groove.py
"""
MusicForge
Bass Groove Generator
"""

import random


class GrooveGenerator:

    def __init__(self):

        self.patterns = [

            [0, 0, 0, 0],

            [0, 0, 4, 0],

            [0, 4, 0, 4],

            [0, 7, 0, 7],

            [0, 0, 7, 4],

            [0, 4, 7, 4]

        ]

    def random(self):

        return random.choice(self.patterns)