import sys

if len(sys.argv) < 2:
	print("Missing eggnog amount as an argument of the command")
	sys.exit(1)

from task import getPointsCount
##

presentsCount = int(sys.argv[1])
			
# part 1

print("part 1:")

minPresentsCount = presentsCount
i = 73920
while True:
	if getPointsCount(i) >= minPresentsCount:
		least = i
		break
	elif i % 10000 == 0:
		print("reached {} and still nothing was found...".format(i))
	i += 1

print("The least number with {} presents delivered is: {}".format(getPointsCount(i), i))

# part 2

print("part 2:")
	
sys.exit(0)