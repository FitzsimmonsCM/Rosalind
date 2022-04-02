# Rosalind INI4: Conditions and Loops
# Given: Two positive integers a and b (a < b < 10,000)
# Return: The sum of all odd integers from a through b, inclusive

# Sample Input: 100 200
# Sample Output: 7500

# Hint: You can use a % 2 == 1 to test if a is odd

# Ask the user for input values
a = int(input ("Enter value for a: "))
b = int(input ("Enter value for b: "))

# Define an empty list
Odds = []

# For loop to interate through the list between a and b+1
for i in range (a, b+1):
	if i % 2 == 1:
		Odds.append(i)

d = sum(Odds)
print (d)
