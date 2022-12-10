# POSITIONAL ARGUMENTS

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls
# you can call a function as many times as needed just like we did here to describe our pet dog
describe_pet('dog', 'will')

# Keyword Arguments
