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