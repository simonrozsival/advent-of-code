from func import unescaped_length

totalEscapedLength = 0
totalUnescapedLength = 0 

with open("in.txt") as file:
	for line in file:
		line = line.strip()
		totalEscapedLength += len(line)
		totalUnescapedLength += unescaped_length(line)

print("{} - {} = {}".format(totalEscapedLength, totalUnescapedLength, totalEscapedLength - totalUnescapedLength))