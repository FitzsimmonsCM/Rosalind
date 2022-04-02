# A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which
# each integer is then provided with either a positive or negative sign.
# For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.

# Given: A positive integer n≤6.

# Return: The total number of signed permutations of length n, followed by a list of all such permutations
# (you may list the signed permutations in any order).

# Sample Input = 2
# Sample Output =
# 8
# -1 -2
# -1 2
# 1 -2
# 1 2
# -2 -1
# -2 1
# 2 -1
# 2 1

# Input the starting value
n = int(input ("Enter value for n: "))
a = 1

# Define an empty list for positives and negatives
positives = []

# For loop to interate through the list between a and n
for i in range (a, n+1):
		positives.append(i)
print (positives)

# permutations with itertools to get all number combinations
import itertools
ordered_positives = list(itertools.permutations(positives, 2))
print(ordered_positives)

# generate a list of all possible sign combinations


# list comprehension to get negatives
#negatives = [i *-1 for i in positives]
#print(negatives)

 # combine the negatives and positives into a single list element
#full_list = negatives + positives
#print(full_list)

# permutations with itertools and then print list length and elements

#print(len(ordered_pairs))
#print(ordered_pairs)

# make for loop for printing
# print item 1 + space + item 2 newline


# 2 parts
# make permutation of numbers
# make permutation of signs--generate all combinations of ± 1
# try it doing for Loops
