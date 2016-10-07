def readGridLine(line):
	row = []
	for c in line:
		if c == "#":
			row.append(True)
		if c == ".":
			row.append(False)
	return row

def animationStep(grid):
	newGrid = []	
	for i in range(0, len(grid)):
		row = []
		for j in range(0, len(grid[i])):
			if isOn(grid, i, j): # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
				if onNeighboursCount(grid, i, j) in [2, 3]:
					row.append(True)
				else:		
					row.append(False)
			else: # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
				if onNeighboursCount(grid, i, j) in [3]:
					row.append(True)
				else:		
					row.append(False)
		newGrid.append(row)

	return newGrid

def animationStepWithCornersOn(grid):
	if len(grid) == 0 or len(grid[0]) == 0:
		raise Exception("Grid must have at least one row and one column.")
	grid = animationStep(grid)
	# now for the corners
	grid[0][0] = True
	grid[0][len(grid[0]) - 1] = True
	grid[len(grid) - 1][0] = True
	grid[len(grid) - 1][len(grid[0]) - 1] = True
	return grid

neighbours = [
	(-1, -1),
	( 0, -1),
	( 1, -1),
	( 1,  0),
	( 1,  1),
	( 0,  1),
	(-1,  1),
	(-1,  0)
]

def onNeighboursCount(grid, i, j):
	count = 0
	for n in neighbours:
		count += 1 if isOn(grid, i + n[0], j + n[1]) else 0
	return count

def isOn(grid, i, j):
	if i < 0 or j < 0 or i >= len(grid) or len(grid) == 0 or j >= len(grid[0]):
		return False
	return grid[i][j]

def animate(grid, steps, method = animationStep):
	for step in range(0, steps):
		grid = method(grid)
	return grid

def lightsOnCount(grid):
	return reduce(lambda acc, row: acc + reduce(lambda acc, cell: acc + (1 if cell == True else 0), row, 0), grid, 0)