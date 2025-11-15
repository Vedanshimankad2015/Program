number = int(input("Enter Number:"))
print("table of",number)
for i in range(1,11):
    mul=number*i
    print(number,"* %d =%d"%(i,mul))