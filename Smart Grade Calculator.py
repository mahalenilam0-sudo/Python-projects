while True:

 name = input("\nEnter name of the student: \t")
 Roll_No = int(input(("\nEnter Roll Number: \t")))
 percent = float(input("\nEnter percentage of the student: \t"))

 if percent > 100 or percent < 0:
     print("Invalid Marks! Please enter valid marks.")

 else:
     if percent >= 90:
         print("\nGrade A+, Excellent Work!")
     elif percent >= 85:
         print("\nGrade A, Outstanding!")
     elif percent >= 75:
         print("\nGrade B, Good Work.")
     elif percent >= 45:
         print("\nGrade C, Needs Improvement.")

     else:
         print("\nFail :( , Work Hard.")

     again = input("\nDo you want to continue? (yes/no) : \t")
     if again.lower() != "yes":
         print("\nThank you, come again!")
         break