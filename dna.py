from sequence import Sequence
from nucleic.adenine import Adenine
from nucleic.cytosine import Cytosine
from nucleic.thymine import Thymine
from nucleic.guanine import Guanine

alphabet = {'A': Adenine, 'C': Cytosine, 'G': Guanine, 'T': Thymine}


class DNA(Sequence):
    def __init__(self, sequence):
        super(DNA, self).__init__(sequence, alphabet)
