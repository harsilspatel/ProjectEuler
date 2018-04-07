#import functools
#
#@functools.lru_cache(maxsize = None)
#def factors(n):
#	factorsList = [n]
#	hasAppended = False
#
#	while n % 2 == 0:
#		n //= 2
#		factorsList.append(2)
#		hasAppended = True
#	
#	if not hasAppended:
#		for i in range(3, n//2 + 1, 2):
#			while n % i == 0:
#				n //= i
#				factorsList.append(i)
#				hasAppended = True
#			
#			if hasAppended:
#				break
#	
#	if hasAppended:
#		reducedFactors = factors(n)
#		reducedFactors.remove(n)
#		factorsList += reducedFactors
#
#	return list(set(factorsList))
#	
#answer = factors(2)
##answer.remove(45)
#print(answer)

for i in (3 + 4*i for i in range(20)): print(i, end = ", ")
print()
for i in (3 + 16*i for i in range(20)): print(i, end = ", ")
	