names = []
for line in open('p022_names.txt'):
	names = line.split(',')

for i in range(len(names)):
	names[i] = names[i][1:len(names[i])-1]

names = sorted(names)

totalSum = 0
for i in range(len(names)):
	totalSum += (i+1)*(sum([(ord(j)-64) for j in names[i]]))

print(totalSum)