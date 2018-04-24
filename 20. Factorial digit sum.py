product = 1

for i in range(1, 101):
	while i % 5 == 0:
#		print(i)
		i //= 5
		product //= 2
	product *= i
print(product)
print(sum(list(map(int, list(str(product))))))