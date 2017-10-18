from sequence import Sequence
from dna import DNA
from nucleic.adenine import Adenine
from nucleic.cytosine import Cytosine
from nucleic.thymine import Thymine
from nucleic.guanine import Guanine

dna1 = DNA('GAATC')
dna2 = DNA('CATAC')

sub_matrix = {Adenine:  {Adenine: 10, Cytosine: -5, Guanine: 0, Thymine: -5},
              Cytosine: {Adenine: -5, Cytosine: 10, Guanine: -5, Thymine: 0},
              Guanine:  {Adenine: 0,  Cytosine: -5, Guanine: 10, Thymine: -5},
              Thymine:  {Adenine: -5, Cytosine: 0,  Guanine: -5, Thymine: 10}}


def needle(seq1: Sequence, seq2: Sequence, sub_matrix, gap_penalty):
    matrix = [[None for _ in range(len(seq1)+1)] for _ in range(len(seq2)+1)]
    matrix[0][0] = 0
    matrix = fill_first_lines(matrix, gap_penalty)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            element1 = seq1[j-1]
            element2 = seq2[i-1]
            matrix[i][j] = max(matrix[i-1][j-1] + sub_matrix[element1.__class__][element2.__class__],
                               matrix[i-1][j] - gap_penalty,
                               matrix[i][j-1] - gap_penalty)

    return matrix

def fill_first_lines(matrix, gap_penalty):
    for i in range(1, len(matrix[0])):
        matrix[0][i] = matrix[0][i-1] - gap_penalty
    for i in range(1, len(matrix)):
        matrix[i][0] = matrix[i-1][0] - gap_penalty
    return matrix



matrix = needle(dna1, dna2, sub_matrix, 4)