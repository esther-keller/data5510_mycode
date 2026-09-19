'''--------Notes---------
3 pillers of object oriented programming: 

1. incapsulation - Controls around your data (can make data private so that it's controled by the functions in the class itself, not foregin hackers (self.__xxx = xxx))
2. inheritence - Extending functionality to a child class
3. Polymorphism - ability to extend functionality from multiple classes
'''
class Student: 
    def __init__(self,anum,ssn,gpa,name):
        self.__anum = anum
        self.__ssn = ssn
        self.__gpa = gpa
        self.name = name
#getters
    def get_anum(self):
        return self.__anum
    def get_ssn(self):
        return self.__ssn
    def get_gpa(self):
        return self.__gpa
    def get_name(self):
        return self.name
#setters
    def set_anum(self,anum):
        self.__anum = anum
    def set_ssn(self,ssn):
        self.__ssn = ssn
    def set_gpa(self,gpa):
        self.__gpa = gpa
    def set_name(self,name):
        self.name = name
#calculations
    def calculate_gpa(self):
        pass
        #add in the logic

andy = Student('a00001',123456,3.9,'andy')
print(andy.get_name())
print('---------')
andy.set_anum('a00000001')
print(andy.get_anum())