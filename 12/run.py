import sys

ARGS_COUNT = 0
if len(sys.argv) < ARGS_COUNT:
	print("Missing arguments")
	sys.exit(1)

from task import sumNumbersWithoutRed

##

result = 0

with open("in.txt") as file:
	data = file.read()
	result = sumNumbersWithoutRed(data)


##

print("The result is '\033[1;33m{}\033[1;m'".format(result))
sys.exit(0)