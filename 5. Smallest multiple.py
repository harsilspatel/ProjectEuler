import functools

def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y
		
	lcm = greater
	
	while (True):
		if (lcm % x == 0 and lcm % y == 0):
			break
		lcm += greater
	return lcm
	
print(functools.reduce(lcm, range(1,21)))
