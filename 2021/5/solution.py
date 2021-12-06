file = open('input.txt', 'r')

# Part 1

inp = [line.strip() for line in file]
coordinates = []
maxX, maxY = 0, 0
for line in inp:
	line = line.split(' -> ')
	newLine = []
	for x in line:
		x = x.split(',')
		asInts = [int(y) for y in x]
		if asInts[0] > maxX:
			maxX = asInts[0]
		if asInts[1] > maxY:
			maxY = asInts[1]
		newLine.append(asInts)
	coordinates.append(newLine)
grid = [[0 for j in range(maxY + 1)] for i in range(maxX + 1)]

def markHorizontal(line):
	# line to points
	p1, p2 = line
	# points to x/y
	x1, y1 = p1
	x2, y2 = p2

	if x1 == x2:
		if y2 < y1:
			y1, y2 = y2, y1		
		for y in range(y1, y2 + 1):
			grid[x1][y] += 1

	if y1 == y2:

		if x2 < x1:
			x1, x2 = x2, x1
		for x in range(x1, x2 + 1):
			grid[x][y1] += 1

for line in coordinates:
	markHorizontal(line)

intersect = 0
for x in grid:
	for y in x:
		if y > 1:
			intersect += 1
# for x in grid:
# 	print(x)
print('Part 1:', intersect)

def markDiagonal(line):
	# line to points
	p1, p2 = line
	# points to x/y
	x1, y1 = p1
	x2, y2 = p2

	# diagonal only
	if x1 != x2 and y1 != y2:
		# always low -> high on x
		if x2 < x1:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		if y2 > y1:
			while x1 <= x2 and y1 <= y2:
				grid[x1][y1] += 1
				x1 += 1
				y1 += 1
		else:
			while x1 <= x2 and y1 >= y2:
				grid[x1][y1] += 1
				x1 += 1
				y1 -= 1


for line in coordinates:
	markDiagonal(line)

intersect = 0
for x in grid:
	for y in x:
		if y > 1:
			intersect += 1
# for x in grid:
# 	print(x)
# 21924 too high
print('Part 2:', intersect)
