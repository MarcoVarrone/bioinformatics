import nucleotide.bases as bases


def create(seq_str):
    sequence = []
    for element in seq_str:
        if element == "A":
            sequence.append(bases.adenine.Adenine())
        elif element == "C":
            sequence.append(bases.cytosine.Cytosine())
        elif element == "G":
            sequence.append(bases.guanine.Guanine())
        elif element == "T":
            sequence.append(bases.thymine.Thymine())
        elif element == "U":
            sequence.append(bases.uracil.Uracil())
        else:
            raise ValueError("Try to create a base of non-existing type")
    return sequence


class Sequence:
    def __init__(self, sequence):
        if all(isinstance(element, bases.base.Base) for element in sequence):
            self.sequence = sequence
        elif isinstance(sequence, str):
            self.sequence = create(sequence)

    def __repr__(self):
        seq_str = map(lambda x: str(x), self.sequence)
        return "".join(seq_str)

