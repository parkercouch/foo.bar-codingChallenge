from nose.tools import *
from codingChallenge import codingChallenge 

piratesA = [1, 0]
piratesB = [1, 2, 1]
piratesC = [2, 2, 4, 1, 3]
import random
my_randoms = random.sample(xrange(5000), 5000)

def test_answer():
	result = codingChallenge.answer(piratesA)
	assert_equal(result, 2)
	result = codingChallenge.answer(piratesB)
	assert_equal(result, 2)
	result = codingChallenge.answer(piratesC)
	assert_equal(result, 4)
	