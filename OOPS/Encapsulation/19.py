#  This system models an airline flight booking system with flights,
#  passengers, reservations, and ticketing. It aims to demonstrate
#  encapsulation, interactions, and system management

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._departure_time = departure_time
        self._capacity = capacity
        self._passengers = []

    def book_ticket(self, passenger):
        if len(self._passengers) < self._capacity:
            reservation = Reservation(self, passenger)
            self._passengers.append(passenger)
            passenger.add_reservation(reservation)
            print(f"Ticket booked for {passenger._name} on flight {self._flight_number}")
        else:
            print(f"Flight {self._flight_number} is fully booked")

    def display_info(self):
        print(f"Flight Number: {self._flight_number}")
        print(f"Origin: {self._origin}")
        print(f"Destination: {self._destination}")
        print(f"Departure Time: {self._departure_time}")
        print(f"Available Seats: {self._capacity - len(self._passengers)}")

    def display_passengers(self):
        print("Passengers:")
        for passenger in self._passengers:
            print(passenger._name)


class Passenger:
    def __init__(self, passenger_id, name):
        self._passenger_id = passenger_id
        self._name = name
        self._reservations = []

    def add_reservation(self, reservation):
        self._reservations.append(reservation)

    def display_info(self):
        print(f"Passenger ID: {self._passenger_id}")
        print(f"Name: {self._name}")

    def display_reservations(self):
        print("Reservations:")
        for reservation in self._reservations:
            print(f"Flight {reservation._flight._flight_number} - {reservation._flight._departure_time}")


class Reservation:
    def __init__(self, flight, passenger):
        self._flight = flight
        self._passenger = passenger


class FlightBookingSystem:
    def __init__(self):
        self._flights = {}
        self._passengers = {}

    def add_flight(self, flight):
        self._flights[flight._flight_number] = flight
        print(f"Added flight {flight._flight_number} from {flight._origin} to {flight._destination}")

    def add_passenger(self, passenger):
        self._passengers[passenger._passenger_id] = passenger
        print(f"Added passenger {passenger._name} to the system")

    def display_flights(self):
        print("Flights:")
        for flight in self._flights.values():
            print(f"Flight Number: {flight._flight_number} - Origin: {flight._origin} - Destination: {flight._destination}")

    def display_passengers(self):
        print("Passengers:")
        for passenger in self._passengers.values():
            print(f"Passenger ID: {passenger._passenger_id} - Name: {passenger._name}")


# Creating instances of the Flight, Passenger, and FlightBookingSystem classes
flight_system = FlightBookingSystem()

flight1 = Flight("F101", "New York", "Los Angeles", "2023-08-20 09:00 AM", 200)
flight2 = Flight("F102", "Chicago", "San Francisco", "2023-08-25 11:30 AM", 150)

flight_system.add_flight(flight1)
flight_system.add_flight(flight2)

passenger1 = Passenger("P001", "Alice Johnson")
passenger2 = Passenger("P002", "Bob Smith")

flight_system.add_passenger(passenger1)
flight_system.add_passenger(passenger2)

flight1.book_ticket(passenger1)
flight2.book_ticket(passenger2)

reservation1 = Reservation(flight1, passenger1)
reservation2 = Reservation(flight2, passenger2)

passenger1.add_reservation(reservation1)
passenger2.add_reservation(reservation2)

flight_system.display_flights()
flight_system.display_passengers()

passenger1.display_info()
passenger1.display_reservations()

flight1.display_info()
flight1.display_passengers()
