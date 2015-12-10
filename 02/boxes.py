
def parseLine(line):
	return map(int, line.split("x"))
	
def getSurface(dim):
	dim.sort()
	return (3*dim[0]*dim[1] + 2*dim[0]*dim[2] + 2*dim[1]*dim[2])
	
def getVolume(dim):
	return dim[0]*dim[1]*dim[2]

def shortestPerimeter(dim):
	dim.sort()
	return 2*dim[0] + 2*dim[1]

def processBox(line):
	dim = parseLine(line)
	return getSurface(dim)
	
surface = 0
with open("in.txt", "r") as data:
	for line in data:
		 surface = surface + processBox(line)

print("The surface is {}".format(surface))


ribbonLength = 0;
with open("in.txt", "r") as data:
	for line in data:
		dim = parseLine(line)
		ribbonLength = ribbonLength + shortestPerimeter(dim) + getVolume(dim)
		
print("The ribbon must be {} feet long".format(ribbonLength))