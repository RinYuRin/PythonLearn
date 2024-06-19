x = str(input("Enter a unit you want: [m, km, cm, ft] "))
z = str(input("Enter the unit you want to convert with: [m, km, cm, ft] "))
y = float(input("Enter a value: "))

if x == 'm' and z == 'km':
	new_y = 1000/y
	print("%d m = %d km"%(y, new_y))

elif x == 'km' and z == 'm':
	new_y = 1000*y
	print('%d km = %d m' %(y, new_y))

elif x == 'cm' and z == 'm':
	new_y = y / 100
	print('%d cm = %.2f m' %(y, new_y))

else:
	print("Invalid Unit")
	