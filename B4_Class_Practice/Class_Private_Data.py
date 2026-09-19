'''--------Notes---------
this isn't really for keeping data from hackers. it's to prevent errors and create more robust
you as the developer can cotrol your data and how it's used

'''
import numpy as np

class Person():
    def __init__(self, name, age, height, grades, ssn):
        self.name = name
        self.age = age
        self.height = height
        self.__grades = grades #the __ means that this data is private and you can't access it directly. You NEED to use a getter and setter
        self.__ssn = ssn
    def get_grades(self):
        return self.__grades
    def get_ssn(self):
        return self.__ssn #you can access this data within the same class which is why you can do it here

    def set_ssn(self, ssn):
        self.__ssn = ssn

    def calc_avg_grades(self):
        return np.mean(self.__grades)

p1 = Person("Esther", 24, 165, [100,100,100], 12341234)

print(p1.name)
print(p1.get_grades()) #notice here that i'm using get_grades not get__grades
print(p1.get_ssn())




'''--------personal practice---------'''
class Student():
    def __init__(self, name, anumber):
        self.name = name
        self.__anumber = anumber
    #Getters 
    def get_name(self):
        return self.name
    def get_anumber(self):
        return self.__anumber
    #Setters
    def set_name(self, name):
        self.name = name
    def set_anumber(self, anumber):
        self.__anumber = anumber
    

s1 = Student("Esther", "a00001234") 

print(s1.get_name())
print(s1.get_anumber()) #this will print memory address without () and print anumber with ()
#print(s1.anumber) #this will print an AttributeError becuase the object student has no anumber attribute since i made it private