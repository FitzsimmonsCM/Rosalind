#Rosalind INI3: Strings and Lists

#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and 
#c through d (with space in between), inclusively. 
#In other words, we should include elements s[b] and s[d] in our slice.


#Sample Input: HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
#22 27 97 102

#Sample Output: 
#Humpty Dumpty

weirdtext = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
cutup = weirdtext[22:28] + ' ' + weirdtext[97:103]

print cutup

weirdtext2 = 'QkO5fVuVsGlE9x1a05v5efAR4uTV90AhA52js3UWtTyBombus4PcvZkY6h6PdZ49SX0psMbzxQlqNGMyXJWlPzYfBcherrugCPiMsb9PnWIKDsGtcEEvAgylPpJVhkrOxbU4m1EsSXFAx3A5PshnvRFAVkfI3zq7tCAG0Kuy3EuWPQqftI4yac6sGuALd0I8'
cutup2 = weirdtext2[43:49] + ' ' + weirdtext2[89:96]

print cutup2

