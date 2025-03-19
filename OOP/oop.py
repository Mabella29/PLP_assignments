# Base class (Smartphone)
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.power_status = False  

    def turn_on(self):
        if not self.power_status:
            self.power_status = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def turn_off(self):
        if self.power_status:
            self.power_status = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")


    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Power Status: {'ON' if self.power_status else 'OFF'}")

class PremiumSmartphone(Smartphone):
    def __init__(self, brand, model, storage, waterproof, foldable):
        super().__init__(brand, model, storage)
        self.waterproof = waterproof
        self.foldable = foldable

    def display_details(self):  
        super().display_details()
        print(f"Waterproof: {'Yes' if self.waterproof else 'No'}")
        print(f"Foldable: {'Yes' if self.foldable else 'No'}")


phone1 = Smartphone("Apple", "iPhone 15", 85)
phone2 = PremiumSmartphone("Samsung", "Galaxy Z Fold", 256, 90, True)


phone1.turn_on()
phone1.display_details()

phone2.turn_on()
phone2.display_details()

        
       

# Task 2

# Base class: Animal
class Animal:
    def move(self):
        pass 


class Dog(Animal):
    def move(self):
        print("The dog is running")


class Bird(Animal):
    def move(self):
        print("The bird is flying")


class Fish(Animal):
    def move(self):
        print("The fish is swimming")

dog = Dog()
bird = Bird()
fish = Fish()

# polymorphism
animals = [dog, bird, fish]
for animal in animals:
    animal.move()