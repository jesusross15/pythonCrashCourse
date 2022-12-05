print("A Simple Dictionary")
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print("\nAccessing Values in a Dictionary")
# A dictionary in Python is a collection of key-value pairs. 
# Each key is connected to a vlaue, and you can use a key to acccess the value associated with that key.

# A dictionary is wrapped in braces {} with a series of key- value pairs inside the braces, as shown in the earlier example:
# A key value pair is a set of values associated with each other
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
# as you can see ths returns the value associateed with the key 'color' from the dictionary
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("\nAdding New Key-Value Pairs")
# you can add new key-value pairs to a dictionary at any time 
# this is how you would add more key-value pairs 
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# name the dictionary then in square brackets in '' put the name of the key-value and then equal that to another value

print("\nSometimes it's convenient and necessary to start with an empty dictionary")
alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

print("\nA Dictionary of Simialr Objects")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',   
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# each key is the name of the person who responds to the poll and each value is the langauge choice
# to use this dictionary given the name of a person who took the poll, you can easily look up their favorite language
 

