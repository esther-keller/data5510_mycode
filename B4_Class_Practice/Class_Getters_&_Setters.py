'''--------Notes---------
class = blueprint
object = what you use to create the blueprint
'''
import numpy as np #importing numpy so we can use the mean function to calculate the average of a list

class Person(): #naming convention for classes is to capitalize the first letter
    def __init__(self, name, age, height, grades): #init = initalize, self is in every function of the class and allows you to change data in the class
        self.name = name #self.name is how we store data on the object itself
        self.age = age
        self.height = height
        self.grades = grades
    def calc_avg_grades(self): #we can just put self here because we already stored all the info for it in the part before
        return np.mean(self.grades) #np.mean is a function that takes in a list and returns the average of the list. In order to do this we need to import numpy at the top of the file. We can also use sum(self.grades)/len(self.grades) to get the average but it's less efficient
    def get_name(self): #getter function: return the values
        return self.name
    def get_age(self):
        return self.age
    def get_height(self):
        return self.height
    def get_grades(self):
        return self.grades

    def set_name(self, name): #setter function: set a NEW value
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_height(self, height):
        self.height = height
    def set_grades(self, grades):
        self.grades = grades
    
p1 = Person("Esther", 24, 165, [97,100,96]) #Person is called the innit function of this class
#print(p1.name()) #this is actually bad style to access it directly so we use getters
print(p1.get_name()) #if I just print this, it will show the memory address (an object)
print(p1.get_age()) 
print(p1.get_height())
print(p1.get_grades())

p1.set_grades([100,100,100]) #this is how you set a new value for grades
print(p1.calc_avg_grades())
#print(p1.calc_avg_grades) #this will print the memory address because ofthe missing ()








'''--------personal practice---------'''
class Personpractice(): #create person class
    def __init__(self, name, heights, weight, age): 
        self.name = name
        self.heights = heights
        self.weight = weight
        self.age = age
    def find_Max_Height(self):
        return np.max(self.heights)

    def get_name(self):
        return self.name
    def get_heights(self):
        return self.heights
    def get_weight(self):
        return self.weight
    def get_age(self):
        return self.age

    def set_heights(self, heights):
        self.heights = heights

my_object = Personpractice("Esther", [134.62, 152.4, 160, 165], 115, 24) #creates person object
print(my_object.find_Max_Height())

my_object.set_heights([165,166,167,168])
print(my_object.get_heights())

