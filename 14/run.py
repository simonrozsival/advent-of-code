import sys

ARGS_COUNT = 1
if len(sys.argv) < ARGS_COUNT:
	print("Missing arguments")
	sys.exit(1)

from task import createReindeer, run
from part2 import simulateSecondBySecond
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

print("part 1:")
print("{} will run {} km in {} s".format(bestResult[0], bestResult[1], time))

# part 2
print("part 2:")
winners = simulateSecondBySecond(time, reindeers)
for winner in winners:
	print("{} won scoring race with the score of {}".format(winner["name"], winner["score"]))

sys.exit(0)