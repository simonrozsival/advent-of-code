import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import getCombinationsCount, getMinimalCombinationsCount

## write tests here --

# part 1

t.test("nothing to divide", getCombinationsCount(0, [1, 2, 3]), 1)
t.test("too small bottle", getCombinationsCount(10, [5]), 0)
t.test("one large enough bottle", getCombinationsCount(10, [10]), 1)
t.test("two bottles", getCombinationsCount(2, [2, 2]), 2)
t.test("two bottles, one too small", getCombinationsCount(2, [2, 1]), 1)
t.test("two small bottles", getCombinationsCount(2, [1, 1]), 1)

# part 2

t.test("", getMinimalCombinationsCount(10, [5, 5, 5, 10]), 1)

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

ARGUMENTS = [ "150" ]
if t.report() == True and askYesNo("Run the program with arguments {}?".format(ARGUMENTS)):
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)