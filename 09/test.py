import sys
import re
import time
sys.path.insert(0, '../')

from graph import Graph
from findBestPath import findShortestPath, findLongestPath
from test import test

graph = Graph()
graph.addDistance("a", "b", 5)

test("cities list", graph.getCitiesList(), ["a", "b"])
test("distances matrix", graph.getDistancesMatrix(), { "a": { "b": 5, "a": 0 }, "b": { "a": 5, "b": 0 } })
test("a -> b", graph.getDistancesMatrix()["a"]["b"], 5)

(length, path) = findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("shortest path a -> b", length, 5)
(length, path) = findLongestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("longest path a -> b", length, 5)

graph.addDistance("a", "c", 3)
graph.addDistance("b", "c", 4)
(length, path) = findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("shortest path a -> c -> b", length, 7)
(length, path) = findLongestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("longest path a -> b -> c", length, 9)

graph.addDistance("a", "d", 15)
graph.addDistance("b", "d", 8)
graph.addDistance("c", "d", 6)
(length, path) = findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("shortest path b -> a -> c -> d", length, 14)
(length, path) = findLongestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("longest path a -> d -> b -> c", length, 27)



graph = Graph()
with open("testIn.txt") as file:
	for line in file:
		match = re.match(r'^(.*) to (.*) = (.*)$', line, re.I|re.M)
		graph.addDistance(match.group(1), match.group(2), int(match.group(3)))
		
(length, path) = findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("testIn.txt shortest path length", length, 207)
(length, path) = findLongestPath(graph.getCitiesList(), graph.getDistancesMatrix())
test("testIn.txt longest path length", length, 804)

def testPerformace(fn):
	total = 0
	repeats = 100
	for i in range(0, repeats):
		start = time.time()
		fn()
		end = time.time()
		total += (end - start)
	print("Average elasped time: {}".format(total / repeats)) 

print("Performace test:")
testPerformace(lambda: findShortestPath(graph.getCitiesList(), graph.getDistancesMatrix()))