# Google coding challenge 01/14/16
# Parker Couch

def calculate_loop(numbers, start_of_loop):
	"""Polly wants to count some pirates"""
	i = start_of_loop
	length_of_loop = 0

	while True:
		# We'll only count as we are moving, we'll get back to the starting pirate
		length_of_loop += 1
		i = numbers[i]

		# We've seen that pirate before. They all have been counted now
		if i == start_of_loop:
			return length_of_loop


def answer(numbers):
	"""I'll tell you how many pirates are in a loop, yarrr!"""
	# Keeping track of pirates with 1's and 0's
	pointed = [0] * len(numbers)
	i = 0
	
	while True:

		# We've seen this pirate before, must be a loop
		if pointed[i] == 1:
			return calculate_loop(numbers, i)
		else:
			# Let's mark down that we've seen this pirate before
			pointed[i] = 1
			i = numbers[i]