import sys

sys.path.insert(0, '../lib')
import note
import scale

SEMI = 100
WHOLE = 2 * SEMI
EDO12_MAJ = [WHOLE, WHOLE, SEMI, WHOLE, WHOLE, WHOLE, SEMI]
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

def edo12_chromatic():
    myscale = scale.Scale(list(range(100, 1200, 100)))
    return myscale

def edo12_mode(mode):
    if mode not in MODE:
        return None
    myscale = scale.Scale()
    steps = (EDO12_MAJ[MODE[mode]:] + EDO12_MAJ[:MODE[mode]])
    for step in steps:
        myscale.add_tone(step)
    return myscale

def edo12_major():
    return edo12_mode('ionian')

def edo12_natminor():
    return edo12_mode('aeolian')