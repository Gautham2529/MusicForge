# velocity.py
"""
MusicForge
Velocity Engine

Adds realistic dynamics to notes.
"""

import random


class VelocityEngine:

    def __init__(self):

        self.min_velocity = 70
        self.max_velocity = 120

        self.accent_velocity = 125
        self.ghost_velocity = 45

    # --------------------------------------------------

    def note(self):

        return random.randint(
            self.min_velocity,
            self.max_velocity
        )

    # --------------------------------------------------

    def accent(self):

        return self.accent_velocity

    # --------------------------------------------------

    def ghost(self):

        return self.ghost_velocity

    # --------------------------------------------------

    def pattern(self, length):

        velocities = []

        for step in range(length):

            # Strong beats
            if step % 4 == 0:

                velocities.append(
                    self.accent()
                )

            else:

                velocities.append(
                    self.note()
                )

        return velocities

    # --------------------------------------------------

    def humanize(self, velocity):

        velocity += random.randint(-8, 8)

        velocity = max(1, velocity)
        velocity = min(127, velocity)

        return velocity