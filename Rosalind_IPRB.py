# Rosalind IPRB
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
# (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Input
# 2 2 2

# Sample Output
# 0.78333


# Ask the user for input values
k = int(input ("Enter value for k: "))
m = int(input ("Enter value for m: "))
n = int(input ("Enter value for n: "))


d = k + m + n

# make dictionaries for pairs of parents

# dict 1 = prob of getting that pair of parents
# dict 2 = prob of getting offspring with dominant allele given that set of parents

# interate through them together

mendel_dict ={

'DDvsDD': 1,
'DDvsDd': 1,
'DDvsdd': 1,
'DdvsDD': 1,
'DdvsDd': 0.75,
'Ddvsdd': 0.50,
'ddvsDD': 1,
'ddvsDd': 0.5,
'ddvsdd': 0
}
