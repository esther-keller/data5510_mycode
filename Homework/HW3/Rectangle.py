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




'''AI Prompts
okay so now I'm going to start the homework. This is the first question that I'm starting with. 1.    Create a class called  with attributes  and . Implement a method within the class to calculate the area of the rectangle. Instantiate an object of the  class with length = 5 and width = 3, and print its area.
Don't just give me the code. don't move on to the next part of the homework until we do a sanity check. create checkpoints for me to stop and send a screenshot or my code to you. I have created a class 2 times before, but I'm still learning how to do it. help me to learn. What do you need from me in order to do this with 95% accuracy? 
length and width should be stored with every single rectangle object. I don't understand the question. rephrase it 
the method should be able to calculate area, find the perimiter, etc. all of the basic calculatiosn taht you can dowith length and width
okay so i can't remember how to start it. help me start it but don't just give me all the code teach me about each piece and I'll put it together
what's the difference between class Rectangle(): and class Rectangle:
this is the code that I have. and help me to fill in any gaps in my knowlege: 
this is making a class called rectangle and saying that there's 2 things that should be included iside of it, length and width. I'm not sure what the "self.xxx" does. what this code does not do though is output anything, or define length and width as something specific. I think that I still need to import numpy to do the math to create the area
here's my code fo rmy earlier prompt: class Rectangle:
    def __init__(length, width):
        self.length = length
        self.width = width

okay this is my final code output does it match the requirements of the homework question" class Rectangle:    def __init__(self, length, width):        # save information into the object        self.length = length        self.width = width    def calculate_area(self):        # do something with the data        return self.length * self.width# create an objectRectangle1 = Rectangle(5,3)# print the resultprint("Area = " + str(Rectangle1.calculate_area()) + " units^2")
'''