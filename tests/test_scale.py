__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.note as note
import lib.scale as scale

FREQ_ERROR_MSG = f'frequency Hz must be between 0 and {note.MAX_FREQ_HZ}'


@pytest.mark.parametrize(
    'scale_root, root_freq, degrees, tones',
    [
        (None, None, [1], [0]),
        ('xyz', None, [1], [0]),
    ],
)
def test_scale_noroot(scale_root, root_freq, degrees, tones):
    test = scale.Scale(root_note=scale_root)
    assert test.root_note == root_freq
    assert test.degrees == degrees
    assert test.tones == tones


@pytest.mark.parametrize(
    'scale_root, root_freq',
    [
        (440, 440),
        (note.Note(440), 440),
    ],
)
def test_scale(scale_root, root_freq):
    test = scale.Scale(root_note=scale_root)
    assert test.root_note.freq == root_freq


@pytest.mark.parametrize(
    'root_note, expected',
    [
        (-1, FREQ_ERROR_MSG),
        (0, FREQ_ERROR_MSG),
    ],
)
def test_scale_badroot_hz(root_note, expected):
    with pytest.raises(ValueError) as excinfo:
        test = scale.Scale(root_note=root_note)
    assert str(excinfo.value) == expected


@pytest.mark.parametrize(
    'root_freq, new_freq, ratio',
    [
        (440, 660, 1.5),
    ]
)
def test_scale_freq_ratio(root_freq, new_freq, ratio):
    test = scale.Scale(root_note=root_freq)
    assert test.freq_ratio(new_freq) == ratio


@pytest.mark.parametrize(
    'scale_root, new_tones, degrees, tones',
    [
        (None, [0], [1], [0]),
        (None, list(range(100, 1200, 100)), list(range(1, 13)),
            list(range(0, 1200, 100)))
    ]
)
def test_scale_add_tone(scale_root, new_tones, degrees, tones):
    test = scale.Scale(root_note=scale_root)
    for new_tone in new_tones:
        test.add_tone(new_tone)
    assert test.degrees == degrees
    assert test.tones == tones


def test_add_tone_bad():
    test = scale.Scale(tones=[200, 400, 700, 900, 1100, 1200])
    retval = test.add_tone('100cents')
    assert retval is None
    assert test.degree_steps_cents == {
        1: 0, 2: 200, 3: 200, 4: 300, 5: 200, 6: 200, 7: 100
    }


def test_scale_single_tones():
    test = scale.Scale()
    for i in range(1, 12):
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


@pytest.mark.parametrize(
    'init_tones, degrees, tones',
    [
        ('bad', [1], [0]),
        (['bad', 2], [1], [0])
    ]
)
def test_scale_bad_tone(init_tones, degrees, tones):
    test = scale.Scale(tones=init_tones)
    assert test.degrees == degrees
    assert test.tones == tones


@pytest.mark.parametrize(
    'init_tones, degree_cents',
    [
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            {1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100}
        ),
    ]
)
def test_scale_degree_cents(init_tones, degree_cents):
    test = scale.Scale(tones=init_tones)
    assert test.degree_steps_cents == degree_cents


@pytest.mark.parametrize(
    'init_tones, degree, cents, new, degree_cents',
    [
        (
            [200, 400, 700, 900, 1100, 1200],
            3,
            100,
            4,
            {1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100}
        ),
        (
            [200, 400, 700, 900, 1100, 1200],
            2,
            300,
            4,
            {1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100}
        ),
        (
            [200, 400, 700, 900, 1100, 1200],
            9,
            100,
            -1,
            {1: 0, 2: 200, 3: 200, 4: 300, 5: 200, 6: 200, 7: 100}
        ),
        (
            [200, 400, 700, 900, 1100, 1200],
            4,
            -200,
            4,
            {1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100}
        ),
        (
            [200, 400, 700, 900, 1100, 1200],
            5,
            -400,
            4,
            {1: 0, 2: 200, 3: 200, 4: 100, 5: 200, 6: 200, 7: 200, 8: 100}
        ),
        (
            [200, 400, 700, 900, 1100, 1200],
            4,
            -800,
            None,
            {1: 0, 2: 200, 3: 200, 4: 300, 5: 200, 6: 200, 7: 100}
        )
    ]
)
def test_add_tone_rel_degree(init_tones, degree, cents, new, degree_cents):
    test = scale.Scale(tones=init_tones)
    retval = test.add_tone_rel_degree(degree=degree, cents=cents)
    assert retval == new
    assert test.degree_steps_cents == degree_cents


@pytest.mark.parametrize(
    'init_tones, degrees, remove_degree, new, new_degrees, new_tones',
    [
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            3,
            0,
            [1, 2, 3, 4, 5, 6, 7],
            [0, 200, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            9,
            -1,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 200, 400, 500, 700, 900, 1100, 1200]
        )
    ]
)
def test_scale_remove_degree(
        init_tones, degrees, remove_degree, new, new_degrees, new_tones):
    test = scale.Scale(tones=init_tones)
    assert test.degrees == degrees
    retval = test.remove_degree(remove_degree)
    assert retval == new
    assert test.degrees == new_degrees
    assert test.tones == new_tones


@pytest.mark.parametrize(
    'init_tones, degrees, move_degree, move_cents, new, new_degrees, new_tones',
    [
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            2,
            50,
            0,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 250, 400, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            2,
            250,
            0,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 400, 450, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            2,
            -50,
            0,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 150, 400, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            3,
            -250,
            0,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 150, 200, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            2,
            -500,
            -1,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 200, 400, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            9,
            50,
            -1,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 200, 400, 500, 700, 900, 1100, 1200]
        ),
        (
            [200, 400, 500, 700, 900, 1100, 1200],
            [1, 2, 3, 4, 5, 6, 7, 8],
            1,
            50,
            -1,
            [1, 2, 3, 4, 5, 6, 7, 8],
            [0, 200, 400, 500, 700, 900, 1100, 1200]
        )
    ]
)
def test_move_degree(
        init_tones, degrees, move_degree, move_cents, new, new_degrees, new_tones):
    test = scale.Scale(tones=init_tones)
    assert test.degrees == degrees
    retval = test.move_degree(degree=move_degree, cents=move_cents)
    assert retval == new
    assert test.degrees == new_degrees
    assert test.tones == new_tones
