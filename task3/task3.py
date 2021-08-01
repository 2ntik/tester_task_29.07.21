from sys import argv
from json import load

with open(argv[2], 'r') as file:
	values = load(file)
'''	Это изобретение велосипеда, но я
	первый раз работаю с файлами
	json и не знаю как работать с
	неизвестным количеством уровней
	вложенности, поэтому решение такое
	¯\_(ツ)_/¯
'''
with open(argv[1], 'r') as file:
	value = ''
	report = open('report.json', 'w')
	for line in file:
		if '"id"' in line:
			string = line.split()
			string = string[-1]
			string = string[:-1]
			string = int(string)
			for i in values['values']:
				if i['id'] == string:
					value = i['value']
		if '"value"' not in line:
			report.write(line)
		else:
			report.write(line[0:line.find('""')]+'"'+value+line[line.rfind('"'):])
