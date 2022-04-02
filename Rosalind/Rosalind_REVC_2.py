def complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    bases = list(seq) 
    bases = [complement[base] for base in bases] 
    return ''.join(bases)
    def reverse_complement(s):
    	return complement(s[::-1])

    print(reverse_complement("AAAACCCGGT"))