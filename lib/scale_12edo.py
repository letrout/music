"""
scale_octave.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range of 2:1 freq ratio)
Extends ./scale.py
"""

import scale_octave

SEMITONE_CENTS = 100
HALF = SEMITONE_CENTS
WHOLE = HALF * 2
WHOLEHALF = WHOLE + HALF

class Scale12EDO(scale_octave.ScaleOctave):
    def __init__(self, root_note=None, tones=None):
        super(Scale12EDO, self).__init__(root_note, tones)

    def add_tone(self, cents):
        if cents % SEMITONE_CENTS != 0:
            return None
        return super.add_tone(cents)