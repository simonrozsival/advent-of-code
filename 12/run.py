import sys

ARGS_COUNT = 0
if len(sys.argv) < ARGS_COUNT:
	print("Missing arguments")
	sys.exit(1)

data = sys.argv[1]
print("input argument: {}".format(data))

##

result = 0

with open("in.txt") as file:
	for line in file:
		pass


##

print("The result is '\033[1;33m{}\033[1;m'".format(result))
sys.exit(0)