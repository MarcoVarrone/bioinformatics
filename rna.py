from nucleic.adenine import Adenine
from nucleic.cytosine import Cytosine
from nucleic.uracil import Uracil

from nucleic.guanine import Guanine
from sequence import Sequence

alphabet = {'A': Adenine, 'C': Cytosine, 'G': Guanine, 'U': Uracil}


class RNA(Sequence):
    def __init__(self, sequence):
        super(RNA, self).__init__(sequence, alphabet)
