# Let's use functions to make working lists more efficient.
# say we have a list of users and want ot print a greeting to each
# the following example sends a list of names to a function called greet_users(), which greets each person in the list individually

# Define the function greet_users which assigns to parameter names in it
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    # For loop 
    for name in names:
        # Text for the desired printed message
        msg = f'Hello, {name.title()}!'
        # Print the message
        print(msg) # 
# List of usernames that need to be printed
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames) 

# Every user sees a personalized greeting, and you can call the function any time you want to greet a specific set of users.



