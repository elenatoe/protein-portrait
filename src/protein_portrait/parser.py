# Functions for reading protein sequence files
def read_fasta(file_path):
    """
    Reads a FASTA file and returns a dictionary of sequences.

    Args:
        file_path (str): Path to the FASTA file.

    Returns:
        dict: A dictionary where keys are sequence IDs and values are the corresponding sequences.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        sequence_id = None
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence_id is not None:
                    sequences[sequence_id] = ''.join(sequence)
                header = line[1:].strip()
                parts = header.split("|")
                sequence_id = parts[2] if len(parts) >= 3 else parts[0]
                sequence = []
            else:
                sequence.append(line)
        if sequence_id is not None:
            sequences[sequence_id] = ''.join(sequence)
    return sequences
