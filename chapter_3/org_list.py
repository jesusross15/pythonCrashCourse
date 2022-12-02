# Organizing a List 
# Sometimes your lists will be created in an unpredictable order because you can't control how
# data is provided, Here is how you can organize them in different ways, depending on the situation

# Sorting a List Permanently with the sort() Method
# Be aware that once you use the sort method the list will now be in alphabetical order and can never
# be reverted to the original order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

# You can also revert the list in reverse alphabetical order by using the (reverse=True) argument to the sort() method
cars.sort(reverse=True)
print(cars)
# The order of the list is permanently changed again 

#Sorting a list temporarily with the sorted() function
# Use this to maintain the original order of a list but present it in a sorted order
print("Here is the sorted list")
print(sorted(cars))

print("Here is the original list(well kind of orginal please look at the section above")
print(cars)

print("Same thing goes for sorted(reverse=true")

# Printing a List in Reverse Order
cars.reverse()
print(cars)
# The reverse() method changes the order of the list permanently but you can revert to the original
# order anytime by applying reverse() to the same list a second time


# Find the Length of a List
# Use the len() function to quickly find the length of a list

cool_cars = ['tesla', 'land rover', 'alpha romeo', 'bmw']
print(len(cars))
# You will find len() useful when you need to identify the number of aliens that still need to be shot down in the game
# we will build in later chapters, determine the amount of data you have to manage ina visualization
# or figure out the number of registered users on a website
print("Now we will be movng on to the Try it Yourself Section")
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
locations = ['los angeles', 'maui', 'london', 'figi', 'paris']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
print(locations)
locations.sort(reverse=True)
print(locations)
print(locations)

dude = 'dude'
print(dude)
print(len(dude))
