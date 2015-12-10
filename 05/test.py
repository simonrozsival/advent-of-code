from niceWords2Functions import eye, containsPairTwice, isNice

def test(desc, a, b):
	if a != b:
		raise Exception("FAIL: {} - {} shoud be {}".format(desc, a, b))

test("eye(aa)", eye("aa"), False)
test("eye(aax)", eye("aax"), False)
test("eye(baxab)", eye("baxab"), True)

test("containsPairTwice(xx)", containsPairTwice("xx"), False)
test("containsPairTwice(xxx)", containsPairTwice("xxx"), False)
test("containsPairTwice(xxaa)", containsPairTwice("xxaa"), False)
test("containsPairTwice(axxa)", containsPairTwice("axxa"), False)
test("containsPairTwice(axxxxa)", containsPairTwice("axxxxa"), True)


print("All tests passed")