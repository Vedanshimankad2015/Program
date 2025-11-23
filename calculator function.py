print("Simple Calculator")
print("1 = Multiplication")
print("2 = Addition")

choice = int(input("Enter your choice (1 or 2): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 * num2
    print("Result (Multiplication):", result)

elif choice == 2:
    result = num1 + num2
    print("Result (Addition):", result)

else:
    print("Invalid choice! Please enter 1 or 2.")
