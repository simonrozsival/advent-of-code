import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import createReindeer, run, move, rest

## write tests here --

# part 1
reindeer = createReindeer("Tester can fly 1 km/s for 5 seconds, but then must rest for 10 seconds.")
t.test("reindeer input parsing", reindeer, ("Tester", 1, 5, 10))
t.test("reindeer runs 20 km in 50 seconds", run(50, reindeer[1:]), 20)

movement = move(5, (0, 4), reindeer[1:])
t.test("respect max travel time in movement - move only for one second", movement[0], 1)
t.test("respect max travel time in movement - reach end after one second", movement[1], 5)

rested = rest(5, (0, 4), reindeer[1:]) # rest for one second
t.test("respect max travel time in resting - do not move", rested[0], 0)
t.test("respect max travel time in resting - rest for one second only", rested[1], 5)

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

if t.report() == True and askYesNo("Run the program?"):
	ARGUMENTS = [ "2503" ]
	print("Running 'run.py' process with arguments {}".format(ARGUMENTS))
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)