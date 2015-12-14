import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()
##

from task import parseLine, generatePermutations, countHappiness, buildStructure, findOptimum, addAmbivalentPerson

## write tests here --

# part 1
happinessDeclaration = [ ("A", "B", -53), ("B", "A", 43), ("A", "C", 12), ("C", "A", -3), ("B", "C", 6), ("C", "B", -1), ("A", "D", 0), ("B", "D", 9), ("C", "D", -14), ("D", "A", -100), ("D", "B", 23), ("D", "C", 14) ]
structure = buildStructure(happinessDeclaration)

t.test("David would lose 53 happiness units by sitting next to Carol.", parseLine("David would lose 53 happiness units by sitting next to Carol."), ("David", "Carol", -53))
t.test("David would gain 43 happiness units by sitting next to Alice.", parseLine("David would gain 43 happiness units by sitting next to Alice."), ("David", "Alice", 43))
t.test("generate permutations", generatePermutations(["a", "b", "c"]), [["a","b","c"], ["a","c","b"], ["b","a","c"], ["b","c","a"], ["c","a","b"], ["c","b","a"]])
t.test("build data structure", structure, { "A": { "B": -53, "C": 12, "D": 0 }, "B": { "A": 43, "C": 6, "D": 9 }, "C": { "A": -3, "B": -1, "D": -14 }, "D": { "A": -100, "B": 23, "C": 14 } })
t.test("count happiness", countHappiness(["A", "B", "C", "D"], structure), -53 + 43 + 0 - 100 + 6 - 1 - 14 + 14)
t.test("find optimum", findOptimum(structure), (9 + 0 + 32 - 10, ["A", "C", "D", "B"]))

# part 2
structure = addAmbivalentPerson(structure, "X")
t.test("build data structure", structure, { "A": { "B": -53, "C": 12, "D": 0, "X": 0 }, "B": { "A": 43, "C": 6, "D": 9, "X": 0 }, "C": { "A": -3, "B": -1, "D": -14, "X": 0 }, "D": { "A": -100, "B": 23, "C": 14, "X": 0 }, "X": { "A": 0, "B": 0, "C": 0, "D": 0 } })
t.test("find optimum", findOptimum(structure), (0 + 0 + 0 + 32 + 5 + 9, ["A", "X", "D", "B", "C"]))

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
	ARGUMENTS = []
	print("Running 'run.py' process with arguments {}".format(ARGUMENTS))
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)