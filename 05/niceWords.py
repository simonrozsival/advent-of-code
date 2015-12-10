forbidden = ("ab", "cd", "pq", "xy")
vowels = ("a", "e", "i", "o", "u")

def contains(n, letters, word):
	found = 0
	for letter in word:
		if letter in letters:
			found += 1
			if found >= n:
				return True
	return False
	
def doesNotContain(forbidden, word):
	for dangerous in forbidden:
		if dangerous in word:
			return False
	return True

def hasNLettersInARow(n, word):
	lastLetter = None
	row = 1
	for letter in word:
		if letter == lastLetter:
			row += 1
			if row >= n:
				return True
		else:
			row = 1
			lastLetter = letter
	return False

def isNice(word):
	return contains(3, vowels, word) and doesNotContain(forbidden, word) and hasNLettersInARow(2, word)

niceWords = 0
with open("in.txt") as file:
	for line in file:
		if isNice(line):
			niceWords += 1

print(niceWords)