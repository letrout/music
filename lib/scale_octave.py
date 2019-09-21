"""
scale_octave.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range of 2:1 freq ratio)
Extends ./scale.py
"""

import scale

MAX_CENTS = 1200


class ScaleOctave(scale.Scale):
    def __init__(self, root_note=None, tones=None):
        super(ScaleOctave, self).__init__(root_note, tones)

    def add_tone(self, cents):
        if cents > MAX_CENTS:
            return None
        return super.add_tone(cents)
