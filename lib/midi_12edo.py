"""
MIDI utilities for 12-EDO tuning
From https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies
"""

from numpy import log2
import pandas as pd

CONCERT_A_HZ = 440

def notes_df():
    """
    DataFrame of notes
    :return: dataframe
    """
    notes_sharps = ['C', 'C', 'D', 'D', 'E', 'F', 'F', 'G', 'G', 'A', 'A', 'B']
    accidentals = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
    notes_flats =['C', 'D', 'D', 'E', 'E', 'F', 'G', 'G', 'A', 'A', 'B', 'B']
    return pd.DataFrame({
        'halfstep': range(0, 12),
        'note_sharp': notes_sharps,
        'note_flat': notes_flats,
        'accidental': accidentals
    })

def octave_from_midi(midi_note):
    """
    Get octave number from MIDI number
    :param midi_note: MIDI note number
    :return: octave number
    """
    octave = None
    if midi_note >= 12:
        octave = int((midi_note / 12) - 1)
    elif midi_note >= 0:
        octave = -1
    return octave

def freq_from_midi(midi_note):
    """
    Frequency of MIDI note
    :param midi_note: MIDI note number
    :return: frequency in Hz
    """
    return CONCERT_A_HZ * 2 ** ((midi_note - 69) / 12)

def midi_from_freq(freq_hz):
    """
    MIDI note number for a given frequency
    :param freq_hz: frequency in Hz
    :return: MIDI note number (float, may need rounding by caller)
    """
    return 12 * log2(freq_hz/CONCERT_A_HZ) + 69

def piano_key_from_midi(midi_note):
    """
    Piano key number for a MIDI note number
    :param midi_note: MIDI note number
    :return: piano key number
    """
    return midi_note - 20
