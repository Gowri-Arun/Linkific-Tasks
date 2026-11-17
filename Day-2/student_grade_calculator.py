
def calculate_percentage(marks):
    return sum(marks) / len(marks)

def find_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

print("Student Grade Calculator")

name = input("Enter student name: ")

subjects = ["Maths", "Science", "English", "Computer", "Physics"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input("Enter marks for " + subject + ": "))

            if mark >= 0 and mark <= 100:
                marks.append(mark)
                break
            else:
                print("Marks should be between 0 and 100")

        except ValueError:
            print("Please enter a valid number")

total = sum(marks)
percentage = calculate_percentage(marks)
grade = find_grade(percentage)

passed = True

for mark in marks:
    if mark < 40:
        passed = False

if not passed:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")
