import sys

if len(sys.argv) < 1:
	print("Missing eggnog amount as an argument of the command")
	# sys.exit(1)

from task import parseReplacement, getAllOutcomes
##

# steps = int(sys.argv[1])

replacements = []
formula = False

with open("in.txt") as file:
	for line in file:
		if formula == False and line.strip() != "":
			replacements.append(parseReplacement(line.strip()))
		elif formula == None:
			formula = line
		else:
			formula = None # next round, read the formula
			
# part 1

print("part 1:")
outcomes = getAllOutcomes(formula, replacements)
print("The derivates count is: {}".format(len(outcomes)))


# part 2

print("part 2:")
	
sys.exit(0)