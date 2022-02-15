__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.note as note

FREQ_ERROR_MSG = f'frequency Hz must be between 0 and {note.MAX_FREQ_HZ}'


@pytest.mark.parametrize(
    'freq, expected',
    [
        (440, 440),
    ],
)
def test_note_freq_ok(freq, expected):
    test = note.Note(freq)
    assert test.freq == expected


@pytest.mark.parametrize(
    'freq, expected',
    [
        (-1, FREQ_ERROR_MSG),
        (0, FREQ_ERROR_MSG),
        (note.MAX_FREQ_HZ + 1, FREQ_ERROR_MSG),
    ],
)
def test_note_freq_error(freq, expected):
    with pytest.raises(ValueError) as excinfo:
        test = note.Note(freq)
    assert str(excinfo.value) == expected


@pytest.mark.parametrize(
    'freq, change, expected',
    [
        (440, 450, 450),
    ],
)
def test_note_freq_change(freq, change, expected):
    test = note.Note(freq)
    test.freq = change
    assert test.freq == expected


@pytest.mark.parametrize(
    'freq, change, expected',
    [
        (440, 0, FREQ_ERROR_MSG),
        (440, note.MAX_FREQ_HZ + 1, FREQ_ERROR_MSG),
    ],
)
def test_note_freq_change_error(freq, change, expected):
    test = note.Note(freq)
    with pytest.raises(ValueError) as excinfo:
        test.freq = change
    assert str(excinfo.value) == expected
