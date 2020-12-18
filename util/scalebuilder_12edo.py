__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

import sys

sys.path.insert(0, '../lib')
import scale_12edo

MAJOR = [scale_12edo.WHOLE,
         scale_12edo.WHOLE,
         scale_12edo.HALF,
         scale_12edo.WHOLE,
         scale_12edo.WHOLE,
         scale_12edo.WHOLE,
         scale_12edo.HALF]
MODE = {
    'ionian': 0,
    'dorian': 1,
    'phrygian': 2,
    'lydian': 3,
    'mixolydian': 4,
    'aeolian': 5,
    'locrian': 6
}

# 12 EDO scales

def chromatic():
    myscale = scale_12edo.Scale12EDO(list(range(100, 1200, 100)))
    return myscale

def mode(mode):
    if mode not in MODE:
        return None
    myscale = scale_12edo.Scale12EDO()
    steps = (MAJOR[MODE[mode]:] + MAJOR[:MODE[mode]])
    for step in steps:
        myscale.add_tone(step)
    return myscale

def major():
    return mode('ionian')

def natminor():
    return mode('aeolian')