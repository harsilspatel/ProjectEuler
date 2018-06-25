powerEndings = [
	[0],
	[1],
	[2,4,8,6],
	[3,9,7,1],
	[4,6],
	[5],
	[6],
	[7,9,3,1],
	[8,4,2,6],
	[9,1],
]

def isPossible(base, number):
	baseLastDigit = base % 10
	numberLastDigit = number % 10
	try:
		return powerEndings[baseLastDigit].index(numberLastDigit)
	except ValueError:
		return -1

def sumDigits(number):
	theSum = 0
	while number != 0:
		theSum += number % 10
		number //= 10
	return theSum

i = 10
count = 0

while count < 30:
	i += 1
	digitSum = sumDigits(i)
	
	startingPower = isPossible(digitSum, i)
	
	if startingPower == -1:
		continue
	
	power = digitSum**(startingPower+1)
	multiple = digitSum**len(powerEndings[digitSum%10])
	
	while power <= i:
		if power == i:
			print('answer:',count+1, digitSum, i)
			count += 1
			break
		power *= multiple
		
print(i)