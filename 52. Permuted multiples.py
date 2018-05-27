def hasSameDigits(number, anotherNumber):
	numberString = str(number)
	anotherNumberString = str(anotherNumber)
	return len(numberString) == len(anotherNumberString) and set(numberString) == set(anotherNumberString)

i = 
while True:
	i += 1
	products = []
	if hasSameDigits(i, 2*i) and hasSameDigits(i, 3*i) and hasSameDigits(i, 4*i) and hasSameDigits(i, 5*i) and hasSameDigits(i, 6*i):
		print(i, 2*i, 3*i, 4*i, 5*i, 6*i)
		break