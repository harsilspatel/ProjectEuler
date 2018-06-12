factorialsDictionary = {0:1}

def factorial(n):
	if n in factorialsDictionary:
		return factorialsDictionary[n]
	else:
		product = factorial(n-1)*n
		factorialsDictionary[n] = product
		return product

def combination(n, r):
	return factorial(n)//(factorial(r) * factorial(abs(n-r)))

print(sum([1 for i in range(1, 101) for j in range(1, i) if combination(i, j) > 10**6]))
#print(factorialsDictionary)