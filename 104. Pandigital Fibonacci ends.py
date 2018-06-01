from functools import lru_cache
import math

@lru_cache(maxsize=4)
def fibonacci(n):
	
		
def isPandigital(numberString):
	return '0' not in numberString and len((numberString)) == len(set((numberString)))
	
i = -1
while True:
	i += 1
	number = fibonacci(i)
	numberString = str(number)
	if isPandigital(numberString[:9]) and isPandigital(numberString[-9:]):
		break
	print(i)
print(i)