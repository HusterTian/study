from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_desciptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.increment_odometer(50)
my_new_car.read_odometer()