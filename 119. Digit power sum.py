i = 10
count = 0

while count < 30:
	i += 1
	digitSum = sum(map(int, str(i)))
	if digitSum == 1:
		continue
	power = digitSum
	n = 1
	while power < i:
		n += 1
		power *= digitSum
		if power == i:
			print('answer:',count+1, digitSum, n, i)
			count += 1
			break
print(i)