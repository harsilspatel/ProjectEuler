#If there is a grid of n*n, we have to choose from a total of 2*n (n verticles + n horizontal) lines to reach the bottom right corner from the top left corner.
#That is 2nCn

n = 20

def factorial(n):
	product = 1
	for i in range(1, n+1):
		product *= i
	return product
print(factorial(2*n)//(factorial(2*n-n)*factorial(n)))