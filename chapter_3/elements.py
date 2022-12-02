# Changing, Adding, and Removing Elements
# Most of the lsits you create will change meaning that it will add and
# remove elements from it as your program runs its course
# like how we will create an Alien game 

# MODIFYING ELEMENTS IN A LIST (the syntax is pretty similar to that of adding and element to a list)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# Now check this
motorcycles[2] = 'ducati'
print(motorcycles)

# ADDING ELEMENTS TO A LIST
# You might want to add a new element to a list for many reasons. 
# For example, you might want to make new aliens appear in a game, 
# add new data to a visualization, 
# or add new registered users to a website you’ve built. 
# Python provides several ways to add new data to existing lists.

# Adding elements to the end of a list
# "append" the item (meaning the element is added to the end of the list)
# let's add "ducati" to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# We can start off with an empty lists and add elements to the list using the append method
# makes it easier to build lists dynamically
motorcycles_1 = []

motorcycles_1.append('honda')
motorcycles_1.append('yamaha')
motorcycles_1.append('suzuki')
print(motorcycles_1)

# You can add any new element to any position in a list by using the insert() method
# You need to specify the index of the new element and the value of the new item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'ninja')
print(motorcycles)

# Removing Elements from a list
# You can remove an item according to its position in the list or according to its value.
# For example when someone shoots down the alien you wanna make sure that the alien isn't there any more
# or when someone cancels their account on a web application you created
# you want to remove that user from the list of active users

# If you know the position (its index) of an item you can remove it using the "del" statement
motorocycles_2 = ['honda', 'yamaha', 'suzuki']
print(motorocycles_2)

del motorocycles_2 [2]
print(motorocycles_2)
# Once it's deleted you can no longer access the value

# Removing an item using the pop() method
# sometimes you just wanna use an item after you remove it from a list
# pop() method removes the last item in a list but let's you work with that item after removing it
motorcyles_3 = ['honda', 'yamaha', 'suzuki']
print(motorcyles_3)

popped = motorcyles_3.pop()
print(motorcyles_3)
print(popped)

#could be used like this
last_owned = motorcyles_3.pop()
print(f"The last bike I owned was a {last_owned}.")

# Popping items from any position in a list
# You can do this y including the index of the item u want to removie in parantheses
motorcyles_4 = ['honda', 'yamaha', 'suzuki', 'ducati']

first_owned = motorcyles_4.pop(0)
print(f"The first motorcycle I ever owned was a {first_owned.title()}.")

# You can use the remove method when you don't know the index of the item but you know the value (what it is named)
motorcyles_4 = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcyles_4.remove('suzuki')
print(motorcyles_4)

