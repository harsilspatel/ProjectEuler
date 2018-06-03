def factorial(n):
	product = 1
	for i in range(1, n+1):
		product *= i
	return product
	
factorialsDictionary = {}
for i in range(10):
	factorialsDictionary[i] = factorial(i)
#print(factorialsDictionary)

#def getDigits(n):
#	digits = []
#	while n != 0:	
#		digits.append(n % 10)
#		n //= 10
#	return(digits[::-1])
#	
#print(getDigits(1234))
#
#def doesSatisfy(number):
##	numberString = str(number)
#	theSum = 0
##	for i in numberString:
#	for i in getDigits(number):
##		theSum += factorial(int(i))
##		theSum += factorialsDictionary[int(i)]
#		theSum += factorialsDictionary[i]
#		if theSum > number:
#			return False
#	return theSum == number

#def getDigits(n):
#	digits = []
#	while n != 0:	
#		digits.append(n % 10)
#		n //= 10
#	return(digits[::-1])
#	
#print(getDigits(1234))

def doesSatisfy(number):
	temp = number
	theSum = 0
	while temp != 0:
		theSum += factorialsDictionary[temp % 10]
		temp //= 10
		if theSum > number:
			return False
	return theSum == number

for i in range(10, 10**7):
	if doesSatisfy(i):
		print(i)
	
