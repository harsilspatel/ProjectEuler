def triangle(n):
	return n*(n+1)//2
	
def pentagonal(n):
	return n*(3*n-1)//2

def hexagonal(n):
	return n*(2*n-1)
	
hexagonalList = []
hexagonalList.append(hexagonal(1))
pentagonalNumber = pentagonal(1)
i = 1
j = 1
for _ in range(10**7):
	j += 1
	while pentagonalNumber < hexagonalList[-1]:
		i += 1
		pentagonalNumber = pentagonal(i)

	if pentagonalNumber == hexagonalList[-1]:
		print(pentagonalNumber)
	
	hexagonalList.append(hexagonal(j))
