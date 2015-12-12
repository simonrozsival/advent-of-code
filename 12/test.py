import subprocess
import sys
sys.path.insert(0, "../")
from tester import Tester
t = Tester()

##

from task import hello 

## write tests here --

t.test("dummy test", hello(), "hello world"); 


## -- end of tests

if t.report() == True:
	ARGUMENTS = ["PASTE_ARG_INPUT_HERE"]
	print("Running 'run.py' process with arguments {}".format(ARGUMENTS))
	print("---")
	args = ["python", "run.py"] + ARGUMENTS
	p = subprocess.Popen(args)