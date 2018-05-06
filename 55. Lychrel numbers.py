checkedNumbers = {}

def isLychrel(number):
	for i in range(50):
		if number in checkedNumbers:
			return checkedNumbers[number]
		theSum = number + int(str(number)[::-1])
#		print(theSum, number)
		if str(theSum) == str(theSum)[::-1]:
			checkedNumbers[number] = False
			return False
		number = theSum
	checkedNumbers[number] = True
	return True

lychrelNumbers = [i for i in range(10**4, 1, -1) if isLychrel(i)]

print(lychrelNumbers)
print(len(lychrelNumbers))			