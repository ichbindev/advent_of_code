class Board:
	def __init__(self, board_rep):
		board = []
		for line in board_rep:
			line = line.split('\n')[0]
			line = line.split(' ')
			row = [int(i) for i in line if i != '']
			board.append(row)
		self.board = board

	def mark(self, num):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] == num:
					self.board[i][j] = -1

	def is_solved(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] != -1:
					break;
				if j == len(self.board) - 1:
					return True
		for j in range(len(self.board[0])):
			for i in range(len(self.board)):
				if self.board[i][j] != -1:
					break;
				if i == len(self.board) - 1:
					return True
		return False

	def get_solution(self, last_num):
		sum = 0
		for row in self.board:
			for num in row:
				if num != -1:
					sum += num
		return sum * last_num

file = open('input.txt', 'r')

# Part 1

inp = [line for line in file]
calls = inp[0].split(',')
calls = [int(i) for i in calls]
boards = []
i = 2
while i < len(inp):
	boardInput = []
	for j in range(0, 5):
		boardInput.append(inp[i])
		i += 1
	i += 1
	board = Board(boardInput)
	boards.append(board)
found = False
for call in calls:
	if found: break
	for board in boards:
		board.mark(call)
		if board.is_solved():
			print('The answer for Part 1 is', board.get_solution(call))
			found = True
			break



file.close()