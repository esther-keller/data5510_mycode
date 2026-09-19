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




'''---------Polymorphism Programming Activity---------'''
#create class
class Student:
    def __init__(self,a_number,first_name,last_name,major,gpa,num_credits_enrolled):
        self.__a_number = a_number
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.num_credits_enrolled = num_credits_enrolled
#getters 
    def get_a_number(self):
        return self.__a_number
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_major(self):
        return self.major
    def get_gpa(self):
        return self.gpa
    def get_num_credits_enrolled(self):
        return self.num_credits_enrolled

#setters
    def set_a_number(self,a_number):
        self.__a_number = a_number
    def set_first_name(self,first_name):
        self.first_name = first_name
    def set_last_name(self,last_name):
        self.last_name = last_name
    def set_major(self,major):
        self.major = major
    def set_gpa(self,gpa):
        self.gpa = gpa
    def set_num_credits_enrolled(self,num_credits_enrolled):
        self.num_credits_enrolled = num_credits_enrolled
#add a function to determine fulltime/parttime status
    def is_full_time_student(self):
        return self.num_credits_enrolled >= 12

#create grad student that inherits from student class
class GradStudent(Student):
    def is_full_time_student(self):
        return self.num_credits_enrolled >= 6
#test students: 
s1 = Student('A00000001', 'Esther', 'Keller', 'IS', 4.0, 15)
s2 = Student('A00000002', 'Jason', 'Doe', 'Accounting', 3.2, 12)
s3 = Student('A00000003', 'Ryan', 'Smith', 'Marketing', 3.5, 9)
s4 = GradStudent('A00000004', 'Adele', 'Johnson', 'Finance', 2.0, 7)

students_5500 = [s1,s2,s3,s4]

#loop through all students
for student in students_5500:
    print(student.get_first_name(), student.is_full_time_student())