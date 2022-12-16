# TRY IT YOURSELF 9.1 RESTAURANT

class Restaurant: # naming the class
    """An attempt to make a class.""" # giving the class a description

# this class has 2 PROPERTIES, restaurant name and cuisine type
    def __init__(self, name, type): # then we create a function that initializes the class # self serves here as the current instance of the current class 
        """Initialize restuarant name and cuisine type attributes."""
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        """Description of the restaurant."""
        print(f"{self.name} serves wonderful {self.type}!")
    
    def open_restuarant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.name} is open for business.")

restaurant = Restaurant("Maola's", 'pizza') # creating an instance

print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restuarant()