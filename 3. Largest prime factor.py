theNumber = 600851475143
#theNumber = 10503

def divideIfMultiple(n, x):
	hasDivided = False
	while True:
		if n % x == 0:
			hasDivided = True
			n //= x
		else: break
	return (n, hasDivided)

def factorize(n):
	primeFactors = []
	(n, isFactor) = divideIfMultiple(n, 2)
	if isFactor: primeFactors.append(2)
	
	for divisor in range(3, int(n//2) + 1, 2):
		if divisor > n: break
		(n, isFactor) = divideIfMultiple(n, divisor)
		if isFactor:
			primeFactors.append(divisor)
#			print(n, *primeFactors)
		
	if n != 1: primeFactors.append(n)	
	return (primeFactors) 
	
print(factorize(theNumber))