# Given an amino acid letter, return its chemical properties.
# Hydrophobicity value is based on the Kyte-Doolittle scale. Size is based on molecular weight in Da.
AMINO_ACID_PROPERTIES = {
    'A': {'name': 'Alanine', 'polarity': 'nonpolar', 'hydrophobicity': 1.8, 'charge': 0, 'size': 89},
    'C': {'name': 'Cysteine', 'polarity': 'polar', 'hydrophobicity': 2.5, 'charge': 0, 'size': 121},
    'D': {'name': 'Aspartic acid', 'polarity': 'polar', 'hydrophobicity': -3.5, 'charge': -1, 'size': 133},
    'E': {'name': 'Glutamic acid', 'polarity': 'polar', 'hydrophobicity': -3.5, 'charge': -1, 'size': 147},
    'F': {'name': 'Phenylalanine', 'polarity': 'nonpolar', 'hydrophobicity': 2.8, 'charge': 0, 'size': 165},
    'G': {'name': 'Glycine', 'polarity': 'nonpolar', 'hydrophobicity': -0.4, 'charge': 0, 'size': 75},
    'H': {'name': 'Histidine', 'polarity': 'polar', 'hydrophobicity': -3.2, 'charge': 0, 'size': 155},
    'I': {'name': 'Isoleucine', 'polarity': 'nonpolar', 'hydrophobicity': 4.5, 'charge': 0, 'size': 131},
    'K': {'name': 'Lysine', 'polarity': 'polar', 'hydrophobicity': -3.9, 'charge': +1, 'size': 146},
    'L': {'name': 'Leucine', 'polarity': 'nonpolar', 'hydrophobicity': 3.8, 'charge': 0, 'size': 131},
    'M': {'name': 'Methionine', 'polarity': 'nonpolar', 'hydrophobicity': 1.9, 'charge': 0, 'size': 149},
    'N': {'name': 'Asparagine', 'polarity': 'polar', 'hydrophobicity': -3.5, 'charge': 0, 'size': 132},
    'P': {'name': 'Proline', 'polarity': 'nonpolar', 'hydrophobicity': -1.6, 'charge': 0, 'size': 115},
    'Q': {'name': 'Glutamine', 'polarity': 'polar', 'hydrophobicity': -3.5, 'charge': 0, 'size': 147},
    'R': {'name': 'Arginine', 'polarity': 'polar', 'hydrophobicity': -4.5, 'charge': +1, 'size': 174},
    'S': {'name': 'Serine', 'polarity': 'polar', 'hydrophobicity': -0.8, 'charge': 0, 'size': 105},
    'T': {'name': 'Threonine', 'polarity': 'polar', 'hydrophobicity': -0.7, 'charge': 0, 'size': 119},
    'V': {'name': 'Valine', 'polarity': 'nonpolar', 'hydrophobicity': 4.2, 'charge': 0, 'size': 117},
    'W': {'name': 'Tryptophan', 'polarity': 'nonpolar', 'hydrophobicity': -0.9, 'charge': 0, 'size': 204},
    'Y': {'name': 'Tyrosine', 'polarity': 'nonpolar', 'hydrophobicity': -1.3, 'charge': 0, 'size': 181},

}


def get_properties(amino_acid):
    """Return the properties of a given amino acid letter."""
    return AMINO_ACID_PROPERTIES.get(amino_acid.upper(), None)


def sequence_to_properties(sequence):
    """Convert a sequence of amino acids to their properties."""
    return [get_properties(aa) for aa in sequence if get_properties(aa) is not None]
