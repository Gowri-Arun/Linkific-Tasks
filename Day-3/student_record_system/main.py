from student_manager import add_student, delete_student, find_student, load_students, save_students, update_student
def get_student_details():
    name = input("Enter name: ").strip()
    if name == "" or "|" in name:
        print("Enter a valid name.")
        return None
    try:
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Age must be a whole number and marks must be a number.")
        return None
    if age <= 0 or marks < 0 or marks > 100:
        print("Age must be positive and marks must be between 0 and 100.")
        return None
    return name, str(age), str(marks)

def show_student(student):
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])


def main():
    students = load_students()
    menu_choices = {"1", "2", "3", "4", "5", "6"}

    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice not in menu_choices:
            print("Invalid choice. Please select 1 to 6.")
        elif choice == "1":
            student_id = input("Enter student ID: ").strip()
            if student_id == "" or "|" in student_id:
                print("Enter a valid student ID.")
                continue

            details = get_student_details()
            if details is not None:
                name, age, marks = details
                if add_student(students, student_id, name, age, marks):
                    print("Student added successfully.")
                else:
                    print("Student ID already exists.")
        elif choice == "2":
            if len(students) == 0:
                print("No student records found.")
            else:
                for student in students:
                    print()
                    show_student(student)
        elif choice == "3":
            student_id = input("Enter student ID to search: ").strip()
            student = find_student(students, student_id)
            if student is None:
                print("Student not found.")
            else:
                show_student(student)
        elif choice == "4":
            student_id = input("Enter student ID to update: ").strip()
            student = find_student(students, student_id)
            if student is None:
                print("Student not found.")
            else:
                details = get_student_details()
                if details is not None:
                    name, age, marks = details
                    update_student(student, name, age, marks)
                    save_students(students)
                    print("Student updated successfully.")
        elif choice == "5":
            student_id = input("Enter student ID to delete: ").strip()
            student = find_student(students, student_id)
            if student is None:
                print("Student not found.")
            else:
                delete_student(students, student)
                print("Student deleted successfully.")
        else:
            print("Goodbye!")
            break


main()
