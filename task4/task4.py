from sys import argv

file = open(argv[1], 'r')
nums = [int(line.strip()) for line in file]
file.close()
average = int(sum(nums)/len(nums))
steps = 0
for i in nums:
	if i > average:
		steps += i - average
	else:
		steps += average - i
print(steps)
