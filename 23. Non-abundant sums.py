def generateFactors(n):
	factors = []
	for i in range(1, int(n**(1/2)) + 1):
		if n % i == 0:
			factors.append(i)
			factors.append(n//i)
	return list(set(factors))


abundantNumbers = [i for i in range(28123) if sum(generateFactors(i)) - i > i]

sumOfTwoAbundantNumbers = []
for i in range(len(abundantNumbers)):
#	loopBroken = False
	for j in range(i, len(abundantNumbers)):
		theSum = abundantNumbers[i] + abundantNumbers[j]
		if theSum > 28123: break
		else: sumOfTwoAbundantNumbers.append(theSum)

#for i in sumOfTwoAbundantNumbers: print(i)
sumOfTwoAbundantNumbers = set(sumOfTwoAbundantNumbers)
requiredSum = 0
for i in range(28123):
	if i not in sumOfTwoAbundantNumbers:
		requiredSum += i
		
print(requiredSum)