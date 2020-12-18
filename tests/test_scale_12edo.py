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
import scale_12edo

SEMI = 100
WHOLE = SEMI * 2

def test_scale_semitone():
    test = scale_12edo.Scale12EDO(tones=[SEMI])
    assert test.degrees == [1, 2]
    assert test.tones == [0, SEMI]

def test_scale_add_semitone():
    test = scale_12edo.Scale12EDO()
    assert test.tones == [0]
    retval = test.add_tone(SEMI)
    assert retval == 2
    assert test.degrees == [1, 2]
    assert test.tones == [0, SEMI]

def test_scale_wholetone():
    test = scale_12edo.Scale12EDO(tones=[WHOLE])
    assert test.degrees == [1, 2]
    assert test.tones == [0, WHOLE]

def test_scale_add_wholetone():
    test = scale_12edo.Scale12EDO()
    assert test.degrees == [1]
    assert test.tones == [0]
    retval = test.add_tone(WHOLE)
    assert retval == 2
    assert test.degrees == [1, 2]
    assert test.tones == [0, WHOLE]

def test_scale_nontet():
    test = scale_12edo.Scale12EDO(tones=[101])
    assert test.degrees == [1]
    assert test.tones == [0]

def test_scale_add_nontet():
    test = scale_12edo.Scale12EDO()
    assert test.degrees == [1]
    assert test.tones == [0]
    retval = test.add_tone(101)
    assert retval is None
    assert test.degrees == [1]
    assert test.tones == [0]

def test_scale_insert_tone_overmax():
    test = scale_12edo.Scale12EDO(tones=list(range(100, 1200, 100)))
    retval = test.add_tone_rel_degree(degree=12, cents=200)
    assert retval is None
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }

def test_scale_insert_tone_nonet():
    test = scale_12edo.Scale12EDO(tones=list(range(100, 1200, 100)))
    retval = test.add_tone_rel_degree(degree=3, cents=111)
    assert retval is None
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }

def test_scale_move_tone_overmax():
    test = scale_12edo.Scale12EDO(tones=list(range(100, 1200, 100)))
    retval = test.move_degree(degree=12, cents=200)
    assert retval == -1
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }

def test_scale_move_tone_up_nonet():
    test = scale_12edo.Scale12EDO(tones=list(range(100, 1200, 100)))
    retval = test.move_degree(degree=3, cents=1)
    assert retval == -1
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }

def test_scale_move_tone_down_nonet():
    test = scale_12edo.Scale12EDO(tones=list(range(100, 1200, 100)))
    retval = test.move_degree(degree=3, cents=-1)
    assert retval == -1
    assert test.degree_tones == {
        1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
        9: 800, 10: 900, 11: 1000, 12: 1100
    }
