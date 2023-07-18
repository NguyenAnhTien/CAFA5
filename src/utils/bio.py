"""
@author : Tien Nguyen
@date   : 2023-07-11
"""
from Bio import SeqIO

def read_fasta(
        fasta_file: str
    ) -> dict:
    sequences = SeqIO.parse(fasta_file, "fasta")
    sequences = SeqIO.to_dict(sequences)
    return sequences
