from nose.tools import *
from codingChallenge import spySnippets

# Test cases
# ==========
# 
# Inputs:
#     (string) document = "many google employees can program"
#     (string list) searchTerms = ["google", "program"]
# Output:
#     (string) "google employees can program"
# 
# Inputs:
#     (string) document = "a b c d a"
#     (string list) searchTerms = ["a", "c", "d"]
# Output:
#     (string) "c d a"

input_string1 = "many google employees can program"
input_search1 = ["google", "program"]
output_string1 = "google employees can program"

input_string2 = "a b c d a"
input_search2 = ["a", "c", "d"]
output_string2 = "c d a"

input_string3 = "a a x x y y a a a z a a a x y z a a a a z a x"
input_search3 = ["x", "y", "z"]
output_string3 = "x y z"

input_string4 = "a a x x y y a a a z a a a x a y z a a a a z a x"
input_search4 = ["x", "y", "z"]
output_string4 = "x a y z"


def test_answer():
	result = spySnippets.answer(input_string1, input_search1)
	assert_equal(result, output_string1)
	result = spySnippets.answer(input_string2, input_search2)
	assert_equal(result, output_string2)
	result = spySnippets.answer(input_string3, input_search3)
	assert_equal(result, output_string3)
	result = spySnippets.answer(input_string4, input_search4)
	assert_equal(result, output_string4)