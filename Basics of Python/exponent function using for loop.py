def power(base, exponent):
	result = 1
	
	for index in range(exponent):
		result = result * base
		
	return result
		
print(power(2, 4))