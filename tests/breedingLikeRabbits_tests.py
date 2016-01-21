from nose.tools import *
from codingChallenge import breedingLikeRabbits

# Test cases
# ==========
# 
# Inputs:
#     (string) str_S = "7"
# Output:
#     (string) "4"
# 
# Inputs:
#     (string) str_S = "100"
# Output:
#     (string) "None"

input1 = "7"
output1 = "4"

input2 = "100"
output2 = "None"

input3 = "10000"
output3 = "2973"

input4 = "17826"
output4 = "4991"

input5 = "17480"
output5 = "None"


def test_answer():
	result = breedingLikeRabbits.answer(input1)
	assert_equal(result, output1)
	result = breedingLikeRabbits.answer(input2)
	assert_equal(result, output2)
	result = breedingLikeRabbits.answer(input3)
	assert_equal(result, output3)
	result = breedingLikeRabbits.answer(input4)
	assert_equal(result, output4)
	result = breedingLikeRabbits.answer(input5)
	assert_equal(result, output5)