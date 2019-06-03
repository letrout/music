"""
MIDI utilities for 12-EDO tuning
From https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies
"""

from math import log2
import pandas as pd

CONCERT_A_HZ = 440

def notes_df():
    """
    DataFrame of notes
    :return: dataframe
    """
    notes_sharps = ['C', 'C', 'D', 'D', 'E', 'F', 'F', 'G', 'G', 'A', 'A', 'B']
    accidental = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    notes_flats =['C', 'D', 'D', 'E', 'E', 'F', 'G', 'G', 'A', 'B', 'B']
    accidentals = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    return pd.DataFrame({
        'halfstep': range(0, 11),
        'note_sharp': notes_sharps,
        'note_flat': notes_flats,
        'accidental': accidentals
    })

def octave_from_midi(midi_note):
    octave = None
    if midi_note >= 12:
        octave = int((midi_note / 12) - 1)
    elif midi_note >= 0:
        octave = -1
    return octave

def freq_from_midi(midi_note):
    return CONCERT_A_HZ * 2 ** ((midi_note - 69) / 12)

def midi_from_freq(freq_hz):
    return 12 * log2(freq_hz/CONCERT_A_HZ) + 69

def piano_key(midi_note):
        return midi_note - 20
