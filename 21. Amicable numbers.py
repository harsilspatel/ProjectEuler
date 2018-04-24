def generateFactors(n):
	factors = []
	for i in range(1, int(n**(1/2)) + 1):
		if n % i == 0:
			factors.append(i)
			factors.append(n//i)
	return list(set(factors))

amicableNumbers = []
for i in range(1, 10000):
	sum1 = sum(generateFactors(i)) - i
	sum2 = sum(generateFactors(sum1)) - sum1
	
	if i == sum2 and i != sum1:
		amicableNumbers.append(i)
		print(i, sum1)
		
print(sum(set(amicableNumbers)))