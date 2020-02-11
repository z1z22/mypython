'''此模块是一个用于表示电池的类'''
class Battery():
    '''将子类电动车特有的属性单独归为一类'''
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + 'kwh battery.')
        
    def get_range(self):
        # if self.battery_size == 70:
        #     run = 240
        # elif self.battery_size ==85:
        #     run = 270
        run = self.battery_size * 3.5
        message = "This car can go " + str(run) 
        message += " mile on a full charge."
        print(message)

mycar = Battery(70)
mycar.get_range()

