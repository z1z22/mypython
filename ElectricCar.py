from car import ElectricCar
    
my_tesla = ElectricCar('tesla', 'model s', 2018)
my_tesla.battery.battery_size = 85

print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()