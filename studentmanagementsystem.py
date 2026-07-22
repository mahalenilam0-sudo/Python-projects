import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        return []
    except json.JSONDecodeError:
        print("Warning: The saved student data file is corrupted. Starting with an empty list.")
        return []


def save_students(students):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)


def find_student(students, search_value):
    search_value = search_value.strip().lower()

    for student in students:
        if student["name"].lower() == search_value or student["roll_number"] == search_value:
            return student

    return None


def add_student(students):
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    if not name or not roll_number:
        print("Name and roll number cannot be empty.")
        return

    if any(student["roll_number"] == roll_number for student in students):
        print("A student with this roll number already exists.")
        return

    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks entered.")
        return

    student = {
        "name": name.title(),
        "roll_number": roll_number,
        "marks": marks,
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\nStudent List")
    for student in students:
        print(f"Name: {student['name']} | Roll Number: {student['roll_number']} | Marks: {student['marks']}")


def search_student(students):
    search_value = input("Enter student name or roll number to search: ")
    student = find_student(students, search_value)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found")
    print(f"Name: {student['name']}")
    print(f"Roll Number: {student['roll_number']}")
    print(f"Marks: {student['marks']}")


def update_student(students):
    search_value = input("Enter student name or roll number to update: ")
    student = find_student(students, search_value)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent found. Enter new values (press Enter to keep current values).")

    new_name = input(f"New name [{student['name']}]: ").strip()
    new_roll_number = input(f"New roll number [{student['roll_number']}]: ").strip()

    try:
        new_marks = input(f"New marks [{student['marks']}]: ").strip()
        new_marks = float(new_marks) if new_marks else student["marks"]
    except ValueError:
        print("Invalid marks entered. Update cancelled.")
        return

    if new_name:
        student["name"] = new_name.title()
    if new_roll_number:
        student["roll_number"] = new_roll_number
    student["marks"] = new_marks

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    delete_value = input("Enter student name or roll number to delete: ")
    student = find_student(students, delete_value)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print("Student deleted successfully.")


students = load_students()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        update_student(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")