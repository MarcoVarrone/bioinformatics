from sequence import Sequence


class DNA(Sequence):
    def __init__(self, sequence):
        allowed_bases = ['A', 'C', 'G', 'T']
        if all(x in allowed_bases for x in sequence):
            super(DNA, self).__init__(sequence)
        else:
            raise ValueError('The sequence is not allowed.')

    def __str__(self):
        representation = ''
        for base in self.sequence:
            representation += str(base)
        return representation
