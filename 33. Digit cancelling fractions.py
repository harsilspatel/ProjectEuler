def intersection(numerator, denominator):
	intersected = [i for i in str(numerator) if i in str(denominator)]
	if len(intersected) == 0:
		return (False, 0)
	else:
		return (True, list(set(intersected)))

for numerator in range(10, 100):
	for denominator in range(numerator+1, 100):
		if numerator * denominator % 100 == 0:
			continue
		result = intersection(numerator, denominator)
		if result[0]:
			for i in result[1]:
				a = list(str(numerator))
				b = list(str(denominator))
#				print(numerator,a, denominator,b, result[1],i)
				(a.remove(i))
				(b.remove(i))
				if b[0] != '0' and numerator/denominator == int(a[0])/int(b[0]):
					print(a[0], b[0])