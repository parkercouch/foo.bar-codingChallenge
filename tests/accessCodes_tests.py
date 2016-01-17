from nose.tools import *
from codingChallenge import accessCodes

## Test Cases
## Inputs:
##     (string list) x = ["foo", "bar", "oof", "bar"]
## Output:
##     (int) 2
## 
## Inputs:
##     (string list) x = ["x", "y", "xy", "yy", "", "yx"]
## Output:
##     (int) 5

x = ["foo", "bar", "oof", "bar"]
y = ["x", "y", "xy", "yy", "", "yx"]

def test_answer():
	result = accessCodes.answer(x)
	assert_equal(result, 2)
	result = accessCodes.answer(y)
	assert_equal(result, 5)