# Using the range function to find multiples of 3 and 5 less than 1000, and finding the summation of those values

# range(start, stop, step)
list_fives = list(range(0, 1000, 5))
list_threes = list(range(0, 1000, 3))

# combining lists
list_threefifths = list(set(list_fives)|set(list_threes))


#summation of lists
a = sum(list_threefifths)
print(a)





#####
# Kale's "equiv of master" solution
n = 1000
set_fives = set(range(0, n, 5))
set_threes = set(range(0, n, 3))

b = sum(set_fives | set_threes)
print(b)



#function--mini script
#only variable fxn should use are expressly their inputs
#inputs go in ()

def make_lists():
	list_fives = list(range(0, 1000, 5))
	list_threes = list(range(0, 1000, 3))
	return list_fives, list_threes

def combine_lists(lists):
	return list(set(lists[0])|set(list[1]))
	
def sum_combination(combo):
	return sum(combo)
	
lists = make_lists()
combo = combine_lists(lists)
result = sum_combination(combo)

print(result)
