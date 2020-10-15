#Euler Project #7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10,001st prime number?

#import python's math library
import math

#Creating lists to store the prime numbers
primes = [2]
n = 3

#int don't care after decimal--just chops it
#math.ceil rounds up; still returns float number e.g. 1.0
#math.floor rounds down; still returns float number e.g. 1.0

#While loop for primes
while (len(primes) < 10001):
	is_prime = True
	for i in range(2, int(math.sqrt(n)) + 1): #if range is empty--you know it's prime
		if n % i == 0:
			is_prime = False
			break
		#else:
			#is_prime = True #Don't need to have else statement here b/c is_prime begins 'True'
		
	if is_prime == True:
		primes.append(n)	
	n = n+1	

#printing max value
print len(primes)
print max(primes)
print primes



