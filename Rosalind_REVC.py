#Complementing a Strand of DNA
#GIVEN: A DNA string (s) of length at most 1000 bp
#RETURN: the reverse complement (rc) of s

#Sample Data: AAAACCCGGT
#Sample Output: ACCGGGTTTT

#Need to find all instances of letter and replace
#But need to be careful not to be in endless loop, replacing A/T and C/G pairs
#slice by [::-1] to get rev_comp

#Create Dictionary
def complement(DNAinput):
	revcom_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	print revcom_dict
	revcom_list = []
	print revcom_list
	for letter in DNAinput:
		revcom = revcom_dict[letter]
		revcom_list.append(revcom)
		print revcom_list
	DNA_complement = ''.join(revcom_list)
	return DNA_complement
	
def ez_complement(DNAinput):
	revcom_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	revcom_str = ""
	for letter in DNAinput:
		revcom = revcom_dict[letter]
        revcom_str += revcom
	return revcom_str
  	
#iterates through the input string
#appends the value in the dictionary to a list
#converts the list into a string
#returns the complement of the input string


def reversed_sequence (DNAseq):
	reverse_comp_DNA = DNAseq [::-1]
	return reverse_comp_DNA
#slices the string in the -1 direction
#returns the reverse complement	of the input


Rosalind_input = "AAAACCCGGT"
DNA_comp = complement("TCTACCCCGACTGTAACCTGGTTCGGCACGATCAGTATAAGAACATGTGAGGCTGCGTGTAATAACGTGTAATTCTCTCTCTCCTTCGCTTCTGTAAGTGATTCATTCCCCTACAGAGTCCCGTAATGAAGATCAGCGCAGATGCGACGACACGCCTCGTTATCTTTGAGTGTCTGTCCGCAACCAAATGGGTATGAGGCAGGCGCCCCAATCTGTCAGTTAAAATCAATTATCAATCTAGGGCGAACCAGGTGCTGGCCGGAGTTCAACATAGTACAGAAACATTACCACGAGTTGGTGCTAAAATCAGGATGTCACTTCGGCTGGCTAGAAGACCTGAGCCGCCCATCAGAACACGCGCTAGCAAGCATGTGTTCTGACGGCTGATGGCGCTGCCTACGGCTAACAGGTTTTAACATGGGAAAATCCTTCGTTGTCTGCCGCTATTTGTCCAGCAGTATACGCGCCCGATGAACGAACTTAATCTGGTCTGAACTAGCTCTTGAGTTCATGTAGATTCTATCCTCTGTTCAAACAGGTATGACACGACCTAGAAGCACAAGCGCAATAGCCACCCAAGTACGGCCACTCCGGAATCTTGATTAAAGATTCCAGACAGACCTAGAGACCACCTGCCCTATTCTGCGCTGCAAGATAGAATGGCACTTTCTGAGGAGGCCTAATATGGGTTCGTCGGTTAGCGTCTCCAAGGTGCTAAACGCGGAGTTCGCAAGGATAAAAATGGGGTCAACTATAATGTTCAGACTCTAGCTCCGTCTGCCATAAGTGGATCGGGTATTAGCCTGAAATTGAAACCGCAATCTAGAGCGTAAGGGCCTGGTATTCTGTCTCCCCCGTGAGTTAC")
DNA_rev_comp = reversed_sequence(DNA_comp)
print DNA_rev_comp
