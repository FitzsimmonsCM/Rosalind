# Given: A positive integer n less than or equal to 7
# Return: The total number of permutations of length n, 
# followed by a list of all such permutations (in any order).


import itertools
permutation_list = []
permutation_list = list(itertools.permutations([1,2,3], 3))

print len(permutation_list)

for item in permutation_list:
	print string.replace(item, "," " ")





