class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas = 100

    def get_name(self):
        long_name = f"{self.year} {self.model} {self.make}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car have {self.odometer} miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You cant roll back miles in the car")

    def increment_miles(self, miles):
        self.odometer += miles

    def fill_gas_tank(self, gas):
        if self.gas <= 100:
            self.gas += gas


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 100

    def describe_battery(self):
        print(f"This electric car have {self.battery} battery left")

    def fill_gas_tank(self, gas):
        print("Electric cars dont have gas")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_name())
print(my_tesla.describe_battery())
print(my_tesla.fill_gas_tank(100))
my_tesla.increment_miles(100)
my_tesla.read_odometer()
