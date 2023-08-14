class Car:
    def __init__(self, make, model, year):
        self._make = make  # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._year = year  # Encapsulated attribute
        self._fuel = 0  # Encapsulated attribute for fuel level

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

    def add_fuel(self, amount):
        if amount > 0:
            self._fuel += amount
            print(f"Added {amount} units of fuel")

    def drive(self, distance):
        fuel_needed = distance / 10  # Assuming 10 units of fuel per unit distance
        if self._fuel >= fuel_needed:
            self._fuel -= fuel_needed
            print(f"Driving {distance} units")
        else:
            print("Not enough fuel to drive")

    def get_fuel_level(self):
        return self._fuel


# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Using encapsulated methods to interact with the object
my_car.start_engine()
my_car.add_fuel(50)
my_car.drive(200)
my_car.stop_engine()

print("Fuel level:", my_car.get_fuel_level())
