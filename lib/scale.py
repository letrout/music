"""
scale.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range).

The scale is defined by relative distances between each of the tones and the
root.
The base structure of the scale is provided by degree_tones. This is a
dictionary of degree: tone, where 'degree' is the degree of the scale
(with the root being 1) and 'tone' is the number of cents above the root for
the degree.
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
        # First degree is always the root
        self.__tones = [0]
        self.__root_note = None

        self.root_note = root_note
        if tones is not None and isinstance(tones, (list,)):
            try:
                for tone in sorted(tones):
                    self.add_tone(tone)
            except TypeError:
                pass

    @property
    def degree_tones(self):
        """
        dictionary of degrees->tones
        :return: dict of degree->tone, where tone is cents above root
        """
        i = 1
        degree_tones = {}
        for tone in self.tones:
            degree_tones[i] = tone
            i += 1
        return degree_tones

    @property
    def degrees(self):
        """
        The degrees of the scale
        :return: A sorted list of the scale degrees
        """
        return sorted(list(self.degree_tones.keys()))

    @property
    def tones(self):
        """
        getter for __tones
        Get the tones of the scale, in cents above root
        :return: A sorted list of tones in the scale
        """
        return sorted(self.__tones)

    @property
    def degree_steps_cents(self):
        """
        Get the steps of every degree (to the previous), in cents
        :return: dict of degree->cents to previous degree
        """
        steps = dict()
        for degree, cents in self.degree_tones.items():
            if degree == 1:
                steps[1] = 0
            else:
                steps[degree] = cents - self.degree_tones[degree - 1]
        return steps

    def add_tone(self, cents):
        """
        Add a tone to the scale
        :param cents: difference from scale root, in cents
        :return: new degree of the tone in the scale
                 None if invalid cents value
                 -1 if tone already exists in the scale
        """
        try:
            float(cents)
        except ValueError:
            return None
        if cents < MIN_CENTS:
            return None
        if cents in self.tones:
            return -1
        self.__tones.append(cents)
        return self.tones.index(cents) + 1

    def add_tone_rel_degree(self, degree, cents):
        """
        Add a tone relative to an existing degree,
        by the number of cents above the existing degree
        (cents can be negative to insert below the degree)
        :param degree: existing degree of the scale
        :param cents: number of cents above the existing degree for new tone
        (can be negative to insert a tone below an existing degree)
        :return: the degree of the inserted tone, -1 if error
        """
        new_degree = None
        try:
            new_cents = self.degree_tones[degree] + cents
        except KeyError:
            return -1
        return self.add_tone(new_cents)

    def move_degree(self, degree, cents):
        """
        Move (retune) a degree by cents
        :param degree: the scale degree to retune
        :param cents: the number of cents by which to change the tone
        (can be negative)
        :return: 0 on success, -1 on error
        """
        if degree == 1:
            # can't remove the root
            return -1
        try:
            cur_cents = self.degree_tones[degree]
        except KeyError:
            return -1
        new_cents = cur_cents + cents
        new_degree = self.add_tone(new_cents)
        if new_degree is None or new_degree == -1:
            # Re-tuned tone doesn't fit our scale constraints?
            # reset degree_tones and return error
            return -1
        # Remove the old degree
        self.__tones.remove(cur_cents)
        return 0

    def remove_degree(self, degree):
        """
        Remove a scale degree
        :param degree:
        :return: 0 on success, -1 on error
        """
        try:
            cur_cents = self.degree_tones[degree]
        except KeyError:
            return -1
        new_tones = self.tones
        self.__tones.remove(cur_cents)
        return 0

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
