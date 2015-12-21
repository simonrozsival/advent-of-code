import sys

from task import parseLine, findAunt, Aunt, findAuntPartTwo
##

aunts = []
with open("in.txt") as file:
	for line in file:
		aunt = parseLine(line)
		aunts.append(aunt)

sue = Aunt(-1)
sue.addProp("children", 3)
sue.addProp("cats", 7)
sue.addProp("samoyeds", 2)
sue.addProp("pomeranians", 3)
sue.addProp("akitas", 0)
sue.addProp("vizslas", 0)
sue.addProp("goldfish", 5)
sue.addProp("trees", 3)
sue.addProp("cars", 2)
sue.addProp("perfumes", 1)

# part 1

print("part 1:")

match = findAunt(aunts, sue)
if match != None:
	print("Found aunt Sue: {}".format(match.id))
else:
	print("No match found")

# part 2

print("part 2:")

match = findAuntPartTwo(aunts, sue)
if match != None:
	print("Found aunt Sue: {}".format(match.id))
else:
	print("No match found")
	
sys.exit(0)