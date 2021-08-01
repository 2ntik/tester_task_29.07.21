from sys import argv
from math import sqrt

circle_file = open(argv[1], 'r')
circle = [line.strip().split() for line in circle_file]
circle_file.close()
circle = [int(circle[0][0]), int(circle[0][-1]), int(circle[1][0])]
# circle 0 - Х центра, 1 - Y центра, 2 - радиус

dots_file = open(argv[2], 'r')
dots = [line.strip().split() for line in dots_file]
dots_file.close()

for dot in dots:
	x = int(dot[0])
	y = int(dot[-1])
	h = sqrt((x - circle[0])**2 + (y - circle[1])**2)
	if h > circle[2]:
		print(2)
	elif h == circle[2]:
		print(0)
	else:
		print(1)
