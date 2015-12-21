import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import parseLine, getScore, getTotalScore, getMaxScore

## write tests here --

# part 1

# parsing input
line = "Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3"
output = ("Sprinkles", [2, 0, -2, 0, 3])
t.test("Parsing input", parseLine(line), output)

# calculating score
t.test("Calculate score", getScore(10, [1, 2, 3]), [10, 20, 30])
t.test("Skip calories 1", getTotalScore([1, 2], [[1, 0], [2, -1]]), 5)
t.test("Skip calories 2", getTotalScore([1, 2], [[1, 0], [-2, 1]]), 0)
# max score
t.test("Calculate max score", getMaxScore(100, [[-1, -2, 6, 3, 8], [2, 3, -2, -1, 3]]), 62842880)

# part 2

## -- end of tests

def askYesNo(question):
	print(question + " [y/n]")
	yes = set(['yes','y', 'ye', ''])
	no = set(['no','n'])	
	while True:
		choice = raw_input().lower()
		if choice in yes:
			return True
		elif choice in no:
			return False
		else:
			print("Answer with 'y' (yes) or 'n' (no).")

ARGUMENTS = [ "100", "500" ]
if t.report() == True and askYesNo("Run the program with arguments {}?".format(ARGUMENTS)):
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)