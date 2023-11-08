a = int(input("The first number: "))
b = int(input("The second number: "))
choice = input("Enter your choice (A, S, M, D, Mod): ")
if choice == 'A':
    result = a + b
    print(f"The result of addition is: {result}")
elif choice == 'S':
    result = a - b
    print(f"The result of subtraction is: {result}")
elif choice == 'M':
    result = a * b
    print(f"The result of multiplication is: {result}")  
elif choice == 'D':
    if b == 0:
        print("Division by zero is not allowed!")
    else:
        result = a / b
        print(f"The result of division is: {result}")
elif choice == 'Mod':
    if b == 0:
        print("Modulus by zero is not allowed!")
    else:
        result = a % b
        print(f"The result of modulus is: {result}")
else:
    print("Invalid choice")
