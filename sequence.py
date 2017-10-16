from nucleotide.bases import base, adenine, cytosine, guanine, thymine, uracil


def create(seq_str):
    sequence = []
    for element in seq_str:
        if element == "A":
            sequence.append(adenine.Adenine())
        elif element == "C":
            sequence.append(cytosine.Cytosine())
        elif element == "G":
            sequence.append(guanine.Guanine())
        elif element == "T":
            sequence.append(thymine.Thymine())
        elif element == "U":
            sequence.append(uracil.Uracil())
        else:
            raise ValueError("Try to create a base of non-existing type")
    return sequence


class Sequence:
    def __init__(self, sequence):
        if all(isinstance(element, base.Base) for element in sequence):
            self.sequence = sequence
        elif isinstance(sequence, str):
            self.sequence = create(sequence)

    def __add__(self, other):
        return Sequence(str(self) + str(other))

    def __repr__(self):
        seq_str = map(lambda x: str(x), self.sequence)
        return "".join(seq_str)


