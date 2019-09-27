"""
scale.py
A class to hold a collection of tones defined as a scale
(ie all tones within an octave range).

The scale is defined by relative distances between each of the tones and the
root.
The base structure of the scale is provided by scale_df. This is a
DataFrame with columns degree and tone, where 'degree' is the degree of the
scale (with the root being 1) and 'tone' is the number of cents above the root
for the degree.
"""

import pandas as pd

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
        self.__scale_df = pd.DataFrame.from_dict({'degree': [1], 'tone': [0]})
        self.__root_note = None

        self.root_note = root_note
        if tones is not None and isinstance(tones, (list,)):
            try:
                for tone in sorted(tones):
                    self.add_tone(tone)
            except TypeError:
                pass


    @property
    def scale_df(self):
        """
        getter for scale_df
        :return: scale_df dataframe
        """
        # TODO: run rebuild_scale_df() every access?
        return self.__scale_df

    def rebuild_scale_df(self):
        """
        Rebuild the scale dataframe
        Sort by tones, reset index, and recalculate degrees
        :return: nothing
        """
        # TODO: run these ops on a copy of scale_df?
        # TODO: make this a private method?
        self.__scale_df.sort_values(by=['tone'], inplace=True)
        self.__scale_df.reset_index(inplace=True, drop=True)
        self.__scale_df.loc[:, 'degree'] = self.__scale_df.index + 1
        return

    @property
    def degree_tones(self):
        """
        dict of degree->tone
        :return: dict of degree->tone, where tone is cents above root
        """
        return self.scale_df.set_index('degree').to_dict()['tone']

    @property
    def degrees(self):
        """
        The degrees of the scale
        :return: A sorted list of the scale degrees
        """
        return self.scale_df['degree'].to_list()

    @property
    def tones(self):
        """
        Get the tones of the scale, in cents above root
        :return: A sorted list of tones in the scale
        """
        return self.scale_df['tone'].to_list()

    def degree_from_tone(self, cents):
        """
        Get the scale degree for a given tone
        :param cents: the tone in cents above the root
        :return: the scale degree matching the tone,
        None if tone not found in scale
        """
        degree = None
        try:
            degree = self.scale_df.loc[
                self.scale_df['tone'] == cents, 'degree'].iloc[0]
        except KeyError:
            pass
        return degree

    def tone_from_degree(self, degree):
        """
        Get the tone (cents above root) for a scale degree
        :param degree: the degree of the scale matching the tone
        :return: the tone (in cents above root) for the supplied scale degree
        None if the degree not found in the scale
        """
        tone = None
        try:
            tone = self.scale_df.loc[
                self.scale_df['degree'] == degree, 'tone'].iloc[0]
        except KeyError:
            pass
        return tone

    @property
    def degree_steps_cents(self):
        """
        Get the steps of every degree (to the previous), in cents
        # TODO: make this directly from scale_df?
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
        # TODO: can we do this to scale_df inplace?
        new_df = self.scale_df.append({'tone': cents}, ignore_index=True)
        self.__scale_df = new_df
        self.rebuild_scale_df()
        return self.degree_from_tone(cents)

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
        new_degree = self.add_tone(self.tone_from_degree(degree) + cents)
        return new_degree

    def move_degree(self, degree, cents):
        """
        Move (retune) a degree by cents
        :param degree: the scale degree to retune
        :param cents: the number of cents by which to change the tone
        (can be negative)
        :return: 0 on success, -1 on error
        """
        if degree == 1 or degree not in self.degrees:
            # can't move the root or nonexisting degree
            return -1
        old_cents = self.tone_from_degree(degree)
        retval = self.remove_degree(degree)
        if retval != 0:
            # Something went wrong removing the old degree
            return -1
        new_degree = self.add_tone(old_cents + cents)
        if new_degree is None or new_degree == -1:
            # Re-tuned tone doesn't fit our scale constraints?
            # reset degree_tones and return error
            # FIXME: -1 means tone re-tuned to an existing tone, maybe that's ok?
            # restore the removed degree
            self.add_tone(old_cents)
            return -1
        return 0

    def remove_degree(self, degree):
        """
        Remove a scale degree
        :param degree:
        :return: 0 on success, -1 on error
        """
        if degree == 1 or degree not in self.degrees:
            # Can't remove root or nonexisting degree
            return -1
        self.__scale_df = self.scale_df[self.scale_df['degree'] != degree]
        self.rebuild_scale_df()
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
