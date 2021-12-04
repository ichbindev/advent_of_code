class Solution:
	def __init__(self):
		self.depth = 0
		self.horizontal = 0

	def forward(self, number):
		self.horizontal += number

	def up(self, number):
		self.depth -= number

	def down(self, number):
		self.depth += number

	def solve(self):
		return self.depth * self.horizontal

class Solution2:
	def __init__(self):
		self.depth = 0
		self.horizontal = 0
		self.aim = 0

	def forward(self, number):
		self.horizontal += number
		self.depth += self.aim * number

	def up(self, number):
		self.aim -= number

	def down(self, number):
		self.aim += number

	def solve(self):
		return self.depth * self.horizontal

file = open('input.txt', 'r')
instructions = [ins for ins in file]
solution = Solution()

for instruction in instructions:
	instruction, number = instruction.split(' ')
	number = int(number)
	if instruction == 'up':
		solution.up(number)
	elif instruction == 'down':
		solution.down(number)
	elif instruction == 'forward':
		solution.forward(number)

print('Part one solution', solution.solve())

solution = Solution2()

for instruction in instructions:
	instruction, number = instruction.split(' ')
	number = int(number)
	if instruction == 'up':
		solution.up(number)
	elif instruction == 'down':
		solution.down(number)
	elif instruction == 'forward':
		solution.forward(number)

print('Part one solution', solution.solve())


file.close()