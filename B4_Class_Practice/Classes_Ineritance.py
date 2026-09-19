'''---------Notes---------
if you need to add more to that class, you could create a new class, or create an inheritance
you create a new class (the old class but more)
parent/child == base/dirrived

shape is a base class --> child class would be a type of shape (circle)
child adds it's own data and functionality
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

gregs_car = AntiqueCar("Cadillac", "DeVille", 1976, 100000,18000)
print("gregs_car value:", round(gregs_car.current_value(2026),2))




'''---------Practice---------'''