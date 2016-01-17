from nose.tools import *
from codingChallenge import maximumEquality 

x = [1, 4, 1]
y = [1, 2]
z = [2, 2, 4, 1, 3]
a = [20, 60, 50, 50, 7]

def test_answer():
	result = maximumEquality.answer(x)
	assert_equal(result, 3)
	result = maximumEquality.answer(y)
	assert_equal(result, 1)
	result = maximumEquality.answer(z)
	assert_equal(result, 4)
	result = maximumEquality.answer(a)
	assert_equal(result, 4)