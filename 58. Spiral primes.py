#def isPrime(n):
#    # Assuming inputs are non-even numbers
#	for i in range(3, int(n**(1/2)) + 1, 2):
#		if n % i == 0:
#			return False
#	return True

def eratosthenesSieve(n):
	primesDictionary = {i:True for i in range(2, n+1)}
	rootN = n**(1/2)
	for i in range(2, int(rootN) + 1):
		if primesDictionary[i]:
			j = i**2
			while j <= n:
				primesDictionary[j] = False
				j += i
			
	return primesDictionary

primeNumbers = eratosthenesSieve(10**7)

theSum = 1
totalNumbers = 4
primes = 3
i = 3
while primes/totalNumbers > 0.20:
	i += 2
	square = i**2
	for x in [square-(i-1), square-(i-1)*2, square-(i-1)*3]:
		if primeNumbers[x]:
			primes += 1
	totalNumbers += 3
#	print(i, primes, totalNumbers, primes/totalNumbers)

print(i+2)