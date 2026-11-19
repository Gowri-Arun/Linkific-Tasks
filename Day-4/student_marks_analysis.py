import numpy as np

marks = np.array([
    [85, 78, 92],
    [76, 88, 80],
    [90, 91, 89],
    [68, 74, 72],
    [82, 85, 87]
])

student_totals = marks.sum(axis=1)
student_averages = marks.mean(axis=1)
subject_averages = marks.mean(axis=0)
top_student = student_totals.argmax() + 1

print("Marks:\n", marks)
print("\nStudent totals:", student_totals)
print("Student averages:", student_averages)
print("Subject averages:", subject_averages)
print("Highest mark:", marks.max())
print("Lowest mark:", marks.min())
print("Top-performing student: Student", top_student)
