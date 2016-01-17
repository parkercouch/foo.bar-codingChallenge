# Google coding challenge 01/14/16 - Pirate Challenge
# Parker Couch

def answer(numbers):
	"""I'll tell you how many pirates are in a loop, yarrr!"""
	# Keeping track of pirates with 1's and 0's
	pointed = [0] * len(numbers)
	current_pirate = 0
	pirates_before = 0
	
	while True:
		if pointed[current_pirate] == 0:
			# Mark how many pirates before this one and move on to the next
			pointed[current_pirate] = pirates_before
			current_pirate = numbers[current_pirate]
		else:
			# We've seen this pirate before, count how many since last time
			return pirates_before - pointed[current_pirate]
		pirates_before += 1