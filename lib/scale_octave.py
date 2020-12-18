"""
scale_octave.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range of 2:1 freq ratio)
Extends ./scale.py
"""

__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import scale

MAX_CENTS = 1200
OCTAVE_CENTS = MAX_CENTS


class ScaleOctave(scale.Scale):
    """
    Class to build an octave-based (2:1 freq) musical scale
    """
    def __init__(self, root_note=None, tones=None):
        """
        Constructor
        :param root_note: Note object, root note for the scale (default None)
        :param tones: List of tones, each tone the number of cents above root
        """
        super(ScaleOctave, self).__init__(root_note, tones)

    def add_tone(self, cents):
        """
        Add a tone to the scale
        :param cents: difference from scale root, in cents
        :return: new position of the tone in the scale
                 None if invalid cents value
                 -1 if tone already exists in the scale
        Raises ValueError if cents out of range
        """
        if cents > MAX_CENTS:
            return None
        return super().add_tone(cents)
