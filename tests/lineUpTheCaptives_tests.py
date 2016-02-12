from nose.tools import *
from codingChallenge import lineUpTheCaptives

# Test cases
# ==========
# 
# Inputs:
#     (int) x = 2
#     (int) y = 2
#     (int) n = 3
# Output:
#     (string) "2"
# 
# Inputs:
#     (int) x = 1
#     (int) y = 2
#     (int) n = 6
# Output:
#     (string) "24"


class TestLineUpTheCaptives(object):
	
	@classmethod
	def setup_class(self):
		"""PLACEHOLDER. Will run once then execute all tests"""
		self.x1, self.y1, self.n1 = 2, 2, 3
		self.output1 = "2"
		self.x2, self.y2, self.n2 = 1, 2, 6
		self.output2 = "24"

	@classmethod
	def teardown_class(self):
		"""PLACEHOLDER. Will run once after all tests have been executed"""
		pass

	def setup(self):
		"""Runs before every test"""
		pass

	def teardown(self):
		"""Runs after every test"""
		pass

	def test_answer(self):
		"""lineUpTheCaptives"""
		result = lineUpTheCaptives.answer(self.x1, self.y1, self.n1)
		assert_equal(result, self.output1)
		result = lineUpTheCaptives.answer(self.x2, self.y2, self.n2)
		assert_equal(result, self.output2)