__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

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

def test_scale_insert_tone_overmax():
    test = scale_octave.ScaleOctave(tones=list(range(100, 1200, 100)))
    retval = test.add_tone_rel_degree(degree=12, cents=200)
    assert retval is None
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }

def test_scale_move_tone_overmax():
    test = scale_octave.ScaleOctave(tones=list(range(100, 1200, 100)))
    retval = test.move_degree(degree=11, cents=201)
    assert retval == -1
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }