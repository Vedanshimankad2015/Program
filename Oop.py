
class Car:
    def __init__(self, brand, color):
        self.brand = brand      
        self.color = color

    def start(self):            
        print(f"{self.brand} car started.")

    def show_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Color: {self.color}")


car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

car1.start()
car2.start()

car1.show_details()
car2.show_details()
