#n = 1000
#squaresDict = {0:0}
#for i in range(1,n+1):
#	squaresDict[i] = i**2
#pythagoreanTriplets = []

#for x in range(n+1):
#	for y in range(x+1, n+1):
#		for z in range(y+1, n+1):
#			if x + y + z > 1000:
#				break
#			if squaresDict[z] == squaresDict[x] + squaresDict[y]:
#				print(x, y, z)
#			if squaresDict[z] > squaresDict[x] + squaresDict[y]:
#				break
def generateTriplets(n):
	squaresDict = {i:i**2 for i in range(n+2)}
	triplets = []
	for x in range(1, n+1):
		y = x + 1
		z = y + 1
		xyResult = squaresDict[x] + squaresDict[y]
		while z <= n:
			while z <= n and squaresDict[z] < xyResult:
				z += 1
			
			if z <= n and squaresDict[z] == xyResult:
	#			print(x, y, z)
				triplets.append((x, y, z))
			
			y += 1
			xyResult = squaresDict[x] + squaresDict[y]
			
	return triplets

frequency = {}
for triplet in generateTriplets(1000):
	result = sum(triplet)
	if result > 1000:
		continue
	if result in frequency:
		frequency[result] += 1
	else:
		frequency[result] = 1

print(max(frequency.values()))
print(frequency)