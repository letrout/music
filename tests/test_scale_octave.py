import pytest
import sys

sys.path.insert(0, '../lib')
import scale_octave

def test_scale_tone1200():
    test = scale_octave.ScaleOctave()
    retval = test.add_tone(1200)
    assert retval == 2
    assert test.degrees == [1, 2]
    assert test.tones == [0, 1200]

def test_scale_tone_overmax():
    test = scale_octave.ScaleOctave()
    retval = test.add_tone(scale_octave.OCTAVE_CENTS + 1)
    assert retval is None
    assert test.degrees == [1]
    assert test.tones == [0]
