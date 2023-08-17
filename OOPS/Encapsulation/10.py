class HealthRecord:
    def __init__(self, name, age):
        self._name = name  # Encapsulated attribute
        self._age = age  # Encapsulated attribute
        self._height = 0  # Encapsulated attribute in centimeters
        self._weight = 0  # Encapsulated attribute in kilograms
        self._blood_pressure = "120/80"  # Encapsulated attribute
        self._allergies = []  # Encapsulated attribute for allergies

    def update_height(self, height):
        if height > 0:
            self._height = height
            print(f"Updated height to {height} cm")

    def update_weight(self, weight):
        if weight > 0:
            self._weight = weight
            print(f"Updated weight to {weight} kg")

    def update_blood_pressure(self, blood_pressure):
        self._blood_pressure = blood_pressure
        print(f"Updated blood pressure to {blood_pressure}")

    def add_allergy(self, allergy):
        self._allergies.append(allergy)
        print(f"Added allergy: {allergy}")

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Height: {self._height} cm")
        print(f"Weight: {self._weight} kg")
        print(f"Blood Pressure: {self._blood_pressure}")
        print("Allergies:", ", ".join(self._allergies))


# Creating an instance of the HealthRecord class
person = HealthRecord("Alice", 30)

# Using encapsulated methods to interact with the object
person.update_height(165)
person.update_weight(60)
person.update_blood_pressure("130/85")
person.add_allergy("Pollen")
person.add_allergy("Penicillin")

person.display_info()
