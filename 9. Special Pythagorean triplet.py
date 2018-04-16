n = 500
for x in range(n):
	for y in range(x+1, n):
		z = y + 1
		while z*z < x*x + y*y:
			z += 1
		if z*z == x*x + y*y and z <= n:
			if sum([x,y,z]) == 1000:
				print(x,y,z, x*y*z)
					
			