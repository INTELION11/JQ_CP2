# JQ 2nd Clasess
# example 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize() 
        self.breed = breed.title()
        self.age = age

    def __str__(self):
        return f"Name: {doug.name} Breed: {doug.breed} age: {doug.age}"
    def speak(self):
        return f'{self.name}: Bark'


doug = Dog("Doug","Golden Retreiver",3)
pongo = Dog("Pongo","Dalmation",8)
#print(f"{pongo}")
#print(doug.speak())

# Example 2
class ClassSunject:
    def __init__(self, name, room = None, teacher = "Ms.LaRose" ):
        self.name = name.title()
        self.room = room
        self.teacher = teacher

    def __str__(self):
        return f"\nName: {self.name} \nRoom: {self.room} \nTeacher: {self.teacher}"
    
first = ClassSunject("Computer Programming 2", 200)
second = ClassSunject("Computer Programming 2", 200)
third = ClassSunject("Computer science principles", 200)
fourth = ClassSunject("Advisory", 218, "Ms. Thorrnock")
print(first, second, third, fourth)
