daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#def isLeap(year):
#	if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#		return True
#	return False

def isLeap(year): #https://en.wikipedia.org/wiki/Leap_year#Algorithm
	leap = True
	if year % 4 != 0:
		 leap = False
	elif year % 100 != 0:
		 leap = True
	elif year % 400 != 0:
		 leap = False
	return leap

firstOfMonthCounts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0} # 0 = Monday, 1 = Tuesday...
numberOfDays = 0
for year in range(1901, 2001):
	for month in range(1,13):
		
		firstOfMonthCounts[numberOfDays%7] += 1
		numberOfDays %= 7
		
		numberOfDays += daysOfMonth[month]
		
#		if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#		if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
		if isLeap(year) and month == 2:
			numberOfDays += 1

#		print(numberOfDays)

print(sum(firstOfMonthCounts.values()))
print(firstOfMonthCounts.values())