"""
Mathematical ratios for musical calculations
"""

from numpy import log2

OCTAVE_CENTS = 1200

def cents(freq1, freq2):
    return OCTAVE_CENTS * log2(freq2 / freq1)

def freq_ratio(cents):
    return 2 ** (cents / OCTAVE_CENTS)