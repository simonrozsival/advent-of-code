import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import readGridLine, isOn, onNeighboursCount, lightsOnCount

## write tests here --

# part 1

t.test("parse line", readGridLine("..##..#."), [False, False, True, True, False, False, True, False])
t.test("grid coords", isOn([[True, False]], 0, 0), True)
t.test("grid coords", isOn([[False, True]], 0, 1), True)
t.test("out of grid neighbours", onNeighboursCount([[True]], 0, 0), 0)
t.test("some neighbours are out of grid neighbours", onNeighboursCount([[True, False, True]], 0, 1), 2)
t.test("all neighbours on", onNeighboursCount([[True, True, True], [True, True, True], [True, True, True]], 1, 1), 8)
t.test("half neighbours on", onNeighboursCount([[True, False, True], [False, True, False], [True, False, True]], 1, 1), 4)
t.test("half neighbours on", lightsOnCount([[False, False, False], [False, False, False], [False, False, False]]), 0)
t.test("half neighbours on", lightsOnCount([[False, False, False], [False, True, False], [False, False, False]]), 1)

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

ARGUMENTS = [ "100" ]
if t.report() == True and askYesNo("Run the program with arguments {}?".format(ARGUMENTS)):
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)