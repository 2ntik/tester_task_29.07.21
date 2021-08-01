from sys import argv

n = int(argv[1])
step_len = int(argv[2])
n = [i+1 for i in range(n)]
step = 0
output = '1'
marker = False
while True:
	for i in n:
		step += 1
		if step == step_len:
			step = 1
			if i == 1:
				marker = True
				break
			else:
				output += str(i)
	if marker:
		break
print(output)
