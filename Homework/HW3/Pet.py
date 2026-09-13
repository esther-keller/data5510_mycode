'''Create a class called Pet with attributes name and age. 
Implement a method within the class to calculate the age of the pet in equivalent human years. 
Additionally, create a class variable called species to store the species of the pet. 
Implement a method within the class that takes the species of the pet as input and returns the average lifespan for that species.

Instantiate three objects of the Pet class with different names, ages, and species.
Calculate and print the age of each pet in human years.
Use the average lifespan function to retrieve and print the average lifespan for each pet's species.'''

#set avg lifespans for each species
lifespans = {
    'dog': 13,
    'cat': 15,  
    'fish': 5}

# Make the Class (the Blueprint)
class Pet: 
    def __init__(self, name, age, species):
        # save information into the object
        self.name = name
        self.age = age
        self.species = species

    def age_in_human_years(self):
        if self.species.lower() == 'dog':
            return self.age * 7
        elif self.species.lower() == 'cat':
            return self.age * 6
        elif self.species.lower() == 'fish':
            return self.age * 5
        else:
            return self.age * 1  # default case for unknown species
    def get_average_lifespan(self):
        return lifespans.get(self.species.lower(), "Unknown species")

#animals to put in 
dog = Pet("Mushu", 15, "Dog")
cat = Pet("Little Brother", 3, "Cat")
fish = Pet("Nemo", 1, "Fish")

#print to check
print()
print('-----------Age in Human Years-------------------')
print(f"{dog.name} is a {dog.species}, is {dog.age} year(s) old, and is {dog.age_in_human_years()} in human years.")
print()
print(f"{cat.name} is a {cat.species}, is {cat.age} year(s) old, and is {cat.age_in_human_years()} in human years.")
print()
print(f"{fish.name} is a {fish.species}, is {fish.age} year(s) old, and is {fish.age_in_human_years()} in human years.")
print()
print('-----------Average Lifespan-------------------')
print(f"The average lifespan of a {dog.species} is {dog.get_average_lifespan()} years.")
print()
print(f"The average lifespan of a {cat.species} is {cat.get_average_lifespan()} years.")
print()
print(f"The average lifespan of a {fish.species} is {fish.get_average_lifespan()} years.")
