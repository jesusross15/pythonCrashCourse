from numpy import result_type


class Restaurant:
    """An attempt to make a class.""" 

    def __init__(self, name, type): 
        """Initialize restuarant name and cuisine type attributes."""
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        """Description of the restaurant."""
        print(f"{self.name} serves wonderful {self.type}!")
    
    def open_restuarant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.name} is open for business.")
    
    def set_number_served(self):
        """Allow user to set the number of customers that have been served at the restaurant."""
        print(f"This restaurant has served {self.number_served} people!")
    

restaurant = Restaurant("Maola's", 'pizza') 
restaurant.describe_restaurant()
restaurant.open_restuarant()

print(f"\nNumber of customers served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number of customers served: {restaurant.number_served}")



