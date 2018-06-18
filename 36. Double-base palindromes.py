def binary(number):
	if number == 0:
		return 0
	binaryString = ''
	while number != 0:
		binaryString += str(number % 2)
		number //= 2
	return int(binaryString[::-1])

palindromes = [i for i in range(10**6) if str(i) == str(i)[::-1]]

palindromesFiltered = [i for i in palindromes if str(binary(i)) == str(binary(i))[::-1]]

print(palindromesFiltered)
print(sum(palindromesFiltered))
