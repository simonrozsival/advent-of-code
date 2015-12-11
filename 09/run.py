import re
from findBestPath import findShortestPath, findLongestPath
from graph import Graph

graph = Graph()
with open("in.txt") as file:
	for line in file:
		match = re.match(r'^(.*) to (.*) = (.*)$', line, re.I|re.M)
		graph.addDistance(match.group(1), match.group(2), int(match.group(3)))


def printPath(path):
	output = path[0] 
	for city in path[1:]:
		output += " -> " + city
	return output

# Part 1	
(length, path) = (findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix()))
print("the shortest path is {} ==> {} km".format(printPath(path), length))

# Part 2
(length, path) = (findLongestPath(graph.getCitiesList(), graph.getDistancesMatrix()))
print("the longest path is {} ==> {} km".format(printPath(path), length))