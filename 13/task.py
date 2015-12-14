import re

def parseLine(line):
	matches = re.match(r'(.*) would (.*) (\d+) happiness units by sitting next to (.*).', line, re.M|re.I)
	sgn = 1 if matches.group(2) == "gain" else -1
	return (matches.group(1), matches.group(4), sgn * int(matches.group(3)))

def buildStructure(happiness):
	people = {}
	for (name, other, gain) in happiness:
		people[name] = {}  
	for (name, other, gain) in happiness:
		people[name][other] = gain  
	return people

def findOptimum(structure):
	optimum = (0, None)
	people = guestlist(structure)
	permutations = generatePermutations(people)
	for permuation in permutations:
		value = countHappiness(permuation, structure)
		if value > optimum[0]:
			optimum = (value, permuation)
	return optimum

def guestlist(structure):
	guests = []
	for guest in structure:
		if guest not in guests:
			guests = guests + [guest]
	
	return guests
	
def addAmbivalentPerson(structure, name = "me"):
	guests = guestlist(structure)	
	while name in guests:
		name += "_x_"
	structure[name] = {}
	for guest in guests:
		structure[name][guest] = 0
		structure[guest][name] = 0
	return structure
	

def generatePermutations(people, prefix = []):
	if len(people) == 0:
		return [prefix]

	permutations = []
	for i in range(0, len(people)):
		person = people[i]
		subperms = generatePermutations(people[0:i] + people[i+1:], prefix + [person])
		for sub in subperms:
			permutations.append(sub)
	return permutations
	
def countHappiness(seating, structure):
	happiness = 0
	for i in range(0, len(seating)):
		prevIndex = (i + 1) % len(seating)
		nextIndex = (i - 1 + len(seating)) % len(seating)
		happiness += structure[seating[i]][seating[prevIndex]]
		happiness += structure[seating[i]][seating[nextIndex]]
	return happiness