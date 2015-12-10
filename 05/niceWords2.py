from niceWords2Functions import isNice

niceWords = 0
with open("in.txt") as file:
	for line in file:
		if isNice(line.strip()):
			niceWords += 1

print(niceWords)