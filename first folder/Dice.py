import random

def roll_dice():
    return random.randint(1, 6)

choice = input("Roll the dice? (yes/no): ")

if choice.lower() == "yes":
    print("You rolled:", roll_dice())
