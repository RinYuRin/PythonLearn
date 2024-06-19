Math = int(input("Your Grade in Math: "))
English = int(input("Your Grade in English: "))
Filipino = int(input("Your Grade in Filipino: "))
Science = int(input("Your Grade in Science: "))

#Formula
Total_Grade = (Math + English + Filipino +Science) / 4

print("Average:",int(Total_Grade))
print("\n")

if Total_Grade >= 75:
	print("Congratulations!! You've Passed!!")

else:
	print("What a pity *sighs* You've Failed!")
