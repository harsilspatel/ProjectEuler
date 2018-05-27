import itertools

allCombinations = list(itertools.permutations(range(10)))
allCombinations = allCombinations[362880:] #Removing all numbers starting with zero

allCombinations = [i for i in allCombinations if ((10*i[7] + i[8] - 5*i[9]) % 17 == 0)] #17
allCombinations = [i for i in allCombinations if ((10*i[6] + i[7] + 4*i[8]) % 13 == 0)] #13
allCombinations = [i for i in allCombinations if (i[5] - i[6] + i[7]) % 11 == 0] #11
allCombinations = [i for i in allCombinations if (((10*i[4] + i[5] - 2*i[6]) % 7 == 0))] #7
allCombinations = [i for i in allCombinations if (i[5] % 5 == 0)] #5
allCombinations = [i for i in allCombinations if (sum(i[2:5]) % 3 == 0)] #3
allCombinations = [i for i in allCombinations if (i[3] % 2 == 0)] #2

requiredNumbers = [int(''.join(map(str, i))) for i in allCombinations]

print((requiredNumbers))
print(sum(requiredNumbers))

#print((allCombinations]))

'''
i = 0
while i < len(allCombinations[:10**5]):
	if allCombinations[i][3] % 2 != 0:
		allCombinations.remove(allCombinations[i])
		continue
	i += 1

print(len(allCombinations))

'''
#def multiples(n, startingFrom, upto):
#	return [n*i for i in range(startingFrom//n + 1, upto//n + 1)]
#
#seventeens = multiples(17, 100, 1000)
#thirteens = multiples(13, 100, 1000)
#elevens = multiples(11, 100, 1000)
#sevens = multiples(7, 100, 1000)
#
#i = 0
#while i < len(sevens):
#	if int(str(sevens[i])[1]) % 5 != 0:
#		sevens.remove(sevens[i])
#		continue
#	i += 1
#	
#print(len(sevens))
#
#i = 0
#sevenString = list(map(str, sevens))
#while i < len(thirteens):
#	for j in sevenString:
#		if i != j[:2]
#		continue
#	i += 1 
	
	
	
	
	
	