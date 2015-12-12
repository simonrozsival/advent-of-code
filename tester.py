from test import test

class Tester:
	GREEN = "\033[1;32m"
	RED = "\033[1;38m"
	def __init__(self):
		self.passedTests = 0
		self.failedTests = 0
	def test(self, desc, real, expected):
		if test(desc, real, expected, False):
			self.passedTests += 1
		else:
			self.failedTests += 1
	def report(self):		
		print("-----")
		(color, resultMsg) = (self.GREEN, "OK") if self.failedTests == 0 else (self.RED, "TESTING FAILED")
		print("{}{}\033[1;m: {} of {} tests failed".format(color, resultMsg, self.failedTests, self.passedTests + self.failedTests))
		return self.failedTests == 0