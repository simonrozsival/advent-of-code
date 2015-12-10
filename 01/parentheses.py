#!/usr/bin/python

level = 0
position = 0

with open("in.txt", "r") as data:
	c = data.read(1)
	while c:
		if c == '(':
			level = level + 1
		else:
			level = level - 1
		position = position + 1
		if level < 0:			
			break;
		c = data.read(1)

print("Level: {}, position: {}".format(level, position))