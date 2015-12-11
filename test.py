def test(name, real, expected):
	if (expected == real):
		print("OK - {} is '{}'".format(name, real))
	else:
		print("FAIL - {}: {} should be {}".format(name, real, expected))