theSum = 1

for i in range(3, 1001+1, 2):
	square = i**2
	theSum += square + square-(i-1) + square-(i-1)*2 + square-(i-1)*3

print(theSum)