count = 0

for power in range(1, 30): #Randomly trying upper bound
	digits = 0
	i = 0
	while digits <= power:
		i += 1
		product = i ** power
		digits = len(str(product))
		if power == digits:
			print(i, power, product)
			count += 1

print(count)