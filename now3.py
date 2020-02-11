class Car(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year


    def fullname(self):
        return (self.name + ' 购买于 ' + str(self.year))

        
my_car = Car('BMW', 2015)
print(my_car.fullname())