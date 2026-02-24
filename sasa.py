class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print("Dog Name:", self.name)
        print("Dog Age:", self.age)
        print("Species:", Dog.species)
        print("-------------------")
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog1.display_details()
dog2.display_details()