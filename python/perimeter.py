print("Perimeter Calculator")

print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    side = float(input("Enter side: "))
    print("Perimeter =", 4 * side)

elif choice == "2":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Perimeter =", 2 * (l + b))

elif choice == "3":
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    print("Perimeter =", a + b + c)

elif choice == "4":
    r = float(input("Enter radius: "))
    print("Perimeter =", 2 * (22/7) * r)

else:
    print("Invalid choice")
    print("Invalid choice! Please enter 1, 2, 3, or 4.")