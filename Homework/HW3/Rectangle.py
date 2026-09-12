#Make the Class (the Blueprint)
class Rectangle:
    def __init__(self, length, width):
        # save information into the object
        self.length = length
        self.width = width
    def calculate_area(self):
        # do something with the data
        return self.length * self.width
#        return "Area = " + str(self.length * self.width) + "units^2"
# create an object
Rectangle1 = Rectangle(5,3)
# print the result
print("Area = " + str(Rectangle1.calculate_area()) + " units^2")