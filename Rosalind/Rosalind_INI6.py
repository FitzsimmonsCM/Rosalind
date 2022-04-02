# Rosalind Project #6: Dictionaries
# GIVEN: A string s of length at most 10,000 letters.
# RETURN: The number of occurrences of each word in s, where words are separated by spaces.
# Words are case-sensitive, and the lines in the output can be in any order.

text = input("Please enter a string of text: ")
passphrase = {}

for word in text.split(' '):
	if word in passphrase:
		passphrase[word] += 1
	else:
		passphrase[word] = 1

for key, value in passphrase.items():
    print key, value


# Pseudocode = This has two parts
	# encounter new word--add it to the dictionary
	# find old word again--update the count
