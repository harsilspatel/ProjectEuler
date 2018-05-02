def isPrime(n):
#	if int(str(n)[-1]) % 2 == 0:
#		return False
#	if (sum(map(int, list(str(n))))) % 3 == 0:
#		return False
	for i in range(3, int(n**(1/2)) + 1, 2):
		if n % i == 0:
			return False
	return True

def cycle(number):
	numberString = str(number)
	cycleString = numberString[1:] + numberString[:1]
	return int(cycleString)
	
def cyclicNumbers(number):
	digits = len(str(number))
	cyclicNumbersList = [number]
	for _ in range(digits-1):
		cyclicNumbersList.append(cycle(number))
		number = cyclicNumbersList[-1]
	return list(set(cyclicNumbersList))
	
def allPrimes(aList):
	digits = len(str(aList[0])) 
	for i in aList:
		if i not in primes[digits-1].keys() or not primes[digits-1][i]:
			return False
	return True

def hasEven(number):
	evenNumbers = ['0','2','4','6','8']
	for i in str(number):
		if i in evenNumbers:
			return True
	return False

primes = [{2:True},{},{},{},{},{}]
for i in range(3, 10**6, 2):
	if isPrime(i) and not hasEven(i):
		primes[len(str(i))-1][i] = True

print((primes[1]))
#print(allPrimes(cyclicNumbers(primes[1][79].key())))

count = 0
for line in primes:
	for i in line.keys():
		cyclicList = cyclicNumbers(i)
		if allPrimes(cyclicList):
			digits = len(str(cyclicList[0]))
			count += len(set(cyclicList))
			for i in set(cyclicList):
				primes[digits-1][i] = False
			print(*set(cyclicList))

print(count)
			
