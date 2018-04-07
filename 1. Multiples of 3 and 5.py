def sumOf(x, n):
	return sum(i for i in range(0, n, x))
	
print(sumOf(3, 1000) + sumOf(5, 1000) - sumOf(15, 1000))