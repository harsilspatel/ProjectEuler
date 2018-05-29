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

n = 10**6
#n = 10**3
primes = eratosthenesSieve(n)
prefixSums = [0, primes[0]]
for i in range(2, len(primes) + 1):
	prefixSums.append(prefixSums[i-1] + primes[i-1])

#print(primes[:10])
#print(prefixSums[:10])
consecutivePrimes = 0

for x in range(len(primes)):
	thePrime = primes[x]
	y = 0
	z = consecutivePrimes + 2
	
	if prefixSums[z] - prefixSums[y] > thePrime:
		continue
		
	while z < n:
		while prefixSums[z] - prefixSums[y] < thePrime and z < n:
			z += 1
		
		if z - y <= consecutivePrimes:
			break
		
		if prefixSums[z] - prefixSums[y] == thePrime:
			print(thePrime, z-y)
			consecutivePrimes = z - y
			break
		
		while prefixSums[z] - prefixSums[y] > thePrime and y < z:
			y += 1
	