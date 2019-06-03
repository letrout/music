import pytest
import sys

sys.path.insert(0, '../lib')
import note
import scale

def test_scale_noroot():
    test = scale.Scale()
    assert test.root_note is None

def test_scale_a_440():
    a_440 = note.Note(440)
    test = scale.Scale(a_440)
    assert test.root_note.freq == 440

def test_scale_hz():
    test = scale.Scale(440)
    assert test.root_note.freq == 440

def test_scale_badroot_hz():
    with pytest.raises(ValueError):
        test = scale.Scale(-1)

def test_scale_freq_change():
    test = scale.Scale(440)
    assert test.freq_change(660) == 1.5