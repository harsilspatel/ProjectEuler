isAllowed = {0:False, 1:True, 2:False, 3:True, 4:False, 5:True, 6:False, 7:True, 8:False, 9:True}

def checkAllOdd(n):
#	while n != 0:
#		if not isAllowed[n % 10]:
#			return False
#		n //= 10
	for i in str(n):
		if not isAllowed[int(i)]:
			return False
	return True

def revereseNumber(n):
	reverse = 0
	while n!= 0:
		reverse *= 10
		reverse += n % 10
		n //= 10
	return reverse

count = 0
for i in range(10, 10**7):
	if i % 10 == 0:
		continue
	reverse = int(str(i)[::-1])
#	iLast = (i % 10)
#	reverseLast = (reverse % 10)
#	if iLast + reverse % 2 == 0 or iLast * reverse % 2 != 0:
#		continue
	theSum = i + reverse
	if checkAllOdd(theSum):
#		print(i)
		count += 1

print(count)