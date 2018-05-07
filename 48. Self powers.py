#def manualAdd(numbersList):
#	theList = numbersList[:]
#	digits = len(str(theList[0]))
#	numberOfNumbers = len(theList)
#
#	theSum = 0
#	theSumString = ''
#	for columns in range(digits-1, -1, -1):
#		for rows in range(numberOfNumbers):
#			theList[rows] = str(theList[rows])
#			theSum += int(theList[rows][columns])
#		theSumString += str(theSum)[-1]
#		theSum = int(str(theSum)[:-1])
#	
#	theSumString += str(theSum)[::-1]
#	return int(theSumString[::-1])

print(sum([(i**i)%(10**10) for i in range(1, 1001)]) % 10**10)
	