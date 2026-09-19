'''--------Notes---------
3 pillers of object oriented programming: 

1. incapsulation - Controls around your data (can make data private so that it's controled by the functions in the class itself, not foregin hackers (self.__xxx = xxx))
2. inheritence - Extending functionality to a child class
3. Polymorphism - ability to extend functionality from multiple classes
'''
class Student: 
    def __init__(self,anum,ssn,name):
        self.__anum = anum
        self.__ssn = ssn
        self.name = name
#getters
    def get_anum(self):
        return self.__anum
    def get_ssn(self):
        return self.__ssn
    def get_name(self):
        return self.name
#setters
    def set_anum(self):
        self.__anum = anum
    def set_ssn(self):
        self.__ssn = ssn
    def set_name(self):
        self.name = name





'''--------Practice---------'''
