from .parser import read_fasta
from .properties import get_properties, sequence_to_properties
from .renderer import render_protein_portrait

def main():
    if _name_=="__main__":
        main()
protein_sequence = read_fasta("examples/xcl1.fasta")
protein = list(protein_sequence.keys())[0]
sequence = list(protein_sequence.values())[0]

properties = sequence_to_properties(sequence)
render_protein_portrait(
    properties, title="Protein Portrait for Sequence: " + protein, protein=protein)
