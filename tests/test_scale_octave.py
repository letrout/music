__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.scale_octave as scale_octave


@pytest.mark.parametrize(
    'initial, tone, new, degrees, tones',
    [
        (None, 1200, 2, [1, 2], [0, 1200]),
        (None, scale_octave.OCTAVE_CENTS + 1, None, [1], [0])
    ],
)
def test_scale_add_tone(initial, tone, new, degrees, tones):
    test = scale_octave.ScaleOctave(tones=initial)
    retval = test.add_tone(tone)
    assert retval == new
    assert test.degrees == degrees
    assert test.tones == tones


@pytest.mark.parametrize(
    'initial, degree, cents, new, degree_tones',
    [
        (list(range(100, 1200, 100)), 12, 200, None,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
    ],
)
def test_scale_add_tone_rel_degree(initial, degree, cents, new, degree_tones):
    test = scale_octave.ScaleOctave(tones=initial)
    retval = test.add_tone_rel_degree(degree=degree, cents=cents)
    assert retval == new
    assert test.degree_tones == degree_tones


@pytest.mark.parametrize(
    'initial, degree, cents, new, degree_tones',
    [
        (list(range(100, 1200, 100)), 11, 201, -1,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
    ],
)
def test_scale_move_degree(initial, degree, cents, new, degree_tones):
    test = scale_octave.ScaleOctave(tones=initial)
    retval = test.move_degree(degree=degree, cents=cents)
    assert retval == new
    assert test.degree_tones == degree_tones
