#def sumOfFirst(n):
#	return ((n)*(n+1)//2)
#
#def sumOfSquaresOfFirst(n):
#	return ((n)*(n+1)*(2*n+1)//6)
#
#print(sumOfFirst(100)**2 - sumOfSquaresOfFirst(100))


print(sum(i for i in range(1, 101))**2 - sum(i**2 for i in range(1,101)))