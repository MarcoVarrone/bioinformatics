from nucleotide.bases.base import Base
from sequence_factory import SequenceFactory


class DNA:
    def __init__(self, sequence):
        if all(isinstance(element, Base) for element in sequence):
            self.sequence = sequence
        elif isinstance(sequence, str):
            self.sequence = SequenceFactory.create_dna(sequence)

    def __str__(self):
        representation = ''
        for base in self.sequence:
            representation += str(base)
        return representation
