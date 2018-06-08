primes = [2, 3, 5, 7]
squares = [i**2 for i in range(1, 10**4)]

def isPrime(n):
    # Assuming inputs are non-even numbers
	for i in range(3, int(n**(1/2)) + 1, 2):
		if n % i == 0:
			return False
	return True

def doesSatisfy(number):
	for j in (primes):
		for k in (squares):
			if number == j + 2*k:
				return True
			if number < j + 2*k:
				break
	return False

i = 9
foundAnswer = False
while not foundAnswer:
	i += 2
	if isPrime(i):
		primes.append(i)
		continue
	else:
		if not doesSatisfy(i):
			foundAnswer = True
			print(i)			
	