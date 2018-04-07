fibonacciSeries = [0, 1, 1]

def fibonacci(n):
	if n < 3:
		return fibonacciSeries[2]
	elif n < len(fibonacciSeries):
		return fibonacciSeries[n]
	else:
		fibonacciSeries.append(fibonacci(n - 1) + fibonacci(n - 2))
		return fibonacciSeries[n]

sumOfEvenFibonacci = 0
i = 0
while True:
	i += 3
	theNumber = fibonacci(i)
	if theNumber > 4000000: break
#	print(theNumber)
	sumOfEvenFibonacci += theNumber


print(sumOfEvenFibonacci)
