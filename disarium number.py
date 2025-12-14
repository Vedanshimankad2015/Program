num = int(input("Enter a number: "))
temp = num
digits = list(map(int, str(num)))

sum = 0
for i in range(len(digits)):
    sum += digits[i] ** (i + 1)

if sum == num:
    print("Disarium Number")
else:
    print("Not a Disarium Number")
