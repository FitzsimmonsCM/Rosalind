#Rosalind INI3: Strings and Lists

#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and
#c through d (with space in between), inclusively.
#In other words, we should include elements s[b] and s[d] in our slice.


# Sample Input: HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102

# Sample Output 1:
# Humpty Dumpty

# Sample Input 2:
# bkWm0rEKPicadgMaguXhBFguttataNZHV6GJEYST3Q7CrOdMzudCYrhzxJARJIdj7PqbBfY9d3Tj5t7lAmfukT7F5Sl66tSvySCR4X4Jmak3b0oD2JuiBCgwAHwiXphI1UiGt7vSv3bWxNbDl8SFaQ1IBQApIRJs1v.
# 8 11 22 28

# Sample Output 2:
# Pica guttata


text = input("Please enter a string of text: ")
a, b, c, d = [int(x) for x in input("Enter four space-separated integers: ").split( )]

cut3 =text[a:b+1] + ' ' + text[c:d+1]
print(cut3)
