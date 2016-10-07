import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import divisors, getPointsCount

## write tests here --

# part 1

t.test("divisors count of one", divisors(1), [1])
t.test("divisors count of a prime number (5)", divisors(5), [1, 5])
t.test("divisors count of a prime number (19)", divisors(19), [1, 19])
t.test("divisors of a small number (6)", divisors(6), [1, 2, 3, 6])

t.test("points count for 5", getPointsCount(5), 60)
t.test("points count for 6", getPointsCount(6), 120)

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

ARGUMENTS = [ "29000000" ]
if t.report() == True and askYesNo("Run the program with arguments {}?".format(ARGUMENTS)):
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)