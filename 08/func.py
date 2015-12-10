def unescaped_length(line):
	line = line[1:len(line)-1]
	length = 0
	skip = 0
	for i in range(0, len(line)):
		if skip > 0:
			skip -= 1
			continue
		
		c = line[i]
		length += 1
		if c == "\\": 
			d = line[i+1]
			if d == '"' or d == "\\":
				skip = 1
			elif d == "x":
				try:
					twoDigits = int(line[i+2:i+4])
					skip = 3
				except:				
					pass
	print("'{}' ({})".format(line, length))
	return length