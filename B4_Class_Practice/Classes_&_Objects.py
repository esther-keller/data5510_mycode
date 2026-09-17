'''--------Notes---------
Class: the blueprint 
Objects: what you use to create the blueprint; used to represent something in the real world; something that has values, attributes, and functionality
Dictionary: can store heterogeneous data;
Classes and objects allow for you to have a bunch of heterogeneous data, wrap up the whole thing, and represent it together
Dictionaries can't have functions, which is why we use classes
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

p1 = Person("Esther", 24, 165, [97,100,96]) #Person is called the innit function of this class
#print(p1) if I just print this, it will show the memory address (an object)
#print (p1.name) if I print this object, then that specific thing will print (This printed "Esther")
#print(self.name) this will throw an error because you're not calling the object where the data is stored, so it doesn't know what self is
print(p1.calc_avg_grades())

'''--------personal practice---------'''
class Personpractice():
    def __init__(self, name, heights, weight, age):
        self.name = name
        self.heights = heights
        self.weight = weight
        self.age = age
    def find_Max_Height(self):
        return np.max(self.heights)

my_object = Personpractice("Esther", [134.62, 152.4, 160, 165], 115, 24)
print(my_object.find_Max_Height())
