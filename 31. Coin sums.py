target = 200
denominations = [1,2,5,10,20,50,100,200]

def coinSums(target, denominations):
	ways = [0] * (target + 1)
	ways[0] = 1
	for x in denominations:
		for i in range(x, target + 1):
			ways[i] += ways[i-x]
	return ways[target]
	
print(coinSums(target, denominations))