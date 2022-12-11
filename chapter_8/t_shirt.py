# first we must define the function
def make_shirt(shirt_size, shirt_message):
    """8.3 try it yourself shirt problem"""
    print(f"The shirt size is a {shirt_size} and it says {shirt_message}.")

# calling the function with positional arguments
# when it comes to positonal arguments location matters
make_shirt('large', 'cool kidz')

# calling the function with keyword arguments
# when it comes to keyword arguments location does NOT matter
make_shirt(shirt_size='small', shirt_message="what's up yall")



