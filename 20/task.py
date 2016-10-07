def divisors(n):
	divs = []
	for i in range(1, n+1):
		if n % i == 0:
			divs.append(i)
	return divs
	
def getPointsCount(n):
	return sum(map(lambda x: 10*x, divisors(n)))