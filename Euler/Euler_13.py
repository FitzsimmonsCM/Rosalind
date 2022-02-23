#Euler #13
#Given this list of one-hundred 50-digit numbers, find their sum. Report the first 10 digits of this sum.

#importing the built-in modules we need and defining lists
import math
import csv

Euler_strings = []

#reading in the csv file with all of the large numbers
#r mean 'read'; 'w' means 'write'
#rb means read in binary mode
#rU means that it looks for any of the conventional newline endings: windows, mac, or linux
with open('Euler_13.csv', 'rU') as f:
    Eureader = csv.reader(f) #the reader function keeps a row together
    for row in Eureader:
    	x = row[0]
    	Euler_strings.append(x) 
    	#when you loop through the rows, it creates a list of lists--keeping everything together

#converting strings to ints
#from pprint import pprint 
#pprint knows what big data sets are, and makes them pretty in terminal
pprint (Euler_strings)

#def int_plus_one(x):
	#return x + 1
Euler_numbers = map(int_plus_one, Euler_strings)

Euler_numbers2 = [int(x)**2 for x in Euler_strings if x % 2 == 0]
#this syntax is nice when you don't already have a built-in function for what you want
#can add if statement to end of syntax
#good way to filter things out of your list
#list comprehensions is name of this method


#summing and printing the list
a = sum(Euler_numbers)
print (a)

#Kale's bonus homework challenge
#can I get the program to only print the first 10 digits?