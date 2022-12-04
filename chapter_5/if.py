# If Statements
# Simple If Statements

print("Voting.py")
age = 17 
if age>= 18:
    print("You are old enought to vote!")
    print("Have you registered to vote?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if else statements are great if you only need to decide between two choices but most
# real world situations require you to evaluate more than 2 possible situations
# this is where the if-elif-else chain comes in

print("\nAmusement Parl prices")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
# Here we have an example of an amusement park that charges different rates depending on your age
# The if tests whether a person is under 4 years old, if it passes the appropriate message is printed
# The elif test is really just another if test that only runs if the previois if test fails
# Any age greater than 17 would cause the first 2 tests to fail ----> which makes the program run the "else" command in  which case the person would have to pay $40

# EDIT (rather than printing the admission price within the if elif else block our code would be more concise if we just set
# the price INSIDE the if elif else chain just like this)

age=12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# You can use as many elif blocks in your code as you like (example: add another one if the amusment park gives a discount to senior citizens)
# Python does ~NOT~ require an "else" block at the end of the chain it just makes the code clearer (sometimes)

# Testing Multiple Conditions
# The if-elif-else chain is powerful but it's onyl appropriate to use when you just ened one test to pass
# Sometimes it's important to check all of the conditions of interest. In this case use a series of elif or else blocks
# This technique makes sense when more than one condition could be True and you want to act on every condition that is TRUE

print("\nPizzeria Example:")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# THIS CODE WOULD NOT RUN USING AN IF ELIF ELSE BLOCK BECAUSE THE CODE WOULD STOP RUNNING AFTER ONLY ONE TEST PASSES

print("\nAlien Colors 5.3")
alien_color = ['green', 'yellow', 'red']
alien_color = 'yellow'

if alien_color == 'green':
    print("Congrats! You have just earned 5 points!")
elif alien_color == 'yellow':
    print("You have just earned 10 points!")
else:
    print("You have earned 15 points!")

print("\nStages of Life")
age = 14
# Write an if-elif-else chain that determines a person's stage of life
if age < 2:
    print("This person is a baby.")
elif 2 <= age < 4:
    print("This person is a toddler.")
elif 4 <= age < 13:
    print("This person is a kid.")
elif 13 <= age < 20:
    print("This person is a teenager.")
elif 20 <= age < 65:
    print("This person is an adult.")
elif age >= 65:
    print("This person is an elder.")


