
name = "Student"
age = 20
cgpa = 9.1
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)

if cgpa >= 9:
    print("Excellent")
elif cgpa >= 7:
    print("Good")
else:
    print("Needs improvement")

subjects = ["Python", "Maths", "English"]

for subject in subjects:
    print(subject)

i = 1
while i <= 5:
    print(i)
    i += 1

def greet(name):
    print("Hello", name)

def average(a, b, c):
    return (a + b + c) / 3

greet(name)

marks = average(80, 90, 85)
print("Average marks:", marks)
