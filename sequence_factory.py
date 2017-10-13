from nucleotide.bases.adenine import Adenine
from nucleotide.bases.cytosine import Cytosine
from nucleotide.bases.guanine import Guanine
from nucleotide.bases.thymine import Thymine
from nucleotide.bases.uracil import Uracil


class SequenceFactory(object):
    @staticmethod
    def create_dna(sequence_str):
        sequence = []
        for element in sequence_str:
            if element == "A":
                sequence.append(Adenine())
            elif element == "C":
                sequence.append(Cytosine())
            elif element == "G":
                sequence.append(Guanine())
            elif element == "T":
                sequence.append(Thymine())
            else:
                raise ValueError("Try to create a base of non-existing type")
        return sequence
