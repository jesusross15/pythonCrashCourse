print("Working with Part of a List")
print("Slicing a List")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# This will include the first 3 players in a list (it will omit florence)

print(players[1:4])
# Same thing with the omittion of the last value 1:4 will be martina thru florence

# If you ommit the first index in a slice, Python automatically starts your slice at the beginning og the list:
print(players[:4])

# If you ommit the last index in a slice, python automatically starts your slice and the intended first value and all the way through the last
print(players[2:])

# Use this syntax to output all the elements from any point in the list to the end
print(players[-3:])

print("\nLOOPING THROUGH A SLICE")
# You can use a slice in a for loop if u want to loop through a subset of the elements in a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first 3 playrs on my team:")
for player in players[:3]:
    print(player.title())

print("\nCopying a List")
# Python let's you copy a list and make a new one based on the contents of the first list
# To do this just make your first lists equal to your second list and put square brackets with a lone colon in it (ommit the first and second index)
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# From here you can add different stuff to each list seperately if you would like
my_foods.append('cannoli')
friend_foods.append('hamburgers')
print(my_foods)
print(friend_foods)

print("\n4.10 Slices Do it Yourself")
groceries = ['apples', 'celery', 'muchrooms', 'peppers', 'broccoli']
print("The first three items in the list are:")
for grocery in groceries[:3]:
    print(grocery)

print("\nThree items from the middle of the list are:")
for grocery in groceries[1:4]:
    print(grocery)

print("\nMy Pizzas, Your Pizzas")
pizzas = ['pepperoni', 'meat lovers', 'plain']
friend_pizza = pizzas[:]
print(pizzas)
print(friend_pizza)

pizzas.append('veggie')
friend_pizza.append('hawaiin')
print(pizzas)
print(friend_pizza)

print("My favorite pizzas are:")
print(pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizza)

print("\n4.12: More Loops")
my_foods = ['pizza', 'falafel', 'carrot cake']
for loop in my_foods [:]:
    print(loop)

print("\nTuples")
# an immutable list (values that cannot change) is called a TUPLE = a list that doesn't change
# it looks exactly like a list but instad of square brackets you use parantheses
# if we have a rectanlge that should always be a certain size, we can ensure that its size doesn't change by
# putting the dimensions of said rectangle into a tuple
print("dimensions.py")
dimensions = (200, 50)
print(dimensions [0])
print(dimensions [1])
# dimensions [0] = 250 as u can see it does not change
# Tuples are technically defined by the presence of a COMMA (parantheses just make them look neater)
# if you want to define a tuple with one element, you need to include a trailing comma lis this:
my_t = (3, )

print("\nLooping Through All Values in a Tuple")
# You can loop over all the values in a tuple using a for loop, just like a list
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("\nWriting over a Tuple")
# You can't modify a tuple but you can definitely assing a new value to a variable that represents a tuple
# If we wanted to change our dimensions, we could redefine the entire tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimenions:")
for dimension in dimensions:
    print(dimension)
# tuples are simple data structures. 
# Use them when you want to store a set of values that you don't wanna change throughout the life of a program.

print("\n4.13 Buffet")
buffet = ('chicken tendies', 'fries', 'hamburgers', 'hot dogs', 'ribs')
for food in buffet:
    print(food)

# buffet [0] = ("cole slaw") good it rejects it :)
buffet = ('chicken tendies', 'fries', 'hamburgers', 'hot dogs', 'ribs')
print("\nOriginal Menu:")
for food in buffet:
    print(food)

buffet = ('ice cream', 'fies', 'hamburgers', 'hot dogs', 'cole slaw')
print("\nMenu Changes:")
for food in buffet:
    print(food)

