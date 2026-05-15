students = []

while True:

    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice:")

    #add student
    if choice == "1":

        name = input("Enter student name: ")

        try:
            marks = float(input("Enter marks: "))
        except ValueError:
            print("Invalid marks!")
            continue

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)

        print("Student added successfully!")

    #view student
    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\nStudent List")

            for s in students:
                print(f"Name:{s['name']} | Marks:{s['marks']}")

    #search student
    elif choice == "3":

        search = input("Enter student name to search: ")

        found = False

        for s in students:

            if s["name"].lower() == search.lower():

                print("\nStudent Found")
                print(f"Name:{s['name']}")
                print(f"Marks:{s['marks']}")

                found = True
                break

        if not found:
            print("Student not found.")

    #delete student
    elif choice == "4":

        delete_name = input("Enter student name to delete: ")

        found = False

        for s in students:
            if s["name"].lower() == delete_name.lower():

                students.remove(s)

                print("Student deleted successfully.")

                found = True
                break

        if not found:
            print("Student not found.")

    #exit
    elif choice == "5":

        print("Exiting program...")
        break


    else:
        print("Invalid choice!")