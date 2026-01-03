score = 0

print("Welcome to the Quiz")

q1 = input("1) What is the capital of India? ")
if q1.lower() == "delhi":
    score += 1

q2 = input("2) What is 5 + 3? ")
if q2 == "8":
    score += 1

q3 = input("3) Which language are we using? ")
if q3.lower() == "english":
    score += 1

q4 = input("4)who is the president of the India? ")
if q4.lower() == "droupadi murmu":
    score += 1

q5 = input("5) In which state of India is going to the dust - free city in 2030? ")
if q5.lower() == "Gujarat":
    score += 1

print("Your score is:", score, "/ 5")