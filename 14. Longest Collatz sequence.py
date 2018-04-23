#collatzList = {1:1}
#def collatzSequence(n, originalNumber):
#	if n in collatzList.keys():
#		collatzList[originalNumber] = collatzList[n] + collatzSequence.counter
#		return collatzList[originalNumber]
#	collatzSequence.counter += 1
##	if n == 1:
##		return collatzSequence.counter
#	if n % 2 == 0: return collatzSequence(n//2, originalNumber)
#	else: return collatzSequence(3*n+1, originalNumber)
#	
#collatzSequence.counter = 0
#
#print(collatzList)
#print(collatzSequence(13, 13))
#print(collatzList)



# stackoverflow
#collatzList = {1: 1}
#def collatz(n):
#	path = [n]
#	while n not in collatzList:
#		if n % 2:
#			n = 3 * n + 1
#		else:
#			n = n // 2
#		path.append(n)
#	for i, m in enumerate(reversed(path)):
#		collatzList[m] = collatzList[n] + i
##	print(path)
#	return collatzList[path[0]]
#
#maxCollatzPath = 0
#maxCollatzNumber = 0
#for i in range(1, 10**7+1):
#	if collatz(i) > maxCollatzPath:
#		maxCollatzPath = collatz(i)
#		maxCollatzNumber = i
#print(maxCollatzNumber, maxCollatzPath)

#collatzList = {1: 1, 2: 2}
#def collatz(n):
#	if n in collatzList:
##		print(n, collatzList[n], type(collatzList[n]))
#		return collatzList[n]
#	else:
#		if n % 2 == 0:
#			print('before', collatzList)
#			lastSum = collatz(n//2)
#			collatzList[n] = lastSum + 1 
#			print('after', collatzList)
#
#		else:
#			lastSum = collatz(3*n+1)
#			collatzList[n] = lastSum + 1
#
#collatz(8)
#print(collatzList)


collatzList = {1: 0}

n = 10**6

def collatz(n):
	if n not in collatzList:
		if n % 2:
			x = 3 * n + 1
		else:
			x = n // 2
		collatzList[n] = collatz(x) + 1
		return collatzList[n]
	else:
		return collatzList[n]	
	
maxCollatzPath = 0
maxCollatzNumber = 0
for i in range(1, n+1):
	if collatz(i) > maxCollatzPath:
		maxCollatzPath = collatz(i)
		maxCollatzNumber = i
print(maxCollatzNumber, maxCollatzPath)