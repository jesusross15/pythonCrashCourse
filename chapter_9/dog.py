# object oriented programming

# define the class (ALL CLASSES ARE CAPITALIZED)
class Dog:
    """A simple attempt to model a dog.""" # this is a docstring describing what the class does
# we defined the __init__() method to have 3 parameters      

# a function that is part of class is called a method
# __ini__() method is a special method that python runs automatically whenever we craete a new instance based on the given class
    def __init__(self, name, age): 
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()



