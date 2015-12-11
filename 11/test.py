import sys
sys.path.insert(0, "../")

from test import test
from password_gen import isValid, iterate

test("iterate ac", iterate("ac"), "ad")
test("iterate az", iterate("az"), "ba") 
test("iterate azz", iterate("azz"), "baa")
test("iterate abc", iterate("abc"), "abd")
test("iterate abcz", iterate("abcz"), "abda")
test("iterate z", iterate("z"), "aa") 
test("iterate zzzzzzzz", iterate("zzzzzzzz"), "aaaaaaaa") 

test("isValid('a')", isValid("a"), False)
test("isValid('iiiiiiii')", isValid("iiiiiiii"), False)
test("isValid('aaaaaaaa')", isValid("aaaaaaaa"), False)
test("isValid('abdcefhg')", isValid("abdcefhh"), False)
test("isValid('abcabcaa')", isValid("xxxabcab"), False)
test("isValid('abcabcaa')", isValid("xxcabcaa"), True)