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


class Scale(object):
    """
    Class to hold a musical scale
    """
    def __init__(self, root_note=None, tones=None):
        """
        Constructor
        :param root_note: Note object, root note for the scale (default None)
        :param tones: List of tones, each tone the number of cents above root
        """
        self.__tones = [0]
        self.__root_note = None

        self.root_note = root_note
        if isinstance(tones, (list,)):
            try:
                for tone in sorted(tones):
                    self.add_tone(tone)
            except TypeError:
                pass

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
                 None if invalid cents value
                 -1 if tone already exists in the scale
        Raises ValueError if cents out of range
        """
        try:
            float(cents)
        except ValueError:
            return None
        if cents < MIN_CENTS:
            return None
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
        :param new_root: note.Note object or int (Hz)
        :return: freq_ratio, the ratio of new root to the previous root
                (None if no previous root)
        """
        freq_ratio = None
        if isinstance(new_root, note.Note):
            freq_ratio = self.freq_ratio(new_root.freq)
            self.__root_note = new_root
        elif isinstance(new_root, int):
            new_root_note = note.Note(new_root)
            freq_ratio = self.freq_ratio(new_root_note.freq)
            self.__root_note = new_root_note
        return freq_ratio

    def freq_ratio(self, new_freq):
        """
        Calculate the ratio of some frequency to our root note
        (does not change our current root note)
        :param new_freq: the new frequency to compare (Hz)
        :return: ratio of new frequency / our root
                 None if we don't currently have a root note frequency
        """
        freq_ratio = None
        if self.root_note is not None and self.root_note.freq:
            freq_ratio = new_freq / self.root_note.freq
        return freq_ratio
