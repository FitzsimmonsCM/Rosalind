# Determine the sum of the Even Fibonacci numbers between 1 and 4,000,000

# Determine the group of numbers that are Fibonacci numbers
a = 0
b = 1
Fib_n=[a, b]
while b < 4000000:
	a, b = b, a+b
	Fib_n.append(b)


# Determine if the number is even
Fib_2 = []
for i in Fib_n:
	if i % 2 == 0:
		Fib_2.append(i)


# Determine the sum of the even numbers
c = sum(Fib_2)
print(c)

# Each function is an *independent* piece of code.
# You can think of a function like f(x) = mx + b
# The name of the function is f, the input is x, and the "return value" is mx + b
# You can ignore all the variables that aren't in the function.

# This is just a function definition; we don't do anything
# until we call the function.

# Three parts to each function:
# 1. Inputs (aka arguments): upper_limit 
# 2. all the code
# 3. Outputs (aka return values): Fib_n
def find_fibonacci_numbers(upper_limit):
	"""
	Return a list of all the Fibonacci number below the given upper limit.
	"""
	a = 0
	b = 1
	Fib_n=[a, b]
	
	while b < upper_limit:
		a, b = b, a+b
		Fib_n.append(b)
		
	return Fib_n

def discard_odd_numbers(numbers):
	evens_only = []
	
	for i in numbers:
		if i % 2 == 0:
			evens_only.append(i)
			
	return evens_only

def calculate_sum(numbers):
	return sum(numbers)

# Doesn't matter that Fib_n and fib_numbers are different variable names.
fib_numbers = find_fibonacci_numbers(4000000)
# fib_numbers is evaluated for our input 
#once there is a return value, list, etc, fib_numbers gets that final value, list, etc
#e.g. fib_numbers = Fib_n
even_fib_numbers = discard_odd_numbers(fib_numbers)
even_fib_sum = calculate_sum(even_fib_numbers)

print(even_fib_sum)

#Why use functions? Who the F cares? 
#1: Code with functions--usually just skip reading code of the function. 
#only need to read where the function is called (assuming no bugs in fxn)
#Want each fxn to have clear reason for existing. Good names = important!

#2: Each fxn is it's own domain. Variables in f(a) don't effect g(a), etc. 
#could repeat variables if you wanted to do so

#3: Can reuse fxn. 
#Can reuse between scripts
#Can also reuse within scripts

	