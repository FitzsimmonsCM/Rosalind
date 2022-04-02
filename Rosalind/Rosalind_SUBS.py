# Rosalind Finding a Motif in DNA
# Given: Two DNA strings ss and tt (each of length at most 1 kbp).
# Return: All locations of tt as a substring of ss.

# Sample Dataset: 
# String: GATATATGCATATACTT
# substring: ATAT

# Sample Output
# 2 4 10

# Hint
# Different programming languages use different notations for positions of 
# symbols in strings. Above, we use 1-based numbering, as opposed to 0-based numbering, 
# which is used in Python. For ss = "AUGCUUCAGAAAGGUCUUACG", 1-based numbering would 
# state that s[1]s[1] = 'A' is the first symbol of the string, whereas this symbol is 
# represented by s[0]s[0] in 0-based numbering. The idea of 0-based numbering 
# propagates to substring indexing, so that s[2:5]s[2:5] becomes "GCUU" instead of "UGCU".

# Note that in some programming languages, such as Python, s[j:k] returns 
# only fragment from index jj up to but not including index kk, so that s[2:5] 
# actually becomes "UGC", not "UGCU".

DNA_string = "GATATATGCATATACTT"
DNA_sub = "ATAT"

# count = str.count(DNA_sub)
# print count

DNA_motif = DNA_string["ATAT"]
print DNA_motif



	
	