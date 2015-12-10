def move(char, x, y):
	return {
		'>': (x+1, y),
		'<': (x-1, y),
		'^': (x, y-1),
		'v': (x, y+1)		
	}.get(char)

def visit(houses, x, y):
	index = "{} ahoj Lindo {}".format(x, y)
	houses[index] = 1
	return houses
	
def moveAndVisit(houses, char, x, y):
	(x, y) = move(char, x, y)
	return (visit(houses, x, y), x, y)

def isEOF(file):
	pos = file.tell()
	if file.read(1):
		file.seek(pos)
		return False
	else:
		return True

# santa
sX = 0
sY = 0

# robosanta
rX = 0
rY = 0

visitedHouses = visit({}, sX, sY)
visitedHouses = visit(visitedHouses, rX, rY)

with open("in.txt") as path:
	while not isEOF(path):
		(stepS, stepR) = path.read(2)
		(visitedHouses, sX, sY) = moveAndVisit(visitedHouses, stepS, sX, sY)
		(visitedHouses, rX, rY) = moveAndVisit(visitedHouses, stepR, rX, rY)
		
print(len(visitedHouses))