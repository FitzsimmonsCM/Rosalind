#Rosalind INI5: Working with Files
#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. 
#Assume 1-based numbering of lines.


#This function reads in all the lines and prints out all of the lines
#def read_all_lines (txt):
#	with open (txt, 'rU') as f:
#		all_lines = []
#		for line in f:
#			all_lines.append(line)
#	return all_lines

#This function reads all of the lines, but only adds the even lines to the list
def find_even_lines (txt):
	with open (txt, 'rU') as fp:
		even_lines = []
		for cnt, line in enumerate(fp):
			if cnt % 2 == 1:
				even_lines.append(line)
	return even_lines

	
def write_even_lines (even_lines):
	f = open ("INI5_data.txt" , 'w')
	f.write ("\n".join(map(lambda x: str(x), even_lines)))
	f.close()
	return
  	


#ReadIn = read_all_lines('BraveRobin.txt')
#print ReadIn
ReadSort = find_even_lines ('rosalind_ini5.txt')
#print ReadSort
ReadOut = write_even_lines(ReadSort)
print ReadOut


#The command f.readlines() returns a list containing every line in the file. 
#If you need to obtain a particular line, you can use a list item index, e.g., 
#f.readlines()[2] returns the third line of the 
#file object f (don't forget that Python utilizes 0-based numbering!)