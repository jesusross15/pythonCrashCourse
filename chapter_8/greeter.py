# Functions are named blocks of code that are designed to do one specific job
# When you want to perform a particular task that you've defined in a function, you call
# the function responsible for it 

# basically if you need to type the code for the same task again and again you don't need
# to type the entire thing you simply just call the function 
# this makes coding programs easier to read, test, and fix

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('zander')

#ARGUEMNTS AND PARAMETERS
# the variable username in the definition of greet_user() is an example of a parameter
# ---- a piece of information that the function needs to do its job
# the value zander in greet_user('zander') is an example of an argument
# ---- a piece of informaton that's passed from a function call to a function
# zander was passed to the function greet_user() and the value was assigned to the parameter username

