import re

def parseReplacement(line):
	match = re.match(r'^(\w+) => (\w+)$', line, re.M|re.I)
	return (match.group(1), match.group(2))

def getAllOutcomes(formula, replacements):
	derivates = []
	for replacement in replacements:
		derivates += apply(replacement, formula)
	return set(derivates)

def apply(replacement, formula):
	results = []
	for occurance in re.finditer(replacement[0], formula):
		results.append(replace(formula, replacement[1], occurance.start(), occurance.end()))
	return results
	
def replace(formula, replacement, start, end):
	return formula[:start] + replacement + formula[end:]