from gates import push_gate, evaluate

def init():
	gates = {}
	with open("instructions.txt") as file:
		for line in file:
			gates = push_gate(gates, line)
	return gates

gates = init()
a = evaluate(gates, "a")

# first part
print("first part: {}".format(a))

gates = init()
gates["b"] = a
a = evaluate(gates, "a")
print("second part: {}".format(a))