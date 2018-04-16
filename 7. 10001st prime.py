primeNumbers = [2]

dividend = 3
while len(primeNumbers) < 10001:
	isPrime = True
	for divisor in range(2, int((dividend)**(1/2))+1):
		if (dividend % divisor == 0):
			isPrime = False
			break
		
	if isPrime: primeNumbers.append(dividend)
	dividend += 2
	
#print(len(primeNumbers))
print(primeNumbers[-1])