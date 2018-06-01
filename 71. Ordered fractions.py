def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y
		
	lcm = greater
	
	while (True):
		if (lcm % x == 0 and lcm % y == 0):
			break
		lcm += greater
	return lcm

upperBound = 3/7
lowerBound = 2/5
count = 0
lastJ = 1
theAnswer = tuple
for i in range(1, 10**6+1):
	for j in range(lastJ, i):
		if j/i < upperBound:
			if j/i > lowerBound:
				lowerBound = j/i
				theAnswer = (j, i, lowerBound)
				count += 1
		else:
			lastJ = j
			break
			
print(count)
print(theAnswer)
hcf = theAnswer[0]*theAnswer[1]//lcm(theAnswer[0], theAnswer[1])
print(hcf)
print('Asnwer:', theAnswer[0]//hcf, theAnswer[1]//hcf)