import sys
from password_gen import findNewPassword

if len(sys.argv) < 2:
	print("Missing old password as the first argument of the program.")
	sys.exit(1)

oldPwd = sys.argv[1]

# part one
newPwd = findNewPassword(oldPwd)
print("The new password is '{}'".format(newPwd))

# part two
nextPwd = findNewPassword(newPwd)
print("The next new password is '{}'".format(nextPwd))