# Breeding like rabbits
# =====================
# 
# As usual, the zombie rabbits (zombits) are breeding... like rabbits! But 
# instead of following the Fibonacci sequence like all good rabbits do, the 
# zombit population changes according to this bizarre formula, where R(n) is 
# the number of zombits at time n:
# 
# R(0) = 1
# R(1) = 1
# R(2) = 2
# R(2n) = R(n) + R(n + 1) + n (for n > 1)
# R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)
# 
# (At time 2, we realized the difficulty of a breeding program with only one 
# zombit and so added an additional zombit.)
# 
# Being bored with the day-to-day duties of a henchman, a bunch of Professor 
# Boolean's minions passed the time by playing a guessing game: when will the 
# zombit population be equal to a certain amount? Then, some clever minion 
# objected that this was too easy, and proposed a slightly different game: 
# when is the last time that the zombit population will be equal to a certain 
# amount? And thus, much fun was had, and much merry was made.
# 
# (Not in this story: Professor Boolean later downsizes his operation, and you 
# can guess what happens to these minions.)
# 
# Write a function answer(str_S) which, given the base-10 string representation 
# of an integer S, returns the largest n such that R(n) = S. Return the answer 
# as a string in base-10 representation. If there is no such n, return "None". 
# S will be a positive integer no greater than 10^25.

def memoize(f):
	"""Automatically memoizes previous values for our recursive function"""
	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

@memoize
def r(x):
	"""Recursive function which figures out how many zombits"""
	if x == 0 or x == 1:
		return 1
	elif x == 2:
		return 2
	else:
		if x % 2 == 0:
			n = x/2
			return r(n) + r(n+1) + n
		else:
			n = (x-1) / 2
			return r(n-1) + r(n) + 1


def search(start, end, target, parity):
    """Binary search by even or odd indices depending on parity"""
    
    if end <= start:
        # Target is not in the list
        return None

    # set midpoint with a bitshift
    mid = start + ((end - start) >> 1)

    # Use parity to add 1 to keep the indexes even/odd
    if parity != (mid & 1):
    	mid += 1

    # Get the value at the midpoint
    S = r(mid)

    if S == target:
    	# Found the target, so return the index it is at
        return mid

    if S > target:
        # Must be in the first half so end is set to the current midpoint
        end = mid - 1
    else:
        # Must be in the second half so start is set to the current midpoint
        start = mid + 1

    # Search the narrowed field
    return search(start, end, target, parity)


def answer(str_S):
	"""Will return the last time str_S occurs in the list made by r(x)"""
	value = int(str_S)

	#Search odd first, then even if needed
	odd = search(0, value, value, 1)
	if odd != None:
		return '{}'.format(odd)
	else:
		# Check even indices
		return '{}'.format(search(0, value, value, 0))