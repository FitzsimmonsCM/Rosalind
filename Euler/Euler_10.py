#Euler #10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#import python's math library
import math

#Creating lists to store the prime numbers
primes = [2]
n = 3

#int don't care after decimal--just chops it
#math.ceil rounds up; still returns float number e.g. 1.0
#math.floor rounds down; still returns float number e.g. 1.0


for n in range (3, 2000000):
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

#Summation of the list	
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

#printing values
print len(primes)
print max(primes)
print listsum(primes)