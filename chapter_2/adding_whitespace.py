print("python")

# \t is for an indindation so it your overall code coul be easier to read in general which could save people time.
print("\tJesus") 

# \n is for when you want to start a new line of code take a look at this example of a simple greocery list
print("Grocery List: \napples\noranges\nshampoo\ntoothbrush")

# this is a combination of both \n and \t
print("Grocery List: \n\tapples\n\toranges\n\tshampoo\n\ttoothbrush")


# Stripping whitespace
# You have to be careful with your whitespace because to programmers
# "python" and "python " mean the same thing but not to computers unless
# you tell the computer otherwise
# to make sure that there is no whitespace at the end of a string, use the rstrip() method

favorite_language = 'python '
print(favorite_language.rstrip())
