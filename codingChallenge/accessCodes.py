# Access codes
# ============
# 
# You've discovered the evil laboratory of Dr. Boolean, and you've found that 
# the vile doctor is transforming your fellow rabbit kin into terrifying 
# rabbit-zombies! Naturally, you're less-than-happy about this turn of events.
# 
# Of course where there's a will, there's a way. Your top-notch assistant, Beta 
# Rabbit, managed to sneak in and steal some access codes for Dr. Boolean's lab 
# in the hopes that the two of you could then return and rescue some of the 
# undead rabbits. Unfortunately, once an access code is used it cannot be used 
# again. Worse still, if an access code is used, then that code backwards won't 
# work either! Who wrote this security system?
# 
# Your job is to compare a list of the access codes and find the number of 
# distinct codes, where two codes are considered to be "identical" (not 
# distinct) if they're exactly the same, or the same but reversed. The access 
# codes only contain the letters a-z, are all lowercase, and have at most 10 
# characters. Each set of access codes provided will have at most 5000 codes in 
# them.
# 
# For example, the access code "abc" is identical to "cba" as well as "abc." The 
# code "cba" is identical to "abc" as well as "cba." The list 
# ["abc", "cba", "bac"] has 2 distinct access codes in it.
# 
# Write a function answer(x) which takes a list of access code strings, x, and 
# returns the number of distinct access code strings using this definition of 
# identical.

def answer(x):
	
	already_used_codes = []
	number_of_codes = 0

	for code in x:
		if code in already_used_codes:
			pass
		else:
			number_of_codes += 1
			#Add code and reversed code to list of used codes
			already_used_codes.append(code)
			already_used_codes.append(code[::-1])

	return number_of_codes