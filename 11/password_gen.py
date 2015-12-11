def findNewPassword(oldPwd):
	newPwd = iterate(oldPwd)
	while isValid(newPwd) == False:
		newPwd = iterate(newPwd)
	return newPwd

def iterate(pwd):
	if pwd == "zzzzzzzz":
		return "aaaaaaaa" # hande the oveflowing edge case
	
	newPwd = ""
	hasCarry = True
	i = len(pwd) - 1
	while hasCarry and i >= 0:
		(char, hasCarry) = iterateChar(pwd[i])
		newPwd = char + newPwd
		i -= 1
	if hasCarry == True:
		newPwd = "a" + newPwd # the end was reached, but there is still a carry
	else:		
		newPwd = pwd[:i+1] + newPwd # end was not reached or there is no carry
	return newPwd[len(newPwd)-8:] # make sure the maximum length of a password is 8
	
def iterateChar(char):
	if char == "z":
		return ("a", True)
	else:
		return (chr(ord(char) + 1), False)

def isValid(pwd):
	return hasTheRightLength(pwd) and \
					doesNotContainForbiddenLetters(pwd) and \
					containsStraight(pwd) and \
					containsTwoNonOverlapingPairs(pwd)
	
PWD_LEN = 8
def hasTheRightLength(pwd):
	return len(pwd) == PWD_LEN

FORBIDDEN_LETTERS = ('o', 'i', 'l')
def doesNotContainForbiddenLetters(pwd):	
	for c in pwd:
		if c in FORBIDDEN_LETTERS:
			return False
	return True
	
FORBIDDEN_STRAIGHT_LENGTH = 3
def containsStraight(pwd):
	lastLetter = ' '
	straightCounter = 1
	
	for c in pwd:
		if ord(c) - ord(lastLetter) == 1:
			straightCounter += 1
			if straightCounter == FORBIDDEN_STRAIGHT_LENGTH:
				return True
		else:
			straightCounter = 1
		lastLetter = c
				
	return False

MIN_PAIRS_COUNT = 2
def containsTwoNonOverlapingPairs(pwd):
	lastLetter = None
	pairsCount = 0
	for i in range(0, len(pwd)):
		if lastLetter == pwd[i]:
			pairsCount += 1
			lastLetter = None
		else:
			lastLetter = pwd[i] 
	return pairsCount >= MIN_PAIRS_COUNT