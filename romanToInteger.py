def romanToInt(roman):
	value = {
		'M': 1000,
		'D': 500,
		'C': 100,
		'L': 50,
		'X': 10,
		'V': 5,
		'I': 1
	}

	div = 0
	number = 0

	n = len(roman)
	for i in range(n-1, -1, -1):
		if value[roman[i]] >= div:
			number += value[roman[i]]
		else:
			number -= value[roman[i]]
		div = value[roman[i]]
	print("The integer is:", number)


romanToInt(input('Enter a Roman number: '))
