#Upgraded version of Smart Grade Calculator

student = []

def calculate_grade(percent):
    if percent >= 90:
        return "A", "Excellent"
    elif percent >= 75:
        return "B", "Good"
    elif percent >= 50:
        return "C", "Needs Improvement"
    else:
        return "Fail", "Work Hard"

while True:
    name = input("\nEnter Student Name: \t")
    subject = input("\nEnter Subject Name: \t")

    try:
        percent = float(input("\nEnter percentage: \t"))
    except ValueError:
        print("Invalid Input! Please enter correct percentage.")


    if percent <0 or percent > 100:
        print("Marks must be between 0 to 100 only.")
        continue

    grade, msg = calculate_grade(percent)

    student.append((name, subject, percent, grade))

    print("\n---Result---")
    print("\nStudent_name:",name)
    print("\nSubject:",subject)
    print("\nPercentage:",percent)
    print("\nGrade:",grade)
    print("\nFeedback",msg)

    again = input("\nAdd another student?(yes/no):")
    if again.lower() != "yes":
        break


#Summery Section
    print("\n====Summery====")

    total = 0
    highest = 0
    top_student = ""

    for s in student:
        total += s[2]

        if s[2] > highest:
            highest = s[2]
            top_student = s[0]

    if len(student) > 0:
        avg = total / len(student)

        print("\nTotal Students:", len(student))
        print("\nAverage Percentage:", round(avg,2))
        print("\nTop Student:", top_student, "with", highest)

    print("\nProgram Ended.")
