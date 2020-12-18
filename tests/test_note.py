__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest
import sys

sys.path.insert(0, './lib')
import note

def test_note_freq_too_low():
    with pytest.raises(ValueError):
        test = note.Note(-1)

def test_note_freq_ok():
    test = note.Note(440)
    assert test.freq == 440

def test_note_freq_too_high():
    with pytest.raises(ValueError):
        test = note.Note(100 * 1024 * 1024)

def test_note_freq_change():
    test = note.Note(440)
    test.freq = 450
    assert test.freq == 450
