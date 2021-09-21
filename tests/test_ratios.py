__author__ = "Joel Luth"
__copyright__ = "Copyright 2021, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import pytest

import lib.ratios as ratios


def test_cents_neg():
    test = ratios.cents(880, 440)
    assert test == -1200


def test_cents_pos():
    test = ratios.cents(440, 880)
    assert test == 1200


def test_freq_ratio():
    test = ratios.freq_ratio(2400)
    assert test == 4
