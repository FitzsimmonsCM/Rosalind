#Euler_6

#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ...10)^2 = 55^2 = 3025
#The difference between the two is, 3025-385 = 2640
#Find the difference between the sum of squares and the square of sums for the first 100 numbers


#Asking the user for input number
#nString = input("Enter a number: ")
#n = int(nString)
#a = n+1


#Kale's command line argument method
#sys is built into python
#sys gives info about version of python, last error encountered, etc
import sys
a = int(sys.argv[1])
print sys.argv

#Finding the sum of the squares
ss1 =[]
for i in range(1, a+1):
	ss1.append(i**2)
ss1_sum = sum(ss1)	
print(ss1_sum)	
	

#Finding the square of the sum		
ss2=[]
for i in range (1, a+1):
	ss2.append(i)
ss2_sq = ((sum(ss2))**2)
print(ss2_sq)

#Finding the difference
ss_diff = ss2_sq-ss1_sum
print(ss_diff)
		
	
		
