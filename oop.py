# Parent class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute
        self.__price = price  # Private attribute (Encapsulation)

    def get_price(self):  # Getter for private attribute
        return self.__price

    def set_price(self, new_price):  # Setter for private attribute
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def info(self):
        return f"{self.brand} {self.model}, Price: ${self.__price}"

# Child class (inherits from Smartphone)
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels, battery_life):
        super().__init__(brand, model, price)  # Call parent constructor
        self.camera_megapixels = camera_megapixels  # Additional attribute
        self.battery_life = battery_life  # Additional attribute

    # Overriding the info method (Polymorphism)
    def info(self):
        return f"{self.brand} {self.model} | {self.camera_megapixels}MP Camera | {self.battery_life} hrs Battery | Price: ${self.get_price()}"

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera...")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 799)
phone2 = SmartPhonePro("Apple", "iPhone 14 Pro", 1099, 48, 20)

# Using methods
print(phone1.info())  # Samsung Galaxy S21, Price: $799
phone1.call("+123456789")

print(phone2.info())  # Apple iPhone 14 Pro | 48MP Camera | 20 hrs Battery | Price: $1099
phone2.take_photo()  # Taking a photo with 48MP camera...

# Using encapsulation (getter & setter)
print("Old Price:", phone1.get_price())  # 799
phone1.set_price(750)  # Updating price
print("New Price:", phone1.get_price())  # 750



# question 2

# Parent class (Base)
class Entity:
    def move(self):
        pass  # Abstract move method

# Animal classes
class Dog(Entity):
    def move(self):
        print("🐕 Running on four legs!")

class Bird(Entity):
    def move(self):
        print("🐦 Flying in the sky!")

class Snake(Entity):
    def move(self):
        print("🐍 Slithering on the ground!")

# Vehicle classes
class Car(Entity):
    def move(self):
        print("🚗 Driving on the road!")

class Boat(Entity):
    def move(self):
        print("⛵ Sailing on the water!")

class Plane(Entity):
    def move(self):
        print("✈️ Flying in the air!")

# Function to demonstrate polymorphism
def action(entity):
    entity.move()

# Creating objects
entities = [Dog(), Bird(), Snake(), Car(), Boat(), Plane()]

# Calling move() polymorphically
for e in entities:
    action(e)
