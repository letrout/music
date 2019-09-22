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
        # First degree is always the root
        self.__degree_tones = {1: 0}
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
        getter for __degree_tones
        :return: dict of degree->tone, where tone is cents above root
        """
        return self.__degree_tones

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
        Get the tones of the scale, in cents above root
        :return: A sorted list of tones in the scale
        """
        return sorted(list(self.degree_tones.values()))

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
        my_tones = self.tones
        new_degree = None
        try:
            float(cents)
        except ValueError:
            return None
        if cents < MIN_CENTS:
            return None
        if cents in my_tones:
            return -1
        #new_position = bisect.bisect(self.tones, cents)
        #bisect.insort(self.__tones, cents)
        my_tones.append(cents)
        # Rebuild self.__degrees dictionary
        i = 1
        self.__degree_tones = dict()
        for tone in sorted(my_tones):
            self.__degree_tones[i] = tone
            if tone == cents:
                new_degree = i
            i += 1
        return new_degree

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
        if degree not in self.degrees:
            return -1
        new_degree = self.add_tone(self.degree_tones[degree] + cents)
        return new_degree

    def move_degree(self, degree, cents):
        """
        Move (retune) a degree by cents
        :param degree: the scale degree to retune
        :param cents: the number of cents by which to change the tone
        (can be negative)
        :return:
        """
        # FIXME: stub
        return

    def remove_degree(self, degree):
        """
        Remove a scale degree
        :param degree:
        :return: 0 on success, -1 on error
        """
        # FIXME: stub
        return

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
