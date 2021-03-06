from nucleic.base import Base


def str_to_sequence(string, alphabet):
    sequence = []
    for element in string:
        try:
            sequence.append(alphabet[element]())
        except KeyError:
            raise ValueError('The sequence is not valid')
    return sequence


class Sequence:
    def __init__(self, sequence, alphabet=None):
        self.alphabet = alphabet
        if all(isinstance(element, Base) for element in sequence):
            self.sequence = sequence
        elif all(isinstance(element, str) for element in sequence):
            self.sequence = list(map(lambda x: alphabet[x](), sequence))
        elif isinstance(sequence, str):
            if alphabet is None:
                self.sequence = sequence
            else:
                self.sequence = str_to_sequence(sequence, alphabet)
        else:
            raise ValueError('Invalid sequence.')

    def __getitem__(self, key):
        return self.sequence[key]

    def __len__(self):
        return len(self.sequence)

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return Sequence(str(self) + str(other), self.alphabet)
        return False

    def __str__(self):

        seq_str = map(lambda x: str(x), self.sequence)
        return "".join(seq_str)


