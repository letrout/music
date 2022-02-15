__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.midi_12edo as midi_12edo


@pytest.mark.parametrize(
    'index, rel, expected',
    [
        (3, 'halfstep', 3),
        (7, 'note_sharp', 'G'),
        (10, 'note_flat', 'B'),
        (5, 'accidental', 0)
    ],
)
def test_notes_df(index, rel, expected):
    test = midi_12edo.notes_df()
    assert test.iloc[index][rel] == expected


@pytest.mark.parametrize(
    'midi, octave',
    [
        (5, -1),
        (21, 0),
        (30, 1),
        (51, 3)
    ],
)
def test_octave_from_midi(midi, octave):
    test = midi_12edo.octave_from_midi(midi)
    assert test == octave


@pytest.mark.parametrize(
    'midi, freq',
    [
        (69, 440)
    ],
)
def test_freq_from_midi(midi, freq):
    test = midi_12edo.freq_from_midi(midi)
    assert test == freq


@pytest.mark.parametrize(
    'freq, midi',
    [
        (440, 69)
    ],
)
def test_midi_from_freq(freq, midi):
    test = midi_12edo.midi_from_freq(freq)
    assert test == midi


@pytest.mark.parametrize(
    'midi, key',
    [
        (100, 80)
    ],
)
def test_piano_key_from_midi(midi, key):
    test = midi_12edo.piano_key_from_midi(midi)
    assert test == key
