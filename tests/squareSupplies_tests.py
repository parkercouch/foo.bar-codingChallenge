from nose.tools import *
from codingChallenge import squareSupplies


# Test cases
# ==========
# 
# Inputs:
#     (int) n = 24
# Output:
#     (int) 3
# 
# Inputs:
#     (int) n = 160
# Output:
#     (int) 2

input1 = 24
output1 = 3

input2 = 160
output2 = 2

input3 = 23
output3 = 5


def test_answer():
	result = squareSupplies.answer(input1)
	assert_equal(result, output1)
	result = squareSupplies.answer(input2)
	assert_equal(result, output2)
	result = squareSupplies.answer(input3)
	assert_equal(result, output3)