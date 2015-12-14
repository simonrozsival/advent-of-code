import re

def createReindeer(line):
	matches = re.match(r'^(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$', line, re.M|re.I)
	return (matches.group(1), int(matches.group(2)), int(matches.group(3)), int(matches.group(4)))

def move(maxTime, (distance, time), (speed, maxTravelTime, minRestingTime)):
	timeToTravel = min(maxTime - time, maxTravelTime)
	return (distance + timeToTravel*speed, time + timeToTravel)

def rest(maxTime, (distance, time), (speed, maxTravelTime, minRestingTime)):
	maxRestingTime = min(maxTime - time, minRestingTime)
	return (distance, time + maxRestingTime)

def run(time, reindeer):
	travel = (0, 0)
	step = 0
	while travel[1] < time:
		cmd = move if step % 2 == 0 else rest
		step += 1
		travel = cmd(time, travel, reindeer)
	return travel[0]