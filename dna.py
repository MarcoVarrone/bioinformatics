from collections import OrderedDict

from sequence import Sequence
from nucleic.adenine import Adenine
from nucleic.cytosine import Cytosine
from nucleic.thymine import Thymine
from nucleic.guanine import Guanine

alphabet = {'A': Adenine, 'C': Cytosine, 'G': Guanine, 'T': Thymine}
complements = {Adenine: Guanine, Cytosine: Thymine, Guanine: Adenine, Thymine: Cytosine}



class DNA(Sequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, alphabet)

    def prova(self):
        return self.sequence

    def complement(self):
        return DNA(list(map(lambda x: complements[x.__class__](), self.sequence)))

    def reverse(self):
        return DNA(str(self)[::1])



    def __str__(self):
        return super(DNA, self).__str__()

