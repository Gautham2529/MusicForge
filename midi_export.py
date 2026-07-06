"""
MusicForge
MIDI Export Engine v2
"""

from midiutil import MIDIFile
import os


class MIDIExporter:

    # ---------------------------------------------

    def __init__(self, bpm=140):

        self.bpm = bpm

        self.tracks = 4

        self.midi = MIDIFile(self.tracks)

        # -------------------------

        self.DRUM_TRACK = 0
        self.BASS_TRACK = 1
        self.MELODY_TRACK = 2
        self.CHORD_TRACK = 3

        # -------------------------

        self.DRUM_CHANNEL = 9
        self.BASS_CHANNEL = 0
        self.MELODY_CHANNEL = 1
        self.CHORD_CHANNEL = 2

        # -------------------------

        for track in range(self.tracks):

            self.midi.addTempo(track, 0, bpm)

        self.midi.addTrackName(self.DRUM_TRACK, 0, "Drums")
        self.midi.addTrackName(self.BASS_TRACK, 0, "Bass")
        self.midi.addTrackName(self.MELODY_TRACK, 0, "Melody")
        self.midi.addTrackName(self.CHORD_TRACK, 0, "Chords")

        # Instruments

        self.midi.addProgramChange(
            self.BASS_TRACK,
            self.BASS_CHANNEL,
            0,
            33
        )

        self.midi.addProgramChange(
            self.MELODY_TRACK,
            self.MELODY_CHANNEL,
            0,
            0
        )

        self.midi.addProgramChange(
            self.CHORD_TRACK,
            self.CHORD_CHANNEL,
            0,
            48
        )

    # ------------------------------------------------------------

    def note_to_midi(self, note):

        table = {

            "C":60,
            "C#":61,
            "D":62,
            "D#":63,
            "E":64,
            "F":65,
            "F#":66,
            "G":67,
            "G#":68,
            "A":69,
            "A#":70,
            "B":71

        }

        return table[note]

    # ------------------------------------------------------------

    def add_drums(

        self,

        kick,

        snare,

        hats,

        start_bar=0,

        bars=1

    ):

        kick_note = 36
        snare_note = 38
        hat_note = 42

        for bar in range(bars):

            start_time = (start_bar + bar) * 8

            for step in range(16):

                beat = start_time + step * 0.25

                if kick[step]:

                    self.midi.addNote(

                        self.DRUM_TRACK,

                        self.DRUM_CHANNEL,

                        kick_note,

                        beat,

                        0.25,

                        120

                    )

                if snare[step]:

                    self.midi.addNote(

                        self.DRUM_TRACK,

                        self.DRUM_CHANNEL,

                        snare_note,

                        beat,

                        0.25,

                        100

                    )

                if hats[step]:

                    self.midi.addNote(

                        self.DRUM_TRACK,

                        self.DRUM_CHANNEL,

                        hat_note,

                        beat,

                        0.25,

                        70

                    )

    # ------------------------------------------------------------

    def add_bass(

        self,

        bass,

        start_bar=0

    ):

        time = start_bar * 8

        for note in bass:

            self.midi.addNote(

                self.BASS_TRACK,

                self.BASS_CHANNEL,

                note,

                time,

                1,

                95

            )

            time += 1

    # ------------------------------------------------------------

    def add_melody(

        self,

        melody,

        start_bar=0

    ):

        time = start_bar * 8

        for note in melody:

            # Rest
            if note == "-":

                time += 0.5

                continue

            self.midi.addNote(

                self.MELODY_TRACK,

                self.MELODY_CHANNEL,

                self.note_to_midi(note),

                time,

                0.5,

                100

            )

            time += 0.5

    # ------------------------------------------------------------

    def save(

        self,

        filename="output/song.mid"

    ):

        folder = os.path.dirname(filename)

        if folder:

            os.makedirs(folder, exist_ok=True)

        with open(filename, "wb") as file:

            self.midi.writeFile(file)

        print(f"Saved -> {filename}")