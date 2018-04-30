def equalsFifthPower(number):
	theSum = 0
	for i in str(number):
		theSum += int(i)**5
		if theSum > number:
			return False
	return theSum == number

answers = []
i = 1
while len(answers) < 6: # 6 is random guess, but on doing the math is can be said that 6 is also correct
	i += 1
	if equalsFifthPower(i):
		answers.append(i)

print(answers)
print(sum(answers))