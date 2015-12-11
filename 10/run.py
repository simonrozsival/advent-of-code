import sys
from look_and_say import lookAndSay

if len(sys.argv) < 3:
	print("Missing puzzle input")
	sys.exit()
	
puzzleInput = sys.argv[1]
n = int(sys.argv[2])

result = puzzleInput
for i in range(0, n):
	result = lookAndSay(result)

# print("Playing look-and-say with '{}' {} times -> '{}'".format(puzzleInput, n, result))
print("the length of the output is {}".format(len(result)))