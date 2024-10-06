
class Vehicle:
    def __init__(self, make, model, rental_rate):
        self.make = make
        self.model = model
        self.rental_rate = rental_rate
        self.is_available = True

    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
            return True
        
    def return_vehicle(self):
        self.is_available = True

class Car(Vehicle):
    def __init__(self, make, model, rental_rate, car_type):
        super().__init__(make, model, rental_rate)
        self.car_type = car_type

class Bike(Vehicle):
    def __init__(self, make, model, rental_rate, bike_type):
        super().__init__(make, model, rental_rate)
        self.bike_type = bike_type

def add_vehicle(fleet):
    vehicle_type = input("Enter vehicle type (Car/Bike): ").lower()
    make = input("Enter make: ")
    model = input("Enter model: ")
    rental_rate = float(input("Enter rental rate: "))
    if vehicle_type == "car":
        car_type = input("Enter car type: ")
        fleet.append(Car(make, model, rental_rate, car_type))
    elif vehicle_type == "bike":
        bike_type = input("Enter bike type: ")
        fleet.append(Car(make, model, rental_rate, bike_type))

def rent_vehicle(fleet):
    model = input("Enter model to rent: ")
    for vehicle in fleet:
        if vehicle.model == model and vehicle.rent_vehicle():
            print(f"Rented: {model}.")
            return
    print("Vehicle not available.")

def return_vehicle(fleet):
    model = input("Enter model to return: ")
    for vehicle in fleet:
        if vehicle.model == model:
            vehicle.return_vehicle()
            print(f"Returned: {model}.")
            return
    print("Vehicle not found.")

def show_available_vehicles(fleet):
    print("Available vehicles: ")
    for vehicle in fleet:
        if vehicle.is_available:
            print(f"{vehicle.__class__,__name__}: {vehicle.make} {vehicle.mode}")

def main():
    fleet = []
    while True:
        print("\n1. Add Vehicle\n2. Rent Vehicle\n3. Return Vehicle\n4. Show Available Vehicles\n5. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                add_vehicle(fleet)
            elif choice == "2":
                rent_vehicle(fleet)
            elif choice == "3":
                return_vehicle(fleet)
            elif choice == "4":
                show_available_vehicles(fleet)
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()