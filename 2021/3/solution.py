# !/usr/bin/python3

class Consumption:
	def __init__(string):
		self.type = get_type(string)

file = open('input.txt', 'r')
consumption = [string[:12] for string in file]
counts = [[0, 0] for x in consumption[0]]
for string in consumption:
	for i in range(len(string)):
		c = int(string[i])
		counts[i][c] += 1

# Part 1

gamma = []
epsilon = []
for count in counts:
	if count[0] > count[1]:
		gamma.append('0')
		epsilon.append('1')
	else:
		gamma.append('1')
		epsilon.append('0')

print((gamma))
print((epsilon))
gammaInt = int(('').join(gamma), 2)
epsilonInt = int(('').join(epsilon), 2)
print('gamma', gammaInt)
print('epsilon', epsilonInt)
print('Part 1', gammaInt * epsilonInt)

# Part 2



oxygenCounts = counts
co2Counts = counts[:]
idx = 0
		
while len(oxygenCounts) > 1:
	oneIsBigger = gamma[idx] == '1'
	if oneIsBigger:
		oxygenCounts = [x for x in oxygenCounts if x[idx] == '1']
	else:
		oxygenCounts = [x for x in oxygenCounts if x[idx] == '0']
	idx += 1
idx = 0
while len(co2Counts) > 1:
	oneIsBigger = gamma[idx] == '1'
	if oneIsBigger:
		co2Counts = [x for x in co2Counts if x[idx] == '0']
	else:
		co2Counts = [x for x in co2Counts if x[idx] == '1']
	idx += 1
print(int(oxygenCounts[0], 2) * int(co2Counts[0], 2))

file.close()


