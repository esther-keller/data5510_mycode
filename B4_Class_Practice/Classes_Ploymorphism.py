'''---------Notes---------
intermixing child and parent classes

a child class has all the data and functionality of it's parent and then adds more. 
if you know that, you can write a program that assuems that those things exist in a chiild because you know they exist in the parent
knowing that, you can mix and match the objects!! = polymorphism
'''

class Car: 
    def __init__(self, make, model, year,mileage,origional_price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.origional_price = origional_price

    def current_value(self,current_year):
        return self.origional_price * (.90**(current_year - self.year))

andys_car = Car('toyota', 'sequoia', 2001, 275000, 45000)
print("andys_car value:", round(andys_car.current_value(2023),2))


class AntiqueCar(Car): #this is how you specify that it's in inherited class not a new class
    def current_value(self,current_year):
        return self.origional_price *(1.03 **(current_year - self.year))

gregs_car = AntiqueCar("Cadillac", "DeVille", 1976, 100000,18000) #this is where polymorphism is occuring because it's where we're intermixing parent and child classees
print("gregs_car value:", round(gregs_car.current_value(2026),2))

'''add in polymorphism'''
#add in new cars
johnnys_car = Car('ford','f150', 2015, 55000, 45000)
jennys_car = Car('Toyota', 'Rav4', 2006, 125000,20000)

car_lot = [andys_car,johnnys_car,jennys_car,gregs_car] 

total_value = 0.0

for car in car_lot:
    print(type(car))
    total_value = car.current_value(2026)

#when you print just the object, it gives you the string version (the memory address)
print("all cars value: ", round(total_value,2))