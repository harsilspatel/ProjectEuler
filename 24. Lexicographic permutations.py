def factorial(n):
	product = 1
	for i in range(1, n+1):
		product *= i
	return product

def nthPermutation(n, array):
	array = sorted(array)
	thePermutation = ''
	
	while n != 0:
		permuteAllExceptOne = factorial((len(array)-1))
		nRemainder = n % permuteAllExceptOne
		if nRemainder: fixedItemIndex = n // permuteAllExceptOne
		else:
			fixedItemIndex = (n // permuteAllExceptOne) - 1
			array = sorted(array)[::-1]
		fixedItem = array[fixedItemIndex]
		thePermutation += str(fixedItem)
		print(n, permuteAllExceptOne, array, thePermutation)
		array.remove(fixedItem)
		n = nRemainder
		
	
	for i in array:
		thePermutation += str(i)
	
	return thePermutation

print(nthPermutation(1000000, [i for i in range(10)]))