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
    test = scale.Scale(root_note=a_440)
    assert test.root_note.freq == 440

def test_scale_hz():
    test = scale.Scale(root_note=440)
    assert test.root_note.freq == 440

def test_scale_badroot_hz():
    with pytest.raises(ValueError):
        test = scale.Scale(root_note=-1)

def test_scale_badroot_type():
    test = scale.Scale(root_note='xyz')
    assert test.root_note is None

def test_scale_freq_change():
    test = scale.Scale(root_note=440)
    assert test.freq_ratio(660) == 1.5

def test_scale_tone_0():
    test = scale.Scale()
    assert test.degrees == [1]
    assert test.tones == [0]
    test.add_tone(0)
    assert test.tones == [0]

def test_scale_single_tones():
    test = scale.Scale()
    for i in range(1,12):
        test.add_tone(i * 100)
    assert test.tones[8] == 800
    assert test.tones[0] == 0
    assert len(test.tones) == 12

def test_scale_tones_array():
    test = scale.Scale(tones=list(range(100,1200, 100)))
    assert test.tones[8] == 800
    assert test.tones[0] == 0
    assert len(test.tones) == 12

def test_scale_bad_tone():
    test = scale.Scale(tones='bad')
    assert test.tones == [0]

def test_scale_bad_tones_list():
    test = scale.Scale(tones=['bad', 2])
    assert test.tones == [0]
