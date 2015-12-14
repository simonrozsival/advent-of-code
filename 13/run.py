import sys

ARGS_COUNT = 0
if len(sys.argv) < ARGS_COUNT:
	print("Missing arguments")
	sys.exit(1)

from task import parseLine, findOptimum, buildStructure, addAmbivalentPerson

##

result = 0
seating = []

with open("in.txt") as file:
	for line in file:
		seating = seating + [parseLine(line)]

# part 1	
structure = buildStructure(seating)	
(result, permutation) = findOptimum(structure)
print("The result of 'part 1' is '\033[1;33m{}\033[1;m' (seating is {})".format(result, permutation))

# part 2
structure = addAmbivalentPerson(buildStructure(seating))
(result, permutation) = findOptimum(structure)
print("The result of 'part 2' is '\033[1;33m{}\033[1;m' (seating is {})".format(result, permutation))


##

sys.exit(0)