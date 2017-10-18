'''AAs = [('Arg', 'R'), ('Lys', 'K'), ('Asp', 'D'), ('Glu', 'E'), ('Gln', 'Q'), ('Asn', 'N'), ('His', 'H'),
       ('Ser', 'S'), ('Thr', 'T'), ('Tyr', 'Y'), ('Cys', 'C'), ('Trp', 'W'), ('Ala', 'A'), ('Ile', 'I'),
       ('Leu', 'L'), ('Met', 'M'), ('Phe', 'F'), ('Val', 'V'), ('Pro', 'P'), ('Gly', 'G') ]'''


class AminoAcid:
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol
