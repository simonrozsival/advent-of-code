
import re

MAX16BIT = (2 ** 16 - 1) 

def signal(x):
	_x = x
	def resolve(gates):
		return int(_x) & MAX16BIT
	
	return resolve

def redirect(x):
	_x = x
	def resolve(gates):
		return evaluate(gates, _x)
	
	return resolve
	

def and_gate(x, y):
	_x = x
	_y = y
	def resolve(gates):
		x = evaluate(gates, _x)
		y = evaluate(gates, _y)
		return x & y & MAX16BIT
	
	return resolve
	
def or_gate(x, y):
	_x = x
	_y = y
	def resolve(gates):
		x = evaluate(gates, _x)
		y = evaluate(gates, _y)
		return (x | y) & MAX16BIT
	
	return resolve

def not_gate(x):
	_x = x 
	def resolve(gates):
		x = evaluate(gates, _x)
		return x ^ MAX16BIT
	
	return resolve
	
def rshift_gate(x, n):
	_x = x
	_n = n
	def resolve(gates):
		x = evaluate(gates, _x)	
		return (x >> _n) & MAX16BIT
	
	return resolve
	
def lshift_gate(x, n):
	_x = x
	_n = n
	def resolve(gates):		
		x = evaluate(gates, _x)
		return (x << _n) & MAX16BIT
	
	return resolve

def parse_gate(expr):
	# just a signal:
	s = re.match(r'^(\d+)$', expr, re.M|re.I)
	if s != None:
		return signal(s.group(1))
	
	# not gate:
	notGate = re.match(r'^NOT (.*)$', expr, re.M|re.I)
	if notGate != None:
		return not_gate(notGate.group(1))
		
	# rigth shift gate
	rshift = re.match(r'^(.*) RSHIFT (.*)', expr, re.M|re.I)
	if rshift != None:
		return rshift_gate(rshift.group(1), int(rshift.group(2)))
		
	# left shift gate
	lshift = re.match(r'^(.*) LSHIFT (.*)', expr, re.M|re.I)
	if lshift != None:
		return lshift_gate(lshift.group(1), int(lshift.group(2)))
		
	# or gate
	orGate = re.match(r'^(.*) OR (.*)', expr, re.M|re.I)
	if orGate != None:
		return or_gate(orGate.group(1), orGate.group(2))
		
	# and gate
	andGate = re.match(r'^(.*) AND (.*)', expr, re.M|re.I)
	if andGate != None:
		return and_gate(andGate.group(1), andGate.group(2))
		
	return redirect(expr.strip())

def push_gate(gates, expr):
	split = re.match(r'^(.*) -> (.*)$', expr, re.M|re.I)
	dependency_eval = parse_gate(split.group(1))
	letter = split.group(2).strip()
	gates[letter] = dependency_eval
	return gates
	
def evaluate(gates, letter):
	try:
		if type(letter) == int or type(int(letter)) == int:
			return int(letter)
	except:
		pass

	val = gates[letter.strip()]
	if type(val) != int:
		val = int(val(gates))
		gates[letter] = val
		
	return val