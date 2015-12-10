from func import unescaped_length, encode

totalEscapedLength = 0
totalUnescapedLength = 0 
totalMyEscapedLength = 0

with open("in.txt") as file:
	for line in file:
		line = line.strip()
		totalEscapedLength += len(line)
		totalUnescapedLength += unescaped_length(line)
		totalMyEscapedLength += len(encode(line))

print("Part one: {} - {} = {}".format(totalEscapedLength, totalUnescapedLength, totalEscapedLength - totalUnescapedLength))
print("Part two: {} - {} = {}".format(totalMyEscapedLength, totalEscapedLength, totalMyEscapedLength - totalEscapedLength))