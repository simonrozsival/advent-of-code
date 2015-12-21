import re

def getCombinationsCount(eggnog, bottles, maxBottles = 100000000): # $~^&*{} "infinity" 
	if eggnog == 0:
		return 1 # there is nothing to divide into the rest of bottles

	if maxBottles == 0:
		return 0 # no spare bottles left

	bottle = bottles[0]
	bottles = bottles[1:]

	if (len(bottles) == 0): # this is the last bottle
		if (bottle == eggnog):
			return 1 # there is one combination - fill the rest into the last bottle
		else:
			return 0 # the rest does not fit into the bottle
	
	# else, try to reproduce all possibilities:
	combinations = getCombinationsCount(eggnog, bottles, maxBottles) # skip this bottle 
	if eggnog >= bottle:
		combinations += getCombinationsCount(eggnog - bottle, bottles, maxBottles - 1)
	
	return combinations

def getMinimalCombinationsCount(eggnog, bottles):
	for usedBottles in range(0, len(bottles)):
		combinations = getCombinationsCount(eggnog, bottles, usedBottles)
		if combinations > 0:
			return combinations
	return 0