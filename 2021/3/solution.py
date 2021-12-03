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


file.close()


