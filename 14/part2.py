
def simulateSecondBySecond(time, reindeers):
	simulationTime = 0
	score = {}
	status = []
	
	for reindeer in reindeers:
		status += [initStatus(reindeer)]
	
	while simulationTime < time:
		for reindeer in status:
			reindeer = simulationStep(reindeer)
		leaders = findLeaders(status)
		for leader in leaders:
			leader["score"] += 1 
		simulationTime += 1

	return findWinners(status)

def initStatus((name, reindeer)):
	return {
		"name": name,
		"type": "flying",
		"remainingSeconds": reindeer[1],
		"distance": 0,
		"score": 0,
		"reindeer": reindeer	
	}

def checkStatus(status):
	status["remainingSeconds"] -= 1
	if status["remainingSeconds"] == 0:
		if status["type"] == "flying":
			status["type"] = "resting"
			status["remainingSeconds"] = status["reindeer"][2]
		else:
			status["type"] = "flying"
			status["remainingSeconds"] = status["reindeer"][1]

def simulationStep(status):
	if status["type"] == "flying":
		status["distance"] += status["reindeer"][0]
	return checkStatus(status) 

def findLeaders(reindeers):
	leaders = []
	maximum = 0
	for reindeer in reindeers:
		maximum = max(maximum, reindeer["distance"])
	for reindeer in reindeers:
		if reindeer["distance"] == maximum:
			leaders += [reindeer]
	return leaders


def findWinners(reindeers):
	winners = []
	maximum = 0
	for reindeer in reindeers:
		maximum = max(maximum, reindeer["score"])
	for reindeer in reindeers:
		if reindeer["score"] == maximum:
			winners += [reindeer]
	return winners