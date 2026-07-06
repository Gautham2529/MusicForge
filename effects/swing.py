# swing.py
"""
MusicForge
Swing Engine

Applies swing (shuffle) timing to MIDI events.
"""

class SwingEngine:

    def __init__(self, amount=0.0):

        """
        amount:
            0.0 = Straight
            0.10 = Light Swing
            0.20 = Medium Swing
            0.30 = Heavy Swing
        """

        self.amount = max(0.0, min(amount, 0.50))

    # --------------------------------------------------

    def apply(self, beat):

        """
        Apply swing to a beat.

        Every off-beat is delayed slightly.
        """

        subdivision = beat * 2

        if int(subdivision) % 2 == 1:

            beat += self.amount

        return beat

    # --------------------------------------------------

    def apply_pattern(self, beats):

        """
        Apply swing to an entire list of beats.
        """

        return [

            self.apply(beat)

            for beat in beats

        ]

    # --------------------------------------------------

    def set_amount(self, amount):

        self.amount = max(

            0.0,

            min(amount, 0.50)

        )