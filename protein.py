from sequence import Sequence
from proteic.amino_acids import arginine, lysine, aspartic_acid, glutamic_acid, glutamine, asparagine, histidine
from proteic.amino_acids import serine, threonine, tyrosine, cysteine, tryptophan, alanine, isoleucine, leucine
from proteic.amino_acids import methionine, phenylalanine, valine, proline, glycine

alphabet = {'R': arginine.Arginine, 'K': lysine.Lysine, 'D': aspartic_acid.AsparticAcid,
            'E': glutamic_acid.GlutamicAcid, 'Q': glutamine.Glutamine, 'N': asparagine.Asparagine,
            'H': histidine.Histidine, 'S': serine.Serine, 'T': threonine.Threonine,
            'Y': tyrosine.Tyrosine, 'C': cysteine.Cysteine, 'W': tryptophan.Tryptophan,
            'A': alanine.Alanine, 'I': isoleucine.Isoleucine, 'L': leucine.Leucine,
            'M': methionine.Methionine, 'F': phenylalanine.Phenylalanine,
            'V': valine.Valine, 'P': proline.Proline, 'G': glycine.Glycine}


class Protein(Sequence):
    def __init__(self, sequence):
        super(Protein, self).__init__(sequence, alphabet)
