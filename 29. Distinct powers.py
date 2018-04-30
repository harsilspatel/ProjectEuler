#shit = []
#for i in range(2, 11):
#	for j in range(2, 11):
#		shit.append(i**j)

print(len(set([i**j for i in range(2, 101) for j in range(2, 101)])))