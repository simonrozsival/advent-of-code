import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import parseReplacement, replace, apply, getAllOutcomes

## write tests here --

# part 1

t.test("parse replacement line", parseReplacement("OH => HO"), ("OH", "HO"))
t.test("replace part of the molecule name", replace("H2O", "OO", 0, 1), "OO2O")
t.test("replace part of the molecule name", replace("H2O", "OO", 1, 2), "HOOO")
t.test("replace part of the molecule name", replace("H2O", "OO", 1, 3), "HOO")
t.test("apply replacement", apply(("HO", "OH"), "HOOH"), ["OHOH"])
t.test("apply replacement", apply(("HO", "OH"), "HOHO"), ["OHHO", "HOOH"])
t.test("derivates count", getAllOutcomes("HOH", [ ("H", "HO"), ("H", "OH"), ("O", "HH") ]), set([ "HOOH", "HOHO", "OHOH", "HHHH" ]))

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