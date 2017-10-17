from sequence import Sequence
from nucleotide.bases.adenine import Adenine
from nucleotide.bases.cytosine import Cytosine
from nucleotide.bases.guanine import Guanine
from nucleotide.bases.thymine import Thymine

alphabet = {'A': Adenine, 'C': Cytosine, 'G': Guanine, 'T': Thymine}


class DNA(Sequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, alphabet)

    def __str__(self):
        representation = ''
        for base in self.sequence:
            representation += str(base)
        return representation
