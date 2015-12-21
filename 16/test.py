import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

# from task import parseLine

## write tests here --

# part 1

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

ARGUMENTS = [ ]
if t.report() == True and askYesNo("Run the program with arguments {}?".format(ARGUMENTS)):
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)