def test(name, real, expected, reportSuccess = True):
	if (expected == real):
		if reportSuccess == True:
			print("OK - {} is '{}'".format(name, real))
		return True
	else:
		print("FAIL - {}: {} should be {}".format(name, real, expected))
		return False