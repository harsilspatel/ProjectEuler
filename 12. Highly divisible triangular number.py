#def triangeNumber(n):
#	return (n*(n+1)//2)
#
#i = 1
#factors = 1
#while factors < 500:
#	factors = 1
#	theNumber = triangeNumber(i)
#	for divisor in range(1, theNumber//2 + 1):
#		if theNumber % divisor == 0: factors += 1
#	print(i, theNumber, factors)
#	i += 1
#	
#print(theNumber)


# Can still be improved by remembering using dynamic programming

#factorsDictionary = {1:1}

def triangeNumber(n):
	return (n*(n+1)//2)

def factors(n):
	originalNumber = n
	factorsList = []
	for i in range(1, int(n**0.5) + 1): 
		if n % i == 0:
			factorsList.append(i)
			n //= i
			factorsList.append(n)
#			print(factorsList)
	numberOfFactors = len(set(factorsList))
#	factorsDictionary[originalNumber] = numberOfFactors
	return numberOfFactors
	
i = 1
numberOfFactors = 0
while numberOfFactors < 500:
	theNumber = triangeNumber(i)
	numberOfFactors = factors(theNumber)
	print(i, theNumber, factors(theNumber))
	i += 1
	
	
	
	

