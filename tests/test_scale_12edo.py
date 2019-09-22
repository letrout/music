import pytest
import sys

sys.path.insert(0, '../lib')
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
