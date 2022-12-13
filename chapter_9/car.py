# Create the class, remember that each class name has to be Capitalized
class Car:
    """A simple attempt to represent a car."""
# define the init() method with the self parameter first, then give it 3 other parameters/attributes
# attributes are variables within a class that describe what an object is/has
# the init() method takes these parameters and assigns them to the attributes that will be associated with the instances made from this class
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make # taking the value associated with the parameter make and assigning it ot the variable name
        self.model = model # taking the value associated with the paramter model and assigning it to the varibale model
        self.year = year # taking the value associated with the parameter year and assigning it to the variable year
        self.odometer_reading = 0 # setting a default value for an attribute (these can be defined without being passed in as parameters)

# we define a method (get_descriptive_name) that puts a car's year, make, and model into one string neatly describing the car
# a method are functions within a class that describes what an object can do
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
# an instance is made from the car class and it's assigned to the variable my_new_car
# we then call get_descriptive_name to show what kind of car we have
my_new_car = Car('kia', 'k5', 2022) 
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()





