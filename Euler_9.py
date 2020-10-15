#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math
def pythagorean_triple(a,b):
	for a in range (3, 500):
		for b in range (a+1, 500):
			c = ((a**2) + (b**2))**0.5
			pythagorean_sum = a + b + c
			if pythagorean_sum == 1000:
				print(a, b, c)
				pythagorean_multiple = a*b*c			
	return pythagorean_multiple
	


find_triple = pythagorean_triple(3,4)
print find_triple

#I stuck with 500 (rather than 1000) because no 