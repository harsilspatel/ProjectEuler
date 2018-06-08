#squaresDictionary = {i:i**2 for i in range(1, 10)}
#doesReachAnswer = {1:False}
#
##count = 0
##for i in range(1, 10**6):
##	j = i
##	while (j != 1 and j != 89):
##		if j in squaresDictionary:
##			j = squaresDictionary[j]
##		else:
##			result = sum([k**2 for k in list(map(int, list(str(j))))])
##			squaresDictionary[j] = result
##			j = result
##	if j == 89:
##		count += 1
###	print(i, squaresDictionary)
##		
##print(count)
#
##count = 0
##for i in range(1, 10**6):
##	j = i
##	paths = []
##	while True:
##		if j in doesReachAnswer:
##			if doesReachAnswer[j]:
##				count += 1
##			break
##		else:
##			if j in squaresDictionary:
##				j = squaresDictionary[j]
##			else:
##				result = sum([k**2 for k in list(map(int, list(str(j))))])
##				squaresDictionary[j] = result
##				j = result
##			paths.append(j)
##		if j == 1:
##			for l in paths:
##				doesReachAnswer[l] = False
##		if j == 89:
##			for l in paths:
##				doesReachAnswer[l] = True
##			count += 1
##	#	print(i, squaresDictionary)
#		
#print(count)

def digitsSquareSum(number):
	if number in squareSumDictionary:
		return squareSumDictionary[number]
	else:
		theSum = 0
		while number != 0:
			theSum += squares[number % 10]
			number //= 10
		squareSumDictionary[number] = theSum
		return theSum

squares = {i:i**2 for i in range(10)}
squareSumDictionary = {i:i**2 for i in range(10)}
doesReachAnswer = {1:False, 89:True}
countEightyNine = 0
countOne = 0

for i in range(1,10**7):
	j = i
	paths = [j]
	while j not in doesReachAnswer:
#		j = sum([squares[k] for k in list(map(int, list(str(j))))])
		j = digitsSquareSum(j)
		paths.append(j)
	
	if doesReachAnswer[j]:
		countEightyNine += 1
#		print(i)
	else:
		countOne += 1
	
	for k in paths:
		doesReachAnswer[k] = doesReachAnswer[j]

#print(doesReachAnswer)
print(countEightyNine, countOne)