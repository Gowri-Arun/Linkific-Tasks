import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "students.txt")
FIELDS = ("id", "name", "age", "marks")


def load_students():
    students = []

    if not os.path.exists(FILE_NAME):
        return students

    file = open(FILE_NAME, "r")
    for line in file:
        details = line.strip().split("|")
        if len(details) == len(FIELDS):
            student = {
                "id": details[0],
                "name": details[1],
                "age": details[2],
                "marks": details[3]
            }
            students.append(student)
    file.close()

    return students


def save_students(students):
    file = open(FILE_NAME, "w")
    for student in students:
        line = student["id"] + "|" + student["name"] + "|" + student["age"] + "|" + student["marks"] + "\n"
        file.write(line)
    file.close()


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students, student_id, name, age, marks):
    if find_student(students, student_id) is not None:
        return False

    student = {"id": student_id, "name": name, "age": age, "marks": marks}
    students.append(student)
    save_students(students)
    return True


def update_student(student, name, age, marks):
    student["name"] = name
    student["age"] = age
    student["marks"] = marks


def delete_student(students, student):
    students.remove(student)
    save_students(students)
