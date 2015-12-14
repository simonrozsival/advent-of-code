import sys

ARGS_COUNT = 1
if len(sys.argv) < ARGS_COUNT:
	print("Missing arguments")
	sys.exit(1)

from task import createReindeer, run

##

time = int(sys.argv[1])

reindeers = []
with open("in.txt") as file:
	for line in file:
		reindeer = createReindeer(line)
		reindeers += [(reindeer[0], reindeer[1:])]

# part 1
bestResult = None
for reindeer in reindeers:
	name = reindeer[0]
	props = reindeer[1]
	distance = run(time, props)
	if bestResult == None or distance > bestResult[1]:
		bestResult = (name, distance)

print("{} will run {} km in {} s".format(bestResult[0], bestResult[1], time))

##

sys.exit(0)