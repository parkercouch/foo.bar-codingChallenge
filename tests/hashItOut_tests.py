from nose.tools import *
from codingChallenge import hashItOut

# Test cases
# ==========
# 
# Inputs:
#     (int list) digest = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
# Output:
#     (int list) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 
# Inputs:
#     (int list) digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
# Output:
#     (int list) [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

input1 = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
output1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

input2 = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
output2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]


def test_answer():
	result = hashItOut.answer(input1)
	assert_equal(result, output1)
	result = hashItOut.answer(input2)
	assert_equal(result, output2)