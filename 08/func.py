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
			if d == '"':
				skip = 1
			elif d == "\\":
				skip = 1
			elif d == "x":
				skip = 3
	# print("'{}' ({})".format(line, length))
	return length
	
def encode(line):
	output = ""
	for char in line:
		if char == '\"':
			output += '\\\"'
		elif char == '\\':
			output += '\\\\'
		else:
			output += char
	output = '\"{}\"'.format(output)
	print("{} -> {}".format(line, output))
	return output
		