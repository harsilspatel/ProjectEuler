powersDictionary = {}

def power(i, j):
	powersDictionary[(i, 0)] = 1
	if (i, j) in powersDictionary:
		return powersDictionary[(i, j)]
	else:
		product = i*power(i, j-1)
		powersDictionary[(i, j)] = product
		return product

print(power(2, 10))
print(powersDictionary)
#
#maxSum = [0, 0, 0]
#for i in range(2, 400):
#	for j in range(1, 400):
#		powerResult = i**j
#		theSum = sum(map(int, list(str(powerResult))))
#		if theSum > maxSum[0]:
#			maxSum[0] = theSum
#			maxSum[1] = i
#			maxSum[2] = j
#
#print(maxSum)