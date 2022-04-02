# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

# Sample Dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output: MAMAPRTEINSTRING

# slicing the string into triplet code
def mRNAcodonslice(mRNA_string):
	codon_list = []
	m = len(mRNA_string)
	for codon in mRNA_string:
		n = 0
		k = 3
		mRNA_string[n:k:3]
		codon_list.append(codon)
		n +=3
		k +=3
	return codon_list
		

def mRNAtranslation (codon_list):
	RNAcodon_dict = {
	'UUU': 'F', 
	'UUC': 'F',
	'UUA': 'L', 
	'UUG': 'L',
	'UCU': 'S',
	'UCC': 'S',
	'UCA': 'S',
	'UCG': 'S',
	'UAU': 'Y',
	'UAC': 'Y',
	'UAA': '.',
	'UAG': '.',
	'UGU': 'C',
	'UGC': 'C',
	'UGA': '.',
	'UGG': 'W',
	'CUU': 'L',
	'CUC': 'L',
	'CUA': 'L',
	'CUG': 'L',
	'CCU': 'P',
	'CCC': 'P',
	'CCA': 'P',
	'CCG': 'P',
	'CAU': 'H',
	'CAC': 'H',
	'CAA': 'Q',
	'CAG': 'Q',
	'CGU': 'R',
	'CGU': 'R',
	'CGC': 'R',
	'CGA': 'R',
	'CGG': 'R',
	'AUU': 'I',
	'AUC': 'I',
	'AUA': 'I',
	'AUG': 'M',
	'ACU': 'T',
	'ACC': 'T',
	'ACA': 'T',
	'ACG': 'T',
	'AAU': 'N',
	'AAC': 'N',
	'AAA': 'K',
	'AAG': 'K',
	'AGU': 'S',
	'AGC': 'S',
	'AGA': 'R', 
	'AGG': 'R',
	'GUU': 'V',
	'GUC': 'V',
	'GUA': 'V',
	'GUG': 'V',
	'GCU': 'A',
	'GCC': 'A',
	'GCA': 'A',
	'GCG': 'A',
	'GAU': 'D',
	'GAC': 'D',
	'GAA': 'E',
	'GAG': 'E',
	'GGU': 'G',
	'GGC': 'G',
	'GGA': 'G',
	'GGG': 'G',
	}
	return codon_dict

mRNA_input = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

test = mRNAcodonslice (mRNA_input)
print test
