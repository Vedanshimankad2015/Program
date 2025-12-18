print("📘 Welcome to My Slam Book 📘")
print("Hi there my names Vedanshi if you want me to know about you fill out these details")
print("-----------------------------")

while True:
    print("\nNew Friend Entry")

    name = input("Your Name: ")
    nickname = input("Your Nickname: ")
    color = input("Favourite Color: ")
    food = input("Favourite Food: ")
    message = input("One Message for Me: ")

    print("\n✨ Slam Book Entry ✨")
    print("--------------------")
    print("Name:", name)
    print("Nickname:", nickname)
    print("Favourite Color:", color)
    print("Favourite Food:", food)
    print("Message:", message)
    print("part-2")
    choice = input("\nAdd another friend? (yes/no): ")
    if choice.lower() != "yes":
        break
    print("\n Slam Book Closed. Thank you!")
    print("-----------------------------")
    name = input("Your Name: ")
    nickname = input("Your Nickname: ")
    color = input("Favourite Color: ")
    food = input("Favourite Food: ")
    message = input("One Message for Me: ")
    print("\n✨ Slam Book Entry ✨")
    print("--------------------")
    print("Name:", name)
    print("Nickname:", nickname)
    print("Favourite Color:", color)
    print("Favourite Food:", food)
    print("Message:", message)

    choice = input("\nAdd another friend? (yes/no): ")
    if choice.lower() != "yes":
        break

print("\n Slam Book Closed. Thank you!")
