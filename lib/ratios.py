"""
Mathematical ratios for musical calculations
"""

__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

from math import log2

OCTAVE_CENTS = 1200

def cents(freq1, freq2):
    return OCTAVE_CENTS * log2(freq2 / freq1)

def freq_ratio(cents):
    return 2 ** (cents / OCTAVE_CENTS)