__author__ = "Joel Luth"
__copyright__ = "Copyright 2021, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.ratios as ratios


@pytest.mark.parametrize(
    'freq1, freq2, cents',
    [
        (880, 440, -1200),
        (440, 880, 1200),
        (440, 440, 0),
    ],
)
def test_cents(freq1, freq2, cents):
    test = ratios.cents(freq1, freq2)
    assert test == cents


@pytest.mark.parametrize(
    'cents, ratio',
    [
        (2400, 4),
        (0, 1),
        (-1200, 0.5),
    ],
)
def test_freq_ratio(cents, ratio):
    test = ratios.freq_ratio(cents)
    assert test == ratio
