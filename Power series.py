x = float(input("Enter the value of x: "))
n = int(input("Enter number of terms (n): "))

print("Power Series:")

term = 1   # x^0
for i in range(n):
    print(term, end=" ")   
    term *= x             