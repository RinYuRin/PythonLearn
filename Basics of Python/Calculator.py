x = float(input("1st number: "))
z = input("Operator: ")
y = float(input("2nd number: "))

if z == "+":
	print(x + y)
	
elif z == "-":
	print(x - y)
	
elif z == "*":
	print(x * y)

elif z == "/":
	print(x / y)

elif z == "**":
	print(x ** y)
	
else:
	print("Invalid Syntax")