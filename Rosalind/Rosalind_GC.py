# Computing GC content
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error

# Sample input:
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

# Sample Output
# Rosalind_0808
# 60.919540

# Read in and parse the files into a tuple
# count the GC content of the string with slice / count loop
# output the larges values and the name of the sequence (maybe dictionary??)
