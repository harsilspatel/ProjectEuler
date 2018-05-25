def isPandigital(numberString):
	return '0' not in numberString and len((numberString)) == len(set((numberString))) and len((numberString)) == 9

# Now, 100*100 = 10,000 which has 11 digits so multiplication of 
upperBound = 10**4
count = 0
product =[]
lastJ = upperBound
for i in range(upperBound):
	for j in range(i+1, lastJ):
		result = i*j
		string = str(i) + str(j) + str(result)
		if len(string) > 9:
			break
		if isPandigital(string):
			count += 1
			product.append(result)
			print(i,j,result)
		lastJ = j
print(count)
print(sum(set(product)))