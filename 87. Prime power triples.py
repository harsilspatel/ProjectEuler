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
	
n = 50*(10**6)
#n = 50
squares = []
cubes = []
fourths = []
for i in eratosthenesSieve(int(n**(1/2)) + 1):
	squares.append(i**2)
	cubes.append(i**3)
	fourths.append(i**4)

numbers = []
for i in squares:
	for j in cubes:
		for k in fourths:
			if i + j + k <= n:
				numbers.append(i + j + k)
			else:
				break

print(len(set(numbers)))

