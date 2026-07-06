# structure.py
"""
MusicForge
Song Structure
"""

from arranger.intro import Intro
from arranger.verse import Verse
from arranger.build import Build
from arranger.drop import Drop
from arranger.outro import Outro


class SongStructure:

    def __init__(self):

        self.sections = [

            Intro(),

            Verse(),

            Verse(),

            Build(),

            Drop(),

            Verse(),

            Drop(),

            Outro()

        ]

    def total_bars(self):

        total = 0

        for section in self.sections:

            total += section.length

        return total

    def print_structure(self):

        print()

        print("Song Structure")

        print("----------------")

        bars = 1

        for section in self.sections:

            print(

                f"{bars:02d}-{bars+section.length-1:02d}"

                f" : {section.name}"

            )

            bars += section.length