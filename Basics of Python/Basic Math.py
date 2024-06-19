# Given
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
num3 = float(input("enter 3rd number: "))

# Formula
ADD = num1 + num2 + num3
SUBTRACT = num3 - num2
MULTIPLY = num1 * num3
DIVIDE = num1 / num2
POW = num3 ** num2

print("\n")
print("Sum of 1st, 2nd, and 3rd number: %f" %ADD)
print("\n")
print("Difference of 3rd and 2nd number: %f" %SUBTRACT)
print("\n")
print("Product of 1st and 3rd number: %f" %MULTIPLY)
print("\n")
print("Quotient of 1st and 2nd number: %f" %DIVIDE)
print("\n")
print("Exponent of 3rd and 2nd number: %f" %POW)