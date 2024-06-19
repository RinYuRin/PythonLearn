#def welcome(name):
#	print("welcome" + name)
#	
#welcome(" Aldrin")

#def your_name(name):
#	print("hello " + name)

#your_name("Aldrin")

#def cube(num):
#	
#	return num*num*num
#	
#print(cube(3))

def max_num(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >=num3:
		return num2
	else:
		return num3
		
print(max_num(4, 2, 3))