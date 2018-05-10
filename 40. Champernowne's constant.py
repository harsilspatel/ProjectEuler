maxTenthPower = 6
ChampernowneString = '0'
i = 0
while len(ChampernowneString) <= 10**maxTenthPower:
	i += 1
	ChampernowneString += str(i)

product = 1
for power in range(maxTenthPower + 1):
	product *= int(ChampernowneString[10**power])

print(product)