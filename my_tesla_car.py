class Car():
    '''父类的代码要放在子类的前面'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive(self):
        long_name = str(self.year) + " " + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
        
    def update_odometer(self, mileage):
        '''将里程表读数设定为指定值'''
        self.mileage = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer')
    def increment_odometer(self, miles):
        '''将里程表读书增加指定的量'''
        self.odometer_reading += miles

class Battery():
    '''将子类电动车特有的属性单独归为一类'''
    def __init__(self, battery_size=70):

        self.battery_size = battery_size

    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + 'kwh battery.')
        
    def get_range(self):
        if self.battery_size == 70:
            run = 240
        elif self.battery_size ==85:
            run = 270
        message = "This cat can go " + str(run) 
        message += " mile on a full charge."
        print(message)
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
my_tesla = ElectricCar('tesla', 'model s', 2018)
my_tesla.battery.battery_size = 85

print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
    