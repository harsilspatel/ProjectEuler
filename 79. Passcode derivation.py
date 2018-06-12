passcodeAttempts = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]

numbersDictionary = {}
for attempt in passcodeAttempts:
	for priority, i in enumerate(str(attempt)): # 0 -> Max priority
		if i in numbersDictionary:
			numbersDictionary[i] += priority
		else:
			numbersDictionary[i] = priority

print(numbersDictionary)
frequencies = sorted(numbersDictionary.values())

passcode = ''
for frequency in frequencies:
	for key in list(numbersDictionary.keys()):
		if numbersDictionary[key] == frequency:
			passcode += key
			numbersDictionary.pop(key, None)

print(int(passcode))