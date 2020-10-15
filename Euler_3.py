#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

#Pseudocode
#Generate list of primes
#Divide starting number by list of primes
#If modulo has remainder, go to next prime
#If no remainder, store the prime number on the list
#Use the new number to repeat the process
#Go until you have no more numbers

import math


def generate_primes_list(n):
	prime_list= [2]
	#While loop for primes
	while max(prime_list) < int(math.sqrt(n)):
		is_prime = True
		for i in range(2, int(math.sqrt(n)) + 1): #if range is empty--you know it's prime
			if n % i == 0:
				is_prime = False
				break
			#else:
			#is_prime = True #Don't need to have else statement here b/c is_prime begins 'True'
		
		if is_prime == True:
			prime_list.append(n)	
		n = n+1	
	return prime_list

	
def prime_factorization(n):
	for p in prime_list (n):
		while n%p ==0:
			yield p
			n=n//p
			if n==1: return

a = generate_primes_list(600851475143)
b = prime_factorization(600851475143)
print b

			
