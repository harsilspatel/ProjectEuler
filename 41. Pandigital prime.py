import itertools


def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**(1/2)) + 1, 2):
		if n % i == 0:
			return False
	return True

for i in range(9, 1, -1):
	permutations = list(itertools.permutations(list(range(1, i))))

	for j in permutations[::-1]:
		number = int(''.join(map(str, j)))
		if isPrime(number):
			print(number)
			break
