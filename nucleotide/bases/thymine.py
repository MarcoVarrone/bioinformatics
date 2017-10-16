from nucleotide.bases.type.pyrimidine import Pyrimidine


class Thymine(Pyrimidine):
    def __init__(self):
        super(Thymine, self).__init__("T")

    def __str__(self):
        return self.symbol
