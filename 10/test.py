from look_and_say import lookAndSay

def test(name, real, expected):
	if (expected == real):
		print("OK - {}".format(name))
	else:
		print("FAIL - {}: {} should be {}".format(name, real, expected))

test("1 -> 11", lookAndSay('1'), '11')
test("11 -> 21",	lookAndSay('11'), '21')
test("111 -> 31",	lookAndSay('111'), '31')
test("1122 -> 2122",	lookAndSay('1122'), '2122')
test("21 -> 1211",	lookAndSay('21'), '1211')
test("1211 -> 111221",	lookAndSay('1211'), '111221')
test("111221 -> 312211",	lookAndSay('111221'), '312211')
test("1113122113 -> 311311222113", lookAndSay('1113122113'), '311311222113')