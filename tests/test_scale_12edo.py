__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.scale_12edo as scale_12edo

SEMI = 100
WHOLE = SEMI * 2


@pytest.mark.parametrize(
    'initial, degrees, tones',
    [
        ([SEMI], [1, 2], [0, SEMI]),
        ([WHOLE], [1, 2], [0, WHOLE]),
        ([101], [1], [0]),
        (None, [1], [0])
    ],
)
def test_scale(initial, degrees, tones):
    test = scale_12edo.Scale12EDO(tones=initial)
    assert test.degrees == degrees
    assert test.tones == tones


@pytest.mark.parametrize(
    'initial, add, new, degrees, tones',
    [
        (None, SEMI, 2, [1, 2], [0, SEMI]),
        (None, WHOLE, 2, [1, 2], [0, WHOLE]),
        (None, 101, None, [1], [0]),
    ]
)
def test_scale_add(initial, add, new, degrees, tones):
    test = scale_12edo.Scale12EDO(tones=initial)
    retval = test.add_tone(add)
    assert retval == new
    assert test.degrees == degrees
    assert test.tones == tones


@pytest.mark.parametrize(
    'initial, degree, cents, new, degree_tones',
    [
        (list(range(100, 1200, 100)), 12, 200, None,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
        (list(range(100, 1200, 100)), 3, 111, None,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
    ]
)
def test_scale_insert_tone(initial, degree, cents, new, degree_tones):
    test = scale_12edo.Scale12EDO(tones=initial)
    retval = test.add_tone_rel_degree(degree=degree, cents=cents)
    assert retval == new
    assert test.degree_tones == degree_tones


@pytest.mark.parametrize(
    'initial, degree, cents, new, degree_tones',
    [
        (list(range(100, 1200, 100)), 12, 200, -1,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
        (list(range(100, 1200, 100)), 3, 1, -1,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
        (list(range(100, 1200, 100)), 3, -1, -1,
            {1: 0, 2: 100, 3: 200, 4: 300, 5: 400, 6: 500, 7: 600, 8: 700,
             9: 800, 10: 900, 11: 1000, 12: 1100}),
    ]
)
def test_scale_move_degree(initial, degree, cents, new, degree_tones):
    test = scale_12edo.Scale12EDO(tones=initial)
    retval = test.move_degree(degree=degree, cents=cents)
    assert retval == new
    assert test.degree_tones == degree_tones
