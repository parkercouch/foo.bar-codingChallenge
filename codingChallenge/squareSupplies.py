# Square supplies
# ===============
# 
# With the zombie cure injections ready to go, it's time to start treating our 
# zombified rabbit friends (known as zombits) at our makeshift zombit treatment 
# center. You need to run out really fast to buy some gauze pads but you only 
# have 30 seconds before you need to be back.
# 
# Luckily, the corner store has unlimited gauze pads in squares of all sizes. 
# Jackpot! The pricing is simple - a square gauze pad of size K x K costs 
# exactly K * K coins. For example, a gauze pad of size 3x3 costs 9 coins.
# 
# You're in a hurry and the cashier takes a long time to process each 
# transaction. You decide the fastest way to get what you need is to buy as few 
# gauze pads as possible, while spending all of your coins (you can always cut 
# up the gauze later if you need to). Given that you have n coins, what's the 
# fewest number of gauze pads you can buy?
# 
# Write a method answer(n), which returns the smallest number of square gauze 
# pads that can be bought with exactly n coins.
# 
# n will be an integer, satisfying 1 <= n <= 10000.
import math

def answer(n):

	list_of_squares = [x**2 for x in range(1, int(math.sqrt(n)) + 1)]
	gauze = 0

	while True:
		next_square = list_of_squares[-1]

		if next_square <= n :
			n = n - next_square
			if next_square > n:
				list_of_squares.pop()
			gauze += 1
			if n == 0:
				return gauze
		else:
			list_of_squares.pop()