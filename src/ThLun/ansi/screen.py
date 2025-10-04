"""
Screen and cursor operations for ThLun library.
Contains platform-agnostic functions for clearing the screen and moving the cursor.
"""

CSI = '\033['
OSC = '\033]'
BEL = '\a'

def clear_screen(mode=2):
    return CSI + str(mode) + 'J'

def clear_line(mode=2):
    return CSI + str(mode) + 'K'

class Cursor:
    @staticmethod
    def UP(n=1):
        return CSI + str(n) + 'A'
    @staticmethod
    def DOWN(n=1):
        return CSI + str(n) + 'B'
    @staticmethod
    def FORWARD(n=1):
        return CSI + str(n) + 'C'
    @staticmethod
    def BACK(n=1):
        return CSI + str(n) + 'D'
    @staticmethod
    def POS(x=1, y=1):
        return CSI + f"{y};{x}H"
