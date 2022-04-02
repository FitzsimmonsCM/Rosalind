#!/usr/bin/python

# pseudocode
# 1. read in the fasta files
# 2. break up the sequence id and the sequence
# 3. count the GC content associated with that string of letters
# 4. append that GC content to the sequence id
# 5. Print the sequence ID of the highest GC content and the percent GC content

from Bio import SeqIO

def import_FASTA(sequence):
    for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    return


my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
GC(my_seq)
