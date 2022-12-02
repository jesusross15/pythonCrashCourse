# In chapter 3 I learned how to make a simple list and work with individual elements in a list
# Here we will learn how to LOOP through an entire list using just a few lines of code regardless
# of how long the list is.
# This allows us to take the same action with every item in a list
# Resuling in working efficiently with lists of any length (even millions of items)

# The for Loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    #print(magician)
# Looping is important because it's one of the most common ways a computer automates repetitive tasks
# you can use whatever name you want for the temp variable associated with wach value in the list
# (in this case magician could have been dog as long as when we print it the same value should be print(dog)
    print(f"{magician.title()}, that was a great trick! Bravo!")
    # You have to indent after a for loop action 

# Here we start with the try it yourselfs on page 59
print("\n4.1 Pizzas Page 56")

pizzas = ['pepperoni', 'meat lovers', 'plain']
for pizza in pizzas:
    print(f"I love {pizza} pizza.")
print("I really enjoy eating these kinds of pizzas!")

# Another try it yourself on page 59
print("\n4.2 Animals This is the Animal TRY IT YOURSELF")

animals = ('dog', 'cat', 'fox', 'bunny')
for animal in animals:
    print(f"One day I would really love to have a {animal} as a pet.")
print("All of the animals that I mentioned above would make great pets!")

# Making Numerical Lists
# Lists are ideal for storing sets of numbers and Python provides lots of diffferent tools to work 
# with them efficiently 
# Example: In game to keep track of position of each character in a game or the high scores of the players
# Example 2: In data visualizations lots of data invlolving temperatures, distances, population sizes etc.

# Using the range() function
# this makes it east to generate a series of numbers

for value in range(1, 5):
    print(value)
# range() only prints numbers 1 through 4 bc of the off-by-one behavior that you'll often see in programming languages

for value in range(6):
    print(value)
 # if you just put one number in the range parenthesis you will actually get all the numbers to that number -1 starting from 0

# Using range to make a list of numbers
# When you wrap list() around a call to the range() function, the output will be a list of numbers
numbers = list(range(1, 11))
print(numbers)

# We could also use the range function to tell Python to skip numbers in a given range
even_numbers = list(range(2, 21, 3))
print(even_numbers)
# The third value in the parenthesis is what is added to the first number until it reaches the second -1

print("\nNow this is how you make a list of all the square values from 1-10.")
squares = []
for value_1 in range(1, 11):
    squares.append(value_1 ** 2)

print(squares)

print("\nSimple Statistics with a List of Numbers")
# You can find the minimum, maximum, and sum of a list of numbers:

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

print("\nList Comprehensions")
# List comprehension allows you to generate this same list in just one line of code 

# It takes practice to write your own list comprehensions but they are worth practicing bc it leads to cleaner and lesser code
# To use this syntax, begin with a descriptive name for the list, such as squares. 
# Next, open a set of square brackets and define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. 
# Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. 
# The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. 
# Notice that no colon is used at the end of the for statement.
squares_1 = [value_1**2 for value_1 in range(1, 11)]
print(squares_1)
# For reference this is what the original looked like
# squares = []
# for value_1 in range(1, 11):
    # squares.append(value_1 ** 2)

print("\nTry it yourself 4.3 Page 60")
twenty = [value_3 for value_3 in range(1, 21)]
print(twenty)

print("\n4.4 Summing a Million")
million = [milly for milly in range (1, 1000001)]
# print(million) will litterally print all numbers 1 thru 1 million don't do it haha
print(sum(million))
print(max(million))
print(min(million))

print("\n4.6 Odd Numbers")
odd = list(range(1, 21, 3))
print(odd)

print("\n4.7 Threes")
threes = {multiple*3 for multiple in range (1, 31)}
print(threes)

print("\nCubes")
cube = [cubes**3 for cubes in range(1, 11)]
print(cube)