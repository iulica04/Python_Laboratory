# Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types
# of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.
from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

    def calculate_mileage(self):
        pass

class Car(Vehicle):
    model_mileage_rate = {
        "Corolla": 15000,
        "Civic": 14000,
        "Mustang": 12000
    }
    default_mileage_rate = 10000

    def calculate_mileage(self):
        current_year = datetime.now().year
        age = current_year - self.year
        mileage_rate = Car.model_mileage_rate.get(self.model, Car.default_mileage_rate)
        return mileage_rate * age

class Motorcycle(Vehicle):
    model_mileage_rate = {
        "Ninja": 8000,
        "CBR": 7500,
        "Harley": 5000
    }
    default_mileage_rate = 6000

    def calculate_mileage(self):
        current_year = datetime.now().year
        age = current_year - self.year
        mileage_rate = Motorcycle.model_mileage_rate.get(self.model, Motorcycle.default_mileage_rate)
        return mileage_rate * age

class Truck(Vehicle):
    model_mileage_rate = {
        "F-150": 20000,
        "Ram": 18000,
        "Silverado": 19000
    }
    default_mileage_rate = 15000

    def calculate_mileage(self):
        current_year = datetime.now().year
        age = current_year - self.year
        mileage_rate = Truck.model_mileage_rate.get(self.model, Truck.default_mileage_rate)
        return mileage_rate * age

if __name__ == '__main__':

    car = Car("Toyota", "Corolla", 2018)
    print(car.vehicle_info())
    print(car.calculate_mileage())

    motorcycle = Motorcycle("Honda", "CBR", 2020)
    print(motorcycle.vehicle_info())
    print(motorcycle.calculate_mileage())

    truck = Truck("Ford", "F-150", 2015)
    print(truck.vehicle_info())
    print(truck.calculate_mileage())

