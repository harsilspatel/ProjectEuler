def minimal_path_sum(matrix):

	size = len(matrix)
	# calculate minimal sums for bottom row and last column
	# as they don't have any other way to be reached
	for i in reversed(range(0, size - 1)):
		matrix[size - 1][i] += matrix[size - 1][i + 1]
		matrix[i][size - 1] += matrix[i + 1][size - 1]
		
					
	for i in reversed(range(0, size - 1)):
		for j in reversed(range(0, size - 1)):
			for k in matrix:
				print(*k)
			print()
			matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])
#			matrix[j][i] += min(matrix[j + 1][i], matrix[j][i + 1])
			
	

	return matrix[0][0]

matrix = [[131,673,234,103,18], [201,96,342,965,150], [630,803,746,422,111], [537,699,497,121,956], [805,732,524,37,331]]

print(minimal_path_sum(matrix))