from nucleotide.bases.type.purine import Purine


class Adenine(Purine):
    def __init__(self):
        super(Adenine, self).__init__("A")

    def __str__(self):
        return self.symbol
