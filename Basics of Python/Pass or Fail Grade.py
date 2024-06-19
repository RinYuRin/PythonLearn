Quiz = int(input("Your Quiz Grade: "))
Ass = int(input("Your Assignment Grade: "))
Class_standing = int(input("Your Class Grade: "))
Project = int(input("Your Project Grade: "))
Major_exam = int(input("Your Exam Grade: "))
quiz_total = 0.15
ass_total = 0.15
class_total = 0.10
project = 0.40
exam_total = 0.20


# Formula
total = (Quiz + Ass + Class_standing + Project + Major_exam) /5

quiz_score =  Quiz * quiz_total 
ass_score = Ass * ass_total
class_score = Class_standing * class_total
project_score = Project * project
exam_score = Major_exam * exam_total

print("your quiz grade: ", quiz_score) 
print("your assignment grade: ", ass_score)
print("your class grade: ", class_score)
print("your project grade: ", project_score)
print("your exam grade: ", exam_score)
print("Your Total Grade: ", total)

if total >= 75:
	print("Passed")
	
else:
	print("Failed")