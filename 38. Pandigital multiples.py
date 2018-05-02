def isPandigital(number):
	productsString = ''
	i = 0
	while len(productsString) < 9:
		i += 1
		productsString += str(number*i)
	if len(set(productsString)) == len(productsString) and len(set(productsString)) == 9:
		return (True, i, productsString)
	return (False, i, productsString)

print(isPandigital(12356))
for i in range(10**6):
	tryResult = isPandigital(i)
	if tryResult[0]:
		print(i, tryResult[1], tryResult[2])
		