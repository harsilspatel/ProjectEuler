inFile = open('p099_base_exp.txt')
numbers = []
for line in inFile:
	a, b = line.split(',')
	numbers.append((int(a), int(b)))

inFile.close()

maxPair = numbers[0]
for i in numbers:
	if maxPair[0] > i[0] and maxPair[1] > i[1]:
		continue
	if maxPair[0] < i[0] and maxPair[1] < i[1]:
		maxPair = i
	if i[1] > maxPair[1]:
		a, b = i, maxPair
	else:
		a, b = maxPair, i
	powerDifference = a[1] - b[1]
	
	if a[0]*(pow(b[0],(powerDifference)/a[1])) > b[0]:
		maxPair = a
	else:
		maxPair = b

print(maxPair, numbers.index(maxPair) + 1)
	