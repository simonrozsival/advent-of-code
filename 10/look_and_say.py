
def lookAndSay(puzzle):
	result = ""
	prevNumber = puzzle[0]
	inARow = 1
	for number in puzzle[1:]:
		if (number == prevNumber):
			inARow += 1
		else:
			result += "{}{}".format(inARow, prevNumber)
			prevNumber = number
			inARow = 1
	# flush the last digit
	result += "{}{}".format(inARow, prevNumber)
	
	return result