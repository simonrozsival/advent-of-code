import sys

if len(sys.argv) < 2:
	print("Missing eggnog amount as an argument of the command")
	sys.exit(1)

from task import getCombinationsCount, getMinimalCombinationsCount
##

eggnog = int(sys.argv[1])

bottles = []
with open("in.txt") as file:
	for line in file:
		bottles.append(int(line))

# part 1

print("part 1:")
print("Combinations count: {}".format(getCombinationsCount(eggnog, bottles)))


# part 2

print("part 2:")
print("Combinations count with minimal bottles usage: {}".format(getMinimalCombinationsCount(eggnog, bottles)))
	
sys.exit(0)