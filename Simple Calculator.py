#Simple Calculator

while True:

 a1 = float(input("Enter first number \t"))
 a2 = float(input("Enter second number\t"))

 command = input("Enter the operation"
                "\n 1. Addition :+ "
                "\n 2. Subtraction : - "
                "\n 3. Division : / "
                "\n 4. Multiplication : X "
                "\n 5. Find Modulus : % "
                "\n")

 if command == "1": print("Result:\t", a1 + a2 )
 elif command == "2": print("Result:\t", a1 - a2 )
 elif command == "3":
    if a2 != 0:
        print("Result:\t", a1/a2)
    else:
        print("Error: Cannot be divide by zero")
 elif command == "4":print("Result:\t", a1 * a2 )
 elif command == "5": print("Result:\t", a1 % a2 )
 else: print("Invalid operation, please enter any other given operation from the list above.")

 again = input("Do you want to continue? (yes/no) : \t")
 if again.lower() != "yes" :
    print("Thank you for using calculator!")
    breakpoint()
