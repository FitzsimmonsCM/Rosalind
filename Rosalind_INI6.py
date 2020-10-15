#Rosalind Project #6: Dictionaries
#GIVEN: A string s of length at most 10,000 letters.
#RETURN: The number of occurrences of each word in s, where words are separated by spaces. 
#Words are case-sensitive, and the lines in the output can be in any order.

phrasein = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
passphrase = {}

for word in phrasein.split(' '):
	if word in passphrase:
		passphrase[word] += 1
	else:
		passphrase[word] = 1
	
for key, value in passphrase.items():
    print key, value





#import collections
#print collections.Counter(passphrase)

#for key, value in passphrase.items():
#  print key
#  print value



#Two parts
	#encounter new word--add to dictionary
	#find old word again--update count






    