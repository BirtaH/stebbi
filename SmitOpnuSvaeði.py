import random

class SmitOpnuSvaeði:
    def __init__(self):

        self._number = None

    def roll_dice(self):
        self._number = 1 + random.randrange(100)
        if self.numer > 95:
            return True
        else:
            return False
