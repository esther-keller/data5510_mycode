import numpy as np

class Person():
    def __init__(self, name, age, favorite_colors, hw_scores):
        self.name = name
        self.age = age
        self.favorite_colors = favorite_colors
        self.hw_scores = hw_scores

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old and their favorite colors are: " + str(self.favorite_colors) + " and their average grade is " + str(self.calc_avg_grades())
    def calc_avg_grades(self):
        return np.mean(self.hw_scores)
    def set_name(self,name):
        self.name = name


andy_person = Person("Andy", 43, ["aggie blue", "fighting white"], [95, 80, 99])
jaeden_person = Person("Jaeden", 23, ["purple", "dark blue", "orange"], [100,97,94])
saige_person = Person("Saige", 20, ["sage", "yellow"], [100, 100, 100])

print(andy_person) #andy_person is the object while person is the blueprint
print ("--------")
print(jaeden_person) 
print ("--------")
print(saige_person) #saige_person is the object while person is the blueprint
print ("--------")
#input("pause") #this is a pause so you can see the output before it closes

print(saige_person.age)
print(saige_person.name)
print(saige_person.favorite_colors)

# a class is blueprint combining data and functions
# initializer defines the parameters of your blueprint
    # an attribute is a variable inside a class
    # an object is what you build with it
    # innit is a constructor, it runs when you create an object


'''--------personal practice---------'''
#funtion specific to data points
#create a class with 3 objects

class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return self.name + " is " + str(self.age) + " years old and their breed is: " + str(self.breed)

    def set_name(self,name):
        self.name = name

Mushu_Dog = Dog("Mushu", 15, "Poodle Terrior Mix")
Jane_Dog = Dog("Jane", 5, "Unknown Mix")

print(Mushu_Dog)
print()
print(Jane_Dog)
print()
print(Mushu_Dog.age)
print(Mushu_Dog.name)
print(Mushu_Dog.breed)
