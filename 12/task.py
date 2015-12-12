import re
import json

def sumNumbers(data):
	matches = re.findall(r'(-?\d+)', data, re.M|re.I)
	result = 0
	for num in matches:
		result += int(num)
	return result

def sumNumbersWithoutRed(data):
	data = json.loads(data)
	return getValue(data)

def traverseArray(data):
	result = 0
	for item in data:
		result += getValue(item)
	return result

def traverseObject(data):
	isRed = False
	result = 0
	for item in data:
		item = data[item]
		if item == "red":
			isRed = True
			break
		else:
			if type(item) is int:
				result += int(item)
			elif type(item) is dict:
				result += traverseObject(item)
			elif type(item) is list:
				result += traverseArray(item)
	return result if isRed == False else 0

def getValue(data):	
	if type(data) is int:
		return int(data)
	elif type(data) is dict:
		return traverseObject(data)
	elif type(data) is list:
		return traverseArray(data)
	else:
		return 0