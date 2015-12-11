from graph import Graph
import math

def findShortestPath(cities, distances):
	return findBestPath(math.inf, lambda a, b: a < b, cities, distances)

def findLongestPath(cities, distances):
	return findBestPath(-math.inf, lambda a, b: a > b, cities, distances)

def findBestPath(default, isBetter, cities, distances):
	# return findBestPathExhaustively(default, isBetter, cities, distances)
	return findBestPathSmart(default, isBetter, cities, distances)

# average time on the testIn.txt data on my computer: 0.5194985175132751 seconds
def findBestPathExhaustively(default, isBetter, cities, distances):
	if len(cities) == 0:
		raise Exception("Recursion was not ended.") # safety fallback

	if len(cities) == 1:
		return (0, cities) # end the recursion

	paths = findPaths(cities)
	bestPath = None
	bestPathLength = default
	for path in paths:
		length = meassureLength(path, distances)
		if isBetter(length, bestPathLength):
			bestPath = path
			bestPathLength = length
	
	return (bestPathLength, bestPath)
	
def findPaths(cities):
	if len(cities) == 1:
		return [cities]
	
	paths = []
	for i in range(0, len(cities)):
		city = cities.pop()
		furtherPaths = findPaths(cities)
		for path in furtherPaths:
			paths.append([city, *path])
		cities.insert(0, city)
	return paths

def meassureLength(path, distances):
	if len(path) == 1:
		return 0	
	return distances[path[0]][path[1]] + meassureLength(path[1:], distances)

# average time on the testIn.txt data on my computer: 0.12348659038543701
def findBestPathSmart(default, isBetter, cities, distances):
	return findBestContinuance(default, isBetter, None, cities, distances)


def findBestContinuance(default, isBetter, prevCity, cities, distances):
	if len(cities) == 1:
		return (distances[prevCity][cities[0]], cities)
	
	bestLength = default
	bestPath = None
	for i in range(0, len(cities)):		
		city = cities.pop()
		prefixLength = distances[prevCity][city] if prevCity is not None else 0
		(length, path) = findBestContinuance(default, isBetter, city, cities, distances)
		if isBetter(prefixLength + length, bestLength):
			bestLength = prefixLength + length
			bestPath = path 
		cities.insert(0, city)
	
	return (bestLength, bestPath)
