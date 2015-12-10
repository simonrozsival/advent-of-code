def containsPairTwice(word):
	for i in range(0, len(word)):
		pair = word[i:i+2]
		
		# avoid the "last letter only"
		if len(pair) != 2:
			continue
		
		rest = "{}_{}".format(word[0:i], word[i+2:len(word)])
		if pair in rest:
			return True
	return False
	
def eye(word):
	for i in range(0, len(word) - 2):
		a = word[i]
		b = word[i + 2]
		if a == b:
			return True
	return False

def isNice(word):
	return containsPairTwice(word) and eye(word)