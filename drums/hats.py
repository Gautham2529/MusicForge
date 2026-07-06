from drums.patterns import DrumPatterns


class HatGenerator:

    def __init__(self):

        self.patterns=DrumPatterns()

    def generate(

        self,

        style="rock",

        section="verse"

    ):

        return self.patterns.get(style,section)["hat"]