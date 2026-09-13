'''Create a class called Rectangle with attributes length and width. 
Implement a method within the class to calculate the area of the 
rectangle. Instantiate an object of the Rectangle class 
with length = 5 and width = 3, and print its area.'''

#Make the Class (the Blueprint)
class Rectangle:
    def __init__(self, length, width):
        # save information into the object
        self.length = length
        self.width = width
    def calculate_area(self):
        # do something with the data
        return self.length * self.width
# create an object
rectangle1 = Rectangle(5,3)
# print the result
print("Area = " + str(rectangle1.calculate_area()) + " units^2")