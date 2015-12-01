import sys
import linecache 


def verifyArrayLength(length):
	global array
	if len(array) < length:
		array += [None] * (length - len(array))

array = []
if len(sys.argv) > 1:
	lineCount = len(linecache.getlines(sys.argv[1]))
	cursor = 1	
	while cursor <= lineCount: 	
		line = linecache.getline(sys.argv[1],cursor)	
		print(str(cursor) + ": " + line + " "),
		
		cursor += 1
		
		if line[0].upper() == "A":
			values = [x.strip() for x in line[1:].split(',')]
			verifyArrayLength(int(values[0])+1)
			array[int(values[0])] = int(values[1])	
		elif line[0].upper() == "Z":
			verifyArrayLength(int(line[1:])+1)
			array[int(line[1:])] = 0
		elif line[0].upper() == "I":
			verifyArrayLength(int(line[1:])+1)
			array[int(line[1:])] += 1
		elif line[0].upper() == "J":
			values = [x.strip() for x in line[1:].split(',')]
			verifyArrayLength(int(values[0])+1)
			verifyArrayLength(int(values[1])+1)
			if array[int(values[0])] != array[int(values[1])]:
				cursor = int(values[2])
		
		print array
else:
	print "Error: include a path to source code you would like the zmachine to run"

