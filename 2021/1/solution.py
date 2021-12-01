file = open('input.txt', 'r')
numbers = [int(num) for num in file]
increases = 0

for i, number in enumerate(numbers):
	if i != 0:
		if number > numbers[i - 1]:
			increases += 1
	
print(increases)

group_3_increases = 0
for i in range(3, len(numbers)):
	previous = sum(numbers[i - 3:i])
	current = sum(numbers[i - 2:i + 1])
	if current > previous:
		group_3_increases += 1

print(group_3_increases)

file.close()
