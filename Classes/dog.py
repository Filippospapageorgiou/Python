

class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting ")
    
    def roll_over(self):
        print(f"{self.name} rollde over!!")

my_dog = Dog('willie',6)

print(f"My dogs name is {my_dog.name}.")
print(f"My dog age is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
