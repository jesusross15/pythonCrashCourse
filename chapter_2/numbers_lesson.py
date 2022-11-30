# Numbers are used a lot in programming to sleep score in games,
# represent data in visualizations, store information and so on
# Python treats numbers in several different ways, depending on how they're being used.

#Integers 
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# Python uses 2 asteriks ** to represent exponents
print(4 ** 3)

# Python also follows order of operations too
print(2 + 3 * 4)

# Python calls any number with a decimal a "float"
print(0.1 + 0.1)

# Sometimes you will get an arbitray number of decimal places in your answer
print(0.2 + 0.1)
# This happens in all languages and is of little concern and you'll learn to deal with them

# When you divide any 2 numbers no matter what you'll get a float
# If you mix an integer and a float in any other operation, you'll also get a float
print(2 + 3.0)

# When you are writing long numbers, you can group digits using underscores
# to make large numbers more readable for you and to avoid errors
universe_age = 14_000_000_000
print(universe_age)
# Be aware that Python omits these underscores and prints the digits
# without the commas to python 1000 is the same as 1_000

# You can assign values to more than one variable in a single line

x, y, z = 2, 2, 2

print(x)
print(x, y)

# to indicate a constant (number that should never be changed) assign a 
# variable name in all CAPS example below
MAX_CONNECTIONS = 0


