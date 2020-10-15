#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

#What I need to do:
	#compute 2^your power
	#slice the number into individual integers and store those values
	#sum the values in that list
	#print the sum


def powers_2 (power):
	two_raised = 2**power
	return two_raised

def convert_number_to_digits (number):
	power_list = []
	powerstrings = str(number)
	power_list = [int(x) for x in powerstrings]
	return power_list
	
def sum_digits (numbers):
	return sum(numbers)

powers2 = powers_2(1000)
print powers2
power_digits = convert_number_to_digits(powers2)
print power_digits
power_sum = sum_digits(power_digits)
print power_sum


