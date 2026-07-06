"""
MusicForge
Advanced Melody Generator
"""

import random

from melody.motifs import MotifLibrary


class MelodyGenerator:

    def __init__(self):

        self.library = MotifLibrary()

        self.intro_density = 0.35
        self.verse_density = 0.60
        self.build_density = 0.80
        self.drop_density = 1.00
        self.outro_density = 0.30

    # --------------------------------------------------

    def generate(self, scale, section="verse"):

        if section == "intro":
            return self.generate_intro(scale)

        elif section == "verse":
            return self.generate_verse(scale)

        elif section == "build":
            return self.generate_build(scale)

        elif section == "drop":
            return self.generate_drop(scale)

        elif section == "outro":
            return self.generate_outro(scale)

        return self.generate_verse(scale)

    # --------------------------------------------------

    def random_note(self, scale):

        return random.choice(scale)

    # --------------------------------------------------

    def repeat(self, phrase):

        return phrase + phrase

    # --------------------------------------------------

    def variation(self, phrase, scale):

        melody = phrase.copy()

        index = random.randint(
            0,
            len(melody)-1
        )

        melody[index] = random.choice(scale)

        return melody

    # --------------------------------------------------

    def fill_rest(self, melody, scale, density):

        result = []

        for note in melody:

            if random.random() <= density:

                result.append(note)

            else:

                result.append("-")

        return result

    # --------------------------------------------------

    def motif(self):

        # MotifLibrary provides a random() method that returns a motif
        return self.library.random()

    # --------------------------------------------------

    def generate_intro(self, scale):

        motif = self.motif()

        melody = []

        for step in motif:

            melody.append(

                scale[step % len(scale)]

            )

        melody = self.fill_rest(

            melody,

            scale,

            self.intro_density

        )

        return melody

    # --------------------------------------------------

    def generate_verse(self, scale):

        motif = self.motif()

        melody = []

        for step in motif:

            melody.append(

                scale[step % len(scale)]

            )

        melody = self.repeat(melody)

        melody = self.variation(

            melody,

            scale

        )

        melody = self.fill_rest(

            melody,

            scale,

            self.verse_density

        )

        return melody

    # --------------------------------------------------

    def generate_build(self, scale):

        melody = []

        current = 0

        for i in range(16):

            melody.append(

                scale[current]

            )

            if random.random() < 0.75:

                current += 1

            current = min(

                current,

                len(scale)-1

            )

        melody = self.fill_rest(

            melody,

            scale,

            self.build_density

        )

        return melody
    
    # --------------------------------------------------

    def generate_drop(self, scale):

        motif = self.motif()

        melody = []

        # High-energy melody with octave jumps
        for _ in range(4):

            for step in motif:

                note = scale[step % len(scale)]

                melody.append(note)

        melody = self.variation(
            melody,
            scale
        )

        melody = self.fill_rest(
            melody,
            scale,
            self.drop_density
        )

        return melody

    # --------------------------------------------------

    def generate_outro(self, scale):

        melody = []

        current = len(scale) - 1

        while current >= 0:

            melody.append(
                scale[current]
            )

            if random.random() < 0.5:
                current -= 1

        melody = self.fill_rest(
            melody,
            scale,
            self.outro_density
        )

        return melody

    # --------------------------------------------------

    def generate_phrase(self, scale, section):

        """
        Universal entry point used by Song.py.
        """

        return self.generate(
            scale,
            section
        )

    # --------------------------------------------------

    def call_and_response(self, scale):

        motif = self.motif()

        call = []

        for step in motif:

            call.append(
                scale[
                    step % len(scale)
                ]
            )

        response = self.variation(
            call,
            scale
        )

        return call + response

    # --------------------------------------------------

    def evolve(self, melody, scale):

        """
        Evolves an existing melody.
        """

        evolved = melody.copy()

        changes = random.randint(
            1,
            max(1, len(evolved)//4)
        )

        for _ in range(changes):

            index = random.randint(
                0,
                len(evolved)-1
            )

            if evolved[index] != "-":

                evolved[index] = random.choice(
                    scale
                )

        return evolved

    # --------------------------------------------------

    def transpose(self, melody, scale, amount=1):

        new = []

        for note in melody:

            if note == "-":

                new.append("-")

                continue

            if note not in scale:

                new.append(note)

                continue

            index = scale.index(note)

            index += amount

            index %= len(scale)

            new.append(
                scale[index]
            )

        return new

    # --------------------------------------------------

    def repeat_section(self, melody, times=2):

        result = []

        for _ in range(times):

            result.extend(melody)

        return result

    # --------------------------------------------------

    def print_melody(self, melody):

        print()

        print("Generated Melody")

        print("----------------")

        print(" ".join(melody))