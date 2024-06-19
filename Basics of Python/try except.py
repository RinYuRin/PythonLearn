
try:
	number = int(input("enter a number: "))
except ValueError as error:
	print(error)