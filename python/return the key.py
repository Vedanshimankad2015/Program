data = {}

# Taking user details
data["name"] = input("Enter your name: ")
data["age"] = input("Enter your age: ")
data["city"] = input("Enter your city: ")
data["class"] = input("Enter your class: ")

# Searching for key
search_key = input("Enter what you want to know (name/age/city/class): ")

if search_key in data:
    print("Value:", data[search_key])
else:
    print("Invalid key")
