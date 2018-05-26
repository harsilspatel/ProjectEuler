#def isPrime(n):
#	return (True if sum([1 for i in range(2, int(n**(1/2)) + 1) if n % i == 0]) == 0 else False)
primesDict = {}
def isPrime(n):
	if n not in primesDict.keys():
		if n % 2 == 0 and n != 2:
			primesDict[n] = False
			return False
		for i in range(3, int(n**(1/2)) + 1, 2):
			if n % i == 0:
				primesDict[n] = False
				return False
		primesDict[n] = True
		return True
	else:
		return primesDict[n]

primes = [1]
primes += [i for i in range(2, 1000) if isPrime(i)]
possibleSets = []

# 1 + a + b is prime when a + b is odd
for a in range(-2, 1001, 2):
	possibleSets.append((+a, 2))
primes.remove(2)

for b in primes:
	for a in range(+999, -1000, -2): 
		if a + b + 1 > 0:
			possibleSets.append((+a,+b))
		else:
			break
print('Sets', len(possibleSets))

#n = 0
#for a in range(-999, 1001, 2): 
#	for b in primes:
#		possibleSets.append((+a,+b))
##		possibleSets.append((-a,+b))

n = 1
while n < 50:
	n += 1
	for aSet in possibleSets:
		if n**2 + aSet[0]*n + aSet[1] < 0:
			possibleSets.remove(aSet)
	print('Positive', len(possibleSets))


n = 1
while len(possibleSets) != 1:
	n += 1
	for aSet in possibleSets:
		value = n**2 + aSet[0]*n + aSet[1]
		if value < 0 or not isPrime(value):
			possibleSets.remove(aSet)
#		else:
#			if value in primes:
#				continue
#			else:
#				if isPrime(value):
#					primes.append(value)
#				else:
#					possibleSets.remove(aSet)
		
				
	print(len(possibleSets))
	
print(*possibleSets, n)
