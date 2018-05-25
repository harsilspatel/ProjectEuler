primesDictionary = {2:True, 3:True}

def isPrime(n):
	if n in primesDictionary:
		return primesDictionary[n]
	if sum([int(i) for i in str(n)]) % 3 == 0:
		primesDictionary[n] = False
		return False
	for i in range(2, int(n**(1/2)) + 1):
		if n % i == 0:
			primesDictionary[n] = False
			return False
	primesDictionary[n] = True
	return True

def isTruncablePrime(number):
	stringNumber = str(number)
	if stringNumber[0] == '1' or stringNumber[0] == '9':
		return False
	if stringNumber[-1] == '1' or stringNumber[-1] == '9':
			return False
	digits = len(stringNumber)
	for i in range(digits):
		temp = (number % (10**(i+1)))
		if not isPrime(temp):
			return False
		temp2 = int(stringNumber[:i+1])
		if not isPrime(temp2):
			return False
	return True
#print(isTruncablePrime(43))

truncablePrimes = []
i = 11
while len(truncablePrimes) != 11:
	if isTruncablePrime(i):
		truncablePrimes.append(i)
	i += 2

print(truncablePrimes)
print(sum(truncablePrimes))