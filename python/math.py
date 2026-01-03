print("Simple Calculator")
print("1 = Multiplication")
print("2 = Addition")
print("3 = Subtraction")
print("4 = Division")

choice = int(input("Enter your choice (1, 2, 3, or 4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if choice == 1:
    result = num1 * num2
    print("Result (Multiplication):", result)
elif choice == 2:
    result = num1 + num2
    print("Result (Addition):", result)
elif choice == 3:
    result = num3 - num4
    print("Result (Subtraction):", result)
elif choice == 4:
    if num4 != 0:
        result = num3 / num4
        print("Result (Division):", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")
