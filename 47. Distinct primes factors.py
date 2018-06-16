import functools

@functools.lru_cache(maxsize = None)
def factors(n):
	factorsList = [1, n]
	hasAppended = False

	while n % 2 == 0:
		n //= 2
		factorsList.append(2)
		hasAppended = True
	
	if not hasAppended:
		for i in range(3, n + 1, 2):
			while n % i == 0:
				n //= i
				factorsList.append(i)
				hasAppended = True
			
			if hasAppended:
				break
	
	if hasAppended and n != 1:
		reducedFactors = factors(n)
		reducedFactors.remove(n)
		factorsList += reducedFactors

	return list(set(factorsList))

#def allUnique(array):
#	for k in range(len(array)):
#		for l in range(k+1, len(array)):
#			if array[k] == array[l]:
#				return False
#	return True
				

i = 11
consecutivePrimes = 2
while True:
	i += 1
	print(i, factors(i))
	
	if all(len(factors(i+j)) == consecutivePrimes+2 for j in range(consecutivePrimes)): #Assuming no consecutive will have same number of primes
		print([i+j for j in range(consecutivePrimes)])
		break
		
#	if allUnique([factors(i+j) for j in range(consecutivePrimes)]):
#		print([i+j for j in range(consecutivePrimes)])
##		pass
#		break
	
	

#def generateFactors(n):
#	factors = []
#	for i in range(1, int(n**(1/2)) + 1):
#		if n % i == 0:
#			factors.append(i)
#			factors.append(n//i)
#	return list(set(factors))
#	
#print(generateFactors(92))