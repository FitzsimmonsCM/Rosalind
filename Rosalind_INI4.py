#Rosalind INI4: Conditions and Loops
#Given: Two positive integers a and b (a < b < 10,000)
#Return: The sum of all odd integers from a through b, inclusive

#Sample Input: 100 200
#Sample Output: 7500

#Hint: You can use a % 2 == 1 to test if a is odd

a = 4376
b = 9133
c = b + 1
Odds = []

for i in range (a, c):
	if i % 2 == 1:
		Odds.append(i)

d = sum(Odds)
print d

