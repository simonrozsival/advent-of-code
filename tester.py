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
	def succcessReport(self):
		return (self.GREEN, "OK", "all {} tests passed".format(self.passedTests))
	def failReport(self):
		return (self.RED, "TESTING FAILED", "{} of {} tests failed".format(self.failedTests, self.passedTests + self.failedTests))
	def report(self):
		(color, status, reportMsg) = self.succcessReport() if self.failedTests == 0 else self.failReport()
		print("{}{}\033[1;m: {}".format(color, status, reportMsg))
		return self.failedTests == 0