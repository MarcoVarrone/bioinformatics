from nucleotide.bases.type.pyrimidine import Pyrimidine


class Cytosine(Pyrimidine):
    def __init__(self):
        super(Cytosine, self).__init__("C")
    
    def __str__(self):
        return self.symbol
