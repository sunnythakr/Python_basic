class CoffeeMachine:
    def __init__(self):
        self._water_level = 1000  # Encapsulated attribute for water level (ml)
        self._coffee_level = 500  # Encapsulated attribute for coffee level (g)

    def _check_resources(self, water_needed, coffee_needed):
        if self._water_level < water_needed:
            print("Not enough water")
            return False
        elif self._coffee_level < coffee_needed:
            print("Not enough coffee")
            return False
        return True

    def brew_coffee(self, coffee_type):
        if coffee_type == "espresso":
            water_needed = 50  # ml
            coffee_needed = 10  # g
        elif coffee_type == "latte":
            water_needed = 200  # ml
            coffee_needed = 20  # g
        elif coffee_type == "cappuccino":
            water_needed = 150  # ml
            coffee_needed = 15  # g
        else:
            print("Invalid coffee type")
            return

        if self._check_resources(water_needed, coffee_needed):
            print(f"Brewing a {coffee_type}...")
            self._water_level -= water_needed
            self._coffee_level -= coffee_needed
            print("Enjoy your coffee!")

    def refill_water(self, amount):
        self._water_level += amount
        print(f"Refilled {amount} ml of water")

    def refill_coffee(self, amount):
        self._coffee_level += amount
        print(f"Refilled {amount} g of coffee")

    def display_status(self):
        print(f"Water Level: {self._water_level} ml")
        print(f"Coffee Level: {self._coffee_level} g")


# Creating an instance of the CoffeeMachine class
coffee_machine = CoffeeMachine()

# Using encapsulated methods to interact with the object
coffee_machine.display_status()
coffee_machine.brew_coffee("espresso")
coffee_machine.display_status()
coffee_machine.refill_water(300)
coffee_machine.refill_coffee(100)
coffee_machine.display_status()
coffee_machine.brew_coffee("latte")
coffee_machine.brew_coffee("cappuccino")
