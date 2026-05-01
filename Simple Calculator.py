#Simple Calculator

a1 = int(input("Enter first number \t"))
a2 = int(input("Enter second number\t"))

command = input("Enter the operation"
                "\n 1. Addition"
                "\n 2. Substraction"
                "\n 3. Division"
                "\n 4. Multiplication"
                "\n 5. Find Modulus"
                "\n")

if command == "1": print("Result:\t", a1 + a2 )
elif command == "2": print("Result:\t", a1 - a2 )
elif command == "3": print("Result:\t", a1 / a2 )
elif command == "4": print("Result:\t", a1 * a2 )
elif command == "5": print("Result:\t", a1 % a2 )
else : print("Invalid operation, please enter any other given operation from the list above.")
