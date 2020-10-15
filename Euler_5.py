# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

import math
smallest = []
n = 100
while (len(smallest) < 1):
	is_divisible = True
	for i in range (20, 6, -1):
		if n % i > 0:
			is_divisible = False
			break
	if is_divisible == True:
		smallest.append(n)
	n = n+20

print smallest

#import math
#def evenly_divisible (starting_num):
#	smallest_number = []
#	while (len(smallest) < 1):
#		is_divisible = True
#		for i in range (1, 11):
#			if n % i > 0:
#				is_divisible = False
#				break
#		if is_divisible == True:
#			smallest.append(n)
#		n = n+1	
#	return smallest_number


#find_divisible = evenly_divisible(100)
#print smallest_number



