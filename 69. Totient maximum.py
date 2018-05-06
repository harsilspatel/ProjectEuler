#from functools import lru_cache
#
#def primeFactors(n):
#	if n == 1:
#		return []
#	isReduced = False
#	theList = []
#	nCopy = n
#	
#	while n % 2 == 0:
#		n //= 2
#		theList.append(2)
#		isReduced = True
#
#	i = 1
#	while (n != 1) and (i < nCopy//2) and (not isReduced):
#		i += 2
#		while n % i == 0:
#				n //= i
#				theList.append(i)
#				isReduced = True
#	
#	if isReduced:
#		theList += primeFactors(n)
#	
#	if len(theList) == 0:
#		return [n]
#	
#	return list(set(theList))
#
#def totient(n):
#	product = n
#	for i in primeFactors(n):
#		product *= (i - 1)/i
#	return product
#	
##There is no chance that prime number will be the required answer
##Because phi(somePrime) = somePrime-1, so ratio is gonna be tending to 1.

def eratosthenesSieve(n):
	primesDictionary = {i:True for i in range(2, n+1)}
	rootN = n**(1/2)
	for i in range(2, int(rootN) + 1):
		if primesDictionary[i]:
			j = i**2
			while j <= n:
				primesDictionary[j] = False
				j += i
			
	return [i for i in primesDictionary if primesDictionary[i]]

##Marking prime numbers as done so we don't have to iterate thru them
#n = 10**6
#numbersDone = {i:False for i in range(2, n+1)}
#for i in eratosthenesSieve(n+1):
#	numbersDone[i] = True
#	
#maxRatio = 1
#maxN = 1
#for i in range(2, n+1):
#	print(i)
#	if not (numbersDone[i]):
#		ratio = i/totient(i)
#		if ratio > maxRatio:
#			maxRatio = ratio
#			maxN = i
#			print(i, maxRatio)
#


#phi(n) = n*products(1 - (1/prime))
#n/phi(n) = products(p/p-1)
#ratio will be greater when the number is product of primes, because the more the primes of our n -- the more products and thus more ratio
product = 1
for i in eratosthenesSieve(100):
	product *= i
		if product > 10**7:
		product //= i
		break
print(product)
	
	
	