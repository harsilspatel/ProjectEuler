fibonacciSeries = [0, 1, 1]

def fibonacci(n):
	if n < 3:
		return fibonacciSeries[2]
	elif n < len(fibonacciSeries):
		return fibonacciSeries[n]
	else:
		fibonacciSeries.append(fibonacci(n - 1) + fibonacci(n - 2))
		return fibonacciSeries[n]

i = 0
while len(list(str(fibonacci(i)))) < 1000:
	i += 1

print(fibonacci(i))

print(i)