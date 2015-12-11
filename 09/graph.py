
class Graph:
	def __init__(self):
		self.cities = []
		self.distances = {}
	def getCitiesList(self):
		return self.cities
	def addDistance(self, a, b, dist):
		self.addCity(a)
		self.addCity(b)
		self.distances[a][b] = dist
		self.distances[b][a] = dist
	def addCity(self, city):
		if city not in self.cities:
			self.cities.append(city)
			self.distances[city] = {}
			self.distances[city][city] = 0
	def getDistancesMatrix(self):
		return self.distances			