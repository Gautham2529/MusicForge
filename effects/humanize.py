# humanize.py
"""
MusicForge
Humanization Engine

Adds small timing variations to MIDI events
to make performances sound more natural.
"""

import random


class Humanizer:

    def __init__(
        self,
        timing_amount=0.03,
        velocity_amount=5
    ):

        self.timing_amount = timing_amount
        self.velocity_amount = velocity_amount

    # --------------------------------------------------

    def timing(self, beat):

        """
        Returns a slightly shifted beat position.
        """

        shift = random.uniform(
            -self.timing_amount,
            self.timing_amount
        )

        return beat + shift

    # --------------------------------------------------

    def velocity(self, velocity):

        """
        Slightly changes velocity.
        """

        change = random.randint(
            -self.velocity_amount,
            self.velocity_amount
        )

        velocity += change

        velocity = max(1, velocity)
        velocity = min(127, velocity)

        return velocity

    # --------------------------------------------------

    def note(self, beat, velocity):

        """
        Humanize both timing and velocity.
        """

        return (

            self.timing(beat),

            self.velocity(velocity)

        )