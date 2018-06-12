sumsOfFirstN = {1:1}
def sumOfFirst(n):
#	if n in sumsOfFirstN:
#		return sumsOfFirstN[n]
	return (n)*(n+1)//2

upperLimit = 2*(10**6 + 5)
closest = 1.5*(10**6)
lastJ = 1
for i in range(1, upperLimit):
	for j in range(1, upperLimit):
		rectangles = sumOfFirst(i) * sumOfFirst(j)
		if rectangles > upperLimit:
			break
		if rectangles > closest:
			closest = rectangles
			print(i,j, closest)
		# The last printed line has the dimensions as it is the closest one