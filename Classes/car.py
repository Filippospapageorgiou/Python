class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_format_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")


my_new_car = Car('audi','A4',2020)
print(my_new_car.get_format_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 10
my_new_car.read_odometer()
