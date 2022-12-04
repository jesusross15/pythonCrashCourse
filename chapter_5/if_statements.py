# Chapter 5 Overview
# conditional tests
# if statements
# using if statements with lists
# styling if statements

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# We are going to learn to write conditional tests which allow us to check any condition of interest
# Python's if statement allows us to examine the current state of a program and respond appropriately to that state
print("A Simple Example:")
cars = ['audi', 'bmw', 'subaru', 'toyota']
# We have a list of cars. Cars brands are proper nouns which mean that they should be capitlized.
# However we want to capititalize ALL letters in BMW so do the following
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# The loop in this example first checks if the current value of car is 'bmw'
# If it is, the value is printed in uppercase if it's anything other than 'bmw' then it's printed in title case

print("\nLet's Start With the Basics")
print("Checking for Inequality")

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
# The eclamation point represents a 'NOT" as in "!=" NOT EQUAL

print("\nNumerical Comparisons")
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
# You can include different types of numberical comparisons in the conditional statement such as:
# less than <
# less than or equal to <=
# greater than >
# greater than or equal to >
print("\nChecking Whether a Value is Not in a List")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean expressions
# A boolean expression is just another name for a conditional test.
# A boolean value is either TRUE or FALSE
# They are often used to keep track of certain conditions, such as whether a game is running or
# whether a user can edit certain content on a website:
print("\n5.1 Conditional Tests:")
car_1 = 'subaru'
print("Is car_1 == 'subaru'? I think True.")
print(car_1 == 'subaru')

print("\nIs car_1 == 'audi'? I preduct False.")
print(car_1 == 'audi')
