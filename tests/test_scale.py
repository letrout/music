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
    assert test.degrees == [1]
    assert test.tones == [0]

def test_scale_single_tones():
    test = scale.Scale()
    for i in range(1,12):
        test.add_tone(i * 100)
    assert test.degrees == list(range(1, 13))
    assert test.tones[8] == 800
    assert test.tones[0] == 0
    assert len(test.tones) == 12

def test_scale_tones_array():
    test = scale.Scale(tones=list(range(100, 1200, 100)))
    assert test.degrees == list(range(1, 13))
    assert test.tones[8] == 800
    assert test.tones[0] == 0
    assert len(test.tones) == 12

def test_scale_bad_tone():
    test = scale.Scale(tones='bad')
    assert test.degrees == [1]
    assert test.tones == [0]

def test_scale_bad_tones_list():
    test = scale.Scale(tones=['bad', 2])
    assert test.degrees == [1]
    assert test.tones == [0]

def test_scale_degree_cents():
    test = scale.Scale(tones=[200, 400, 500, 700, 900, 1100, 1200])
    assert test.degree_steps_cents == {
        1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100
    }

def test_add_tone_above_degree():
    test = scale.Scale(tones=[200, 400, 700, 900, 1100, 1200])
    retval = test.add_tone_above_degree(degree=3, cents=100)
    assert retval == 4
    assert test.degree_steps_cents == {
        1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100
    }

def test_add_tone_above_degree_jump():
    test = scale.Scale(tones=[200, 400, 700, 900, 1100, 1200])
    retval = test.add_tone_above_degree(degree=2, cents=300)
    assert retval == 4
    assert test.degree_steps_cents == {
        1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100
    }

def test_add_tone_above_bad_degree():
    test = scale.Scale(tones=[200, 400, 700, 900, 1100, 1200])
    retval = test.add_tone_above_degree(degree=9, cents=100)
    assert retval == -1
    assert test.degree_steps_cents == {
        1: 0, 2: 200, 3: 200, 4: 300, 5: 200, 6: 200, 7: 100
    }