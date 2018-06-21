numbers = []
for line in open('p067_triangle.txt'):
	numbers.append(list(map(int, line.split())))


#stackOverflow
#def all_paths(tree, r, c):
#	current = tree[r][c]
#	if r < len(tree) - 1:
#		below_paths = all_paths(tree, r+1, c) + all_paths(tree, r+1, c+1)
#		x = [[current] + path for path in below_paths]
#		return x
#	else:
#		return [[current]]
	
def maxPath(tree):
#	Assuming it is ekdum takka-tak binary tree
	treeCopy = tree[:]
	
	for row in range(len(treeCopy)-1, 0, -1):
		for column in range(len(treeCopy[row])-1):
			treeCopy[row-1][column] += max(treeCopy[row][column], treeCopy[row][column+1])
		
#		for i in treeCopy[:row]:
#			print(*i)
			
	return treeCopy[0][0]
	
print(maxPath(numbers))
			