import re

def initGrid(initialValue, width, height):
	return [[initialValue for j in range(0, width + 1)] for i in range(0, height + 1)]

def set(grid, setVal, (a, b), (c, d)):
	for i in range(a, c + 1):
		for j in range(b, d + 1):
			grid[i][j] = setVal(grid[i][j])
	return grid

def parseCoords(line):
	match = re.match(r'^(\d+),(\d+) through (\d+),(\d+)$', line, re.M|re.I)
	return (int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)))

def processCmd(grid, line):	
	if line.startswith("turn on"):
		line = line[len("turn on "):]
		fn = lambda x: x+1
	elif line.startswith("turn off"):
		line = line[len("turn off "):]
		fn = lambda x: max(0, x-1)
	elif line.startswith("toggle"):	
		line = line[len("toggle "):]
		fn = lambda x: x+2
	else:
		raise Exception("Unknown cmd '{}'".format(line))

	(a, b, c, d) = parseCoords(line)
	return set(grid, fn, (a, b), (c, d))
	
def countLights(grid):
	count = 0
	for row in grid:
		for col in row:
			count += col
	return count		

def processInstructions(fileName):
	grid = initGrid(0, 1000, 1000)
	with open(fileName) as file:
		for line in file:
			grid = processCmd(grid, line)
	return grid

grid = processInstructions("in.txt")
print(countLights(grid))