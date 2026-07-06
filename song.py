"""
MusicForge
Song Class
"""

from harmony.scales import ScaleGenerator
from harmony.chords import ChordGenerator
from harmony.progression import ProgressionGenerator

from melody.melody import MelodyGenerator
from bass.bass import BassGenerator

from drums.kick import KickGenerator
from drums.snare import SnareGenerator
from drums.hats import HatGenerator

from arranger.structure import SongStructure

from midi_export import MIDIExporter


class Song:

    def __init__(
        self,
        key="C",
        scale="major",
        bpm=140,
        style="rock"
    ):

        self.key = key
        self.scale_name = scale
        self.bpm = bpm
        self.style = style

        # Harmony
        self.scale = []
        self.chords = []
        self.progression = []

        # Melody
        self.melody = []

        # Bass
        self.bass = []

        # Drums
        self.kick = []
        self.snare = []
        self.hats = []

        # Song Arrangement
        self.structure = SongStructure()

    # --------------------------------------------------

    def generate(self):

        # Engines

        scale_engine = ScaleGenerator()
        chord_engine = ChordGenerator()
        progression_engine = ProgressionGenerator()

        melody_engine = MelodyGenerator()
        bass_engine = BassGenerator()

        kick_engine = KickGenerator()
        snare_engine = SnareGenerator()
        hat_engine = HatGenerator()

        # -----------------------------
        # Harmony
        # -----------------------------

        self.scale = scale_engine.generate(
            self.key,
            self.scale_name
        )

        self.chords = chord_engine.generate(
            self.scale
        )

        self.progression = progression_engine.generate(
            self.chords
        )

        # -----------------------------
        # Melody
        # -----------------------------

        self.melody = melody_engine.generate(
            self.scale
        )

        # -----------------------------
        # Bass
        # -----------------------------

        self.bass = bass_engine.generate(
            self.progression,
            style=self.style,
            section="verse"
)

        # -----------------------------
        # Default Drum Pattern
        # (Used only for console preview)
        # -----------------------------

        self.kick = kick_engine.generate(
            style=self.style,
            section="verse"
        )

        self.snare = snare_engine.generate(
            style=self.style,
            section="verse"
        )

        self.hats = hat_engine.generate(
            style=self.style,
            section="verse"
        )

    # --------------------------------------------------

    def show_structure(self):

        self.structure.print_structure()

    # --------------------------------------------------

    def export(self, filename="output/song.mid"):

        exporter = MIDIExporter(self.bpm)

        current_bar = 0

        for section in self.structure.sections:

            # -----------------------------
            # Create drums for this section
            # -----------------------------

            kick = KickGenerator().generate(
                style=self.style,
                section=section.drums
            )

            snare = SnareGenerator().generate(
                style=self.style,
                section=section.drums
            )

            hats = HatGenerator().generate(
                style=self.style,
                section=section.drums
            )

            exporter.add_drums(

                kick,
                snare,
                hats,

                start_bar=current_bar,

                bars=section.length

            )

            # -----------------------------
            # Melody
            # -----------------------------

            if section.melody:

                exporter.add_melody(

                    self.melody,

                    start_bar=current_bar

                )

            # -----------------------------
            # Bass
            # -----------------------------

            if section.bass:

                exporter.add_bass(

                    self.bass,

                    start_bar=current_bar

                )

            current_bar += section.length

        exporter.save(filename)