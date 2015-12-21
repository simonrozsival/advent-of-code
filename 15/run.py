import sys

if len(sys.argv) < 2:
	print("Missing arguments")
	sys.exit(1)

from task import parseLine, getMaxScore, getTotalCaloriesCount
##

teaspoons = int(sys.argv[1])

ingredients = []
with open("in.txt") as file:
	for line in file:
		ingredients.append(parseLine(line))

# part 1

print("part 1:")
ingredientsProps = map(lambda (_, props): props, ingredients)
print("Max score is {}".format(getMaxScore(teaspoons, ingredientsProps)))

# part 2

if len(sys.argv) < 3:
	print("Missing arguments for part 2")
	sys.exit(1)

calories = int(sys.argv[2])
print("part 2:")

def cookiesFilter(ratios, ingredients):
	return getTotalCaloriesCount(ratios, ingredients) == calories

print("Max score with exactely {} calories is {}".format(calories, getMaxScore(teaspoons, ingredientsProps, cookiesFilter)))

sys.exit(0)