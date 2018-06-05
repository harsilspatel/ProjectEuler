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
	
primes = [i for i in eratosthenesSieve(10**4) if i > 1000]

for i in range(len(primes)):
	for j in range(len(primes) - 1, i, -1):
		if set(str(primes[i])) != set(str(primes[j])):
			continue
		result = (primes[i] + primes[j]) // 2
		if set(str(primes[j])) == set(str(result)) and result in primes:
			print(primes[i], result, primes[j])
	