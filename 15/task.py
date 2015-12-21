import re

def parseLine(line):
	# 'Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3'
	matches = re.match(r'^(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d)$', line, re.M|re.I)
	# tuple (name, properties)
	return (matches.group(1), [int(matches.group(2)), int(matches.group(3)), int(matches.group(4)), int(matches.group(5)), int(matches.group(6))])

def getScoreWithoutCalories(teaspoons, ingredient):
	return getScore(teaspoons, ingredient[0:-1])

def getScore(teaspoons, ingredient):
	return map(lambda x: teaspoons*x, ingredient)

def getTotalCaloriesCount(ratio, ingredients):
	return sum(map(lambda teaspoons, ingredient: teaspoons*ingredient[-1], ratio, ingredients))

def isZero(score):
	return not reduce(lambda acc, val: acc and val > 0, score, True)

def getTotalScore(ratio, ingredients, cookieFilter = lambda x, y: True):
	if not cookieFilter(ratio, ingredients):
		return 0
	scores = [max(0, sum(x)) for x in zip(*map(getScoreWithoutCalories, ratio, ingredients))] # negative score becomes 0
	return reduce(lambda x, y: x*y, scores, 1)
	
def getMaxScore(capacity, ingredients, cookieFilter = lambda x, y: True):
	return _getMaxScore(capacity, [], [], ingredients, cookieFilter)

def _getMaxScore(capacity, ratioPrefix, ingredientsPrefix, ingredients, cookieFilter):
	ingredient = ingredients[0]
	restOfIngredients = ingredients[1:]
	newIngredientsPrefix = ingredientsPrefix + [ingredient]
	maximum = getTotalScore(ratioPrefix + [capacity], newIngredientsPrefix, cookieFilter) # initial value -> do not leave any teaspoos for the rest of ingredients
	
	if len(restOfIngredients) == 0:
		return maximum # end the recursion here - I cannot split the capacity any more
	
	for i in range(capacity - 1, 0, -1):
		newScore = _getMaxScore(capacity - i, ratioPrefix + [i], newIngredientsPrefix, restOfIngredients, cookieFilter)
		if maximum < newScore:
			maximum = newScore
	
	return maximum