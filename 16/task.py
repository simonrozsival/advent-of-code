import re

class Aunt:
	def __init__(self, id):
		self.id = id
		self.props = {}
	
	def addProp(self, name, value):
		self.props[name] = value
	
	def hasProp(self, name):
		return name in self.props
		
	def getPropValue(self, name):
		return self.props[name]
		
	def match(self, sue):
		for prop in self.props:			
			if sue.hasProp(prop):
				if self.getPropValue(prop) != sue.getPropValue(prop):
					return False
		return True
	
	def matchPartTwo(self, sue):	
		for prop in self.props:			
			if sue.hasProp(prop):
				if prop in ["cats", "trees"]:
					if self.getPropValue(prop) >= sue.getPropValue(prop):
						return False
				elif prop in ["pomeranians", "goldfish"]:
					if self.getPropValue(prop) <= sue.getPropValue(prop):
						return False
				elif self.getPropValue(prop) != sue.getPropValue(prop):
					return False
		return True

idRegexp = re.compile(r'^Sue (\d+)')
infoRegexp = re.compile(r'[,:] (\w+): (\d+)')

def parseLine(line):
	idMatch = idRegexp.match(line)
	infoMatches = infoRegexp.findall(line)
	
	aunt = Aunt(int(idMatch.group(1)))
	for (prop, val) in infoMatches:
		aunt.addProp(prop, int(val))
	
	return aunt

def findAunt(aunts, sue):
	for aunt in aunts:
		if sue.match(aunt):
			return aunt
	return None

def findAuntPartTwo(aunts, sue):
	for aunt in aunts:
		if sue.matchPartTwo(aunt):
			return aunt
	return None