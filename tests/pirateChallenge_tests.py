from nose.tools import *
from codingChallenge import pirateChallenge 

piratesA = [1, 0]
piratesB = [1, 2, 1]
piratesC = [2, 2, 4, 1, 3]

def test_answer():
	result = pirateChallenge.answer(piratesA)
	assert_equal(result, 2)
	result = pirateChallenge.answer(piratesB)
	assert_equal(result, 2)
	result = pirateChallenge.answer(piratesC)
	assert_equal(result, 4)