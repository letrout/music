"""
scale_octave.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range of 2:1 freq ratio)
Extends ./scale.py
"""

import lib.scale_octave as scale_octave

SEMITONE_CENTS = 100
HALF = SEMITONE_CENTS
WHOLE = HALF * 2
WHOLEHALF = WHOLE + HALF


class Scale12EDO(scale_octave.ScaleOctave):
    """
    Class to build a 12-EDO musical scale
    """
    def __init__(self, root_note=None, tones=None):
        """
        Constructor
        :param root_note: Note object, root note for the scale (default None)
        :param tones: List of tones, each tone the number of cents above root
        """
        super(Scale12EDO, self).__init__(root_note, tones)

    def add_tone(self, cents):
        """
        Add a tone to the scale
        :param cents: difference from scale root, in cents
        :return: new position of the tone in the scale
                 None if invalid cents value
                 -1 if tone already exists in the scale
        Raises ValueError if cents out of range
        """
        if cents % SEMITONE_CENTS != 0:
            return None
        return super().add_tone(cents)
