import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()

##

from task import sumNumbers, sumNumbersWithoutRed

## write tests here --

# part 1
t.test("array", sumNumbers("[1,2,3]"), 6); 
t.test("negative value", sumNumbers("[1,4,-3]"), 2); 
t.test("nested json with red value", sumNumbers("{\"a\": [1,3], \"b\":{\"color\": \"red\",\"number\":-3,\"data\":{\"x\":5}}}"), 6);
t.test("nested json", sumNumbers("[{\"a\":5}, 3, [1, {\"red\": \"not-red\", \"x\": 6}, {\"n\": -50, \"green\":\"red\"}]]"), -35) 

# part 2
t.test("array", sumNumbersWithoutRed("[1,2,3]"), 6); 
t.test("negative value", sumNumbersWithoutRed("[1,4,-3]"), 2); 
t.test("nested json with red value", sumNumbersWithoutRed("{\"a\": [1,3], \"b\":{\"color\": \"red\",\"number\":-3,\"data\":{\"x\":5}}}"), 4);
t.test("nested json", sumNumbersWithoutRed("[{\"a\":5}, 3, [1, {\"red\": \"not-red\", \"x\": 6}, {\"n\": -50, \"green\":\"red\"}]]"), 15) 


## -- end of tests

if t.report() == True:
	ARGUMENTS = []
	print("Running 'run.py' process with arguments {}".format(ARGUMENTS))
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)