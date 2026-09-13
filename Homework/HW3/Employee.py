'''Create a class called Employee with attributes name and salary. 
Implement a method within the class that increases the salary of 
the employee by a given percentage. 
Instantiate an object of the Employee class with 
name = "John" and salary = 5000, increase the salary by 10%, 
and print the updated salary.'''

# Make the Class (the Blueprint)
class Employee:
    def __init__(self, name, salary):
        # save information into the object
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        # increase the salary by a given percentage
        self.salary += self.salary * (percentage / 100)

# create an object
employee1 = Employee("John", 5000)
employee1.increase_salary(10)
print("Updated salary = $" + str(employee1.salary))


"""AI Prompt
does this code mach the instructions? if not, don't tell me the answer but show me where I'm wrong: '''Create a class called Employee with attributes name and salary. Implement a method within the class that increases the salary of the employee by a given percentage. Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, and print the updated salary.'''
# Make the Class (the Blueprint)class Employee:    def __init__(self, name, salary):        # save information into the object        self.name = name        self.salary = salary
    def increase_salary(self, percentage):        # increase the salary by a given percentage        self.salary += self.salary * (percentage / 100)
# create an objectemployee1 = Employee("John", 5000)employee1.increase_salary(10)print("Updated salary = $" + str(employee1.salary))
"""