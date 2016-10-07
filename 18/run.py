import sys

if len(sys.argv) < 2:
	print("Missing eggnog amount as an argument of the command")
	sys.exit(1)

from task import readGridLine, animate, lightsOnCount, animationStepWithCornersOn
##

steps = int(sys.argv[1])

grid = []
with open("in.txt") as file:
	for line in file:
		grid.append(readGridLine(line))

# part 1

print("part 1:")
grid1 = animate(grid, steps)
print("Lights on after {} animation steps: {}".format(steps, lightsOnCount(grid1)))


# part 2

print("part 2:")
grid2 = animate(grid, steps, animationStepWithCornersOn)
print("Lights on after {} animation steps: {}".format(steps, lightsOnCount(grid2)))
	
sys.exit(0)