import sys, hashlib

def md5(str):
	return hashlib.md5(str.encode('utf-8')).hexdigest()

def isOK(password, number, length):
	h = md5("{}{}".format(password, number))
	return h[0:length] == "0"*length
	
if len(sys.argv) < 3:
	print("No password or length was given.")
	sys.exit(1)

password = sys.argv[1]
length = int(sys.argv[2])

print("mining adventcoins with password '{}' with {} leading zeros ({})".format(password, length, "0"*length))

i = 0
while not isOK(password, i, length):
	i += 1
	if i % 100000 == 0:
		print("reached {}".format(i))
 
print(i)