__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.midi_12edo as midi_12edo


def test_notes_df_halfstep():
    test = midi_12edo.notes_df()
    assert test.iloc[3]['halfstep'] == 3


def test_notes_df_note_sharp():
    test = midi_12edo.notes_df()
    assert test.iloc[7]['note_sharp'] == 'G'


def test_notes_df_note_flat():
    test = midi_12edo.notes_df()
    assert test.iloc[10]['note_flat'] == 'B'


def test_notes_df_accidental():
    test = midi_12edo.notes_df()
    assert test.iloc[5]['accidental'] == 0


def test_octave_from_midi_vlow():
    test = midi_12edo.octave_from_midi(5)
    assert test == -1


def test_octave_from_midi_low():
    test = midi_12edo.octave_from_midi(21)
    assert test == 0


def test_octave_from_midi_mid():
    test = midi_12edo.octave_from_midi(30)
    assert test == 1


def test_octave_from_midi_high():
    test = midi_12edo.octave_from_midi(51)
    assert test == 3


def test_freq_from_midi():
    test = midi_12edo.freq_from_midi(69)
    assert test == 440


def test_midi_from_freq():
    test = midi_12edo.midi_from_freq(440)
    assert test == 69


def test_piano_key_from_midi():
    test = midi_12edo.piano_key_from_midi(108)
    assert test == 88
