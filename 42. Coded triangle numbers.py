words = open('p042_words.txt').read().split(',')

def wordNumber(word):
	return sum([ord(i)-64 for i in word])

wordNumbers = [wordNumber(word[1:len(word)-1]) for word in words]
print(max(wordNumbers))

def triangle(n):
	return n*(n+1)//2
	
triangleNumbers = [1]
maxWordNumber = max(wordNumbers)
while maxWordNumber > triangleNumbers[-1]:
	triangleNumbers.append(triangle(len(triangleNumbers)+1))
print(triangleNumbers)

print(sum([1 for i in wordNumbers if i in triangleNumbers]))

