"""
scale.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range)
By default, the scale is defined by relative distances between the tones
(in cents), unless a root note is defined.
"""

import bisect

import note

MIN_CENTS = 0
MAX_CENTS = 1200

class Scale(object):
    """
    Class to hold a musical scale
    """
    def __init__(self, root_note=None):
        """
        Constructor
        :param root_note: Note object, root note for the scale (default None)
        """
        self.__tones = [0]
        self.__root_note = root_note

    @property
    def tones(self):
        """
        getter for self.__tones
        :return: self.__tones
        """
        return self.__tones

    def add_tone(self, cents):
        """
        Add a tone to the scale
        :param cents: difference from scale root, in cents
        :return: new position of the tone in the scale
                 -1 if tone already exists in the scale
        Raises ValueError if cents out of range
        """
        if not MIN_CENTS < cents <= MAX_CENTS:
            raise ValueError("cents must be between {0} and {1}".format(
                MIN_CENTS, MAX_CENTS))
        if cents in self.tones:
            return -1
        new_position = bisect.bisect(self.tones, cents)
        bisect.insort(self.__tones, cents)
        return new_position

    @property
    def root_note(self):
        """
        getter for self.__root_note
        :return: self.__root_note
        """
        return self.__root_note

    @root_note.setter
    def root_note(self, new_root):
        """
        Sets a new root note for the scale
        :param new_root: note.Note object
        :return: freq_change, the ratio of new root to the previous root
                (None if no previous root)
        """
        freq_change = None
        if isinstance(new_root, note.Note):
            if self.__root_note.freq:
                freq_change = new_root.freq / self.__root_note.freq
            self.__root_note = new_root
        return freq_change
