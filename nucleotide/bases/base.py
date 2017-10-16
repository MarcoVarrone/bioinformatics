import sequence


class Base(object):
    def __init__(self, symbol):
        self.symbol = symbol

    def __add__(self, other):
        return sequence.Sequence(self.symbol + other.symbol)
