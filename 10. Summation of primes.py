primeNumbers = [2]

dividend = 3
while primeNumbers[-1] < 2000000:
	isPrime = True
	for divisor in range(2, int((dividend)**(1/2))+1):
		if (dividend % divisor == 0):
			isPrime = False
			break
		
	if isPrime:
		primeNumbers.append(dividend)
		print(dividend)
	dividend += 2
	
#print(len(primeNumbers))
print(sum(primeNumbers) - primeNumbers[-1])