"""
note.py
A class to hold information about a musical note
"""

__author__ = "Joel Luth"
__copyright__ = "Copyright 2020, Joel Luth"
__credits__ = ["Joel Luth"]
__license__ = "MIT"
__maintainer__ = "Joel Luth"
__email__ = "joel.luth@gmail.com"
__status__ = "Prototype"

MAX_FREQ_HZ = 100 * 1000


class Note(object):
    """
    CLass to define a musical note
    """
    def __init__(self, freq_hz):
        """
        Constructor
        :param freq_hz: Frequency in Hz of the note
        """
        self.__freq = None

        self.freq = freq_hz

    @property
    def freq(self):
        """
        getter for self.__freq
        :return: the note's frequency in Hz
        """
        return self.__freq

    @freq.setter
    def freq(self, freq_hz):
        """
        Set this note's frequency in Hz
        :param freq_hz: frequency in Hz
        """
        # TODO: raise ValueError on invalid freq?
        if 0 < freq_hz <= MAX_FREQ_HZ:
            self.__freq = freq_hz
        else:
            raise ValueError("frequency Hz must be between {0} and {1}".format(
                0, MAX_FREQ_HZ))
