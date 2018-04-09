def isPalindrome(n):
	if n == int(''.join(list(str(n))[::-1])): return True
	else: return False

palindromes = []
for i in range(999, 99, -1):
	for j in range(i, 99, -1):
		if isPalindrome(i*j):
			print(i, j, i*j)
			palindromes.append(i*j)
			break
print(max(palindromes))