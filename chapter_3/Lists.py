bicylces = ['trek', 'cannondale', 'redline', 'specialized']
print(bicylces)
# Because you don't want this output to be what the user sees, let's learn
# how to access the individual items in a list

# Accessing Elements in a List
# Index is also a word for the "position" that an item is in your list

# Index positions start at 0 not 1
bicylces = ['trek', 'cannondale', 'redline', 'specialized']
print(bicylces[3])

# You can also do some string methods that we learned in chapter 2 
bicylces = ['trek', 'cannondale', 'redline', 'specialized']
print(bicylces[2].title())

# You can make the index -1 to get the LAST positon in the list -2 for
# second to last -3 for third to last and so on
bicylces = ['trek', 'cannondale', 'redline', 'specialized']
print(bicylces[-1].upper())

# You can use individual values from a list just as you would any other variable
# You can use f-strings to create a message based on a value from a list
bicylces = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My cousin has a yellow {bicylces[0].title()} bike."
print(message)

# TRY IT YOURSELF
# 3-1 Names: Store the names of a few of your friends in a list called names. 
# print each person’s name by accessing each element in the list, one at a time.
names = ['Zander', 'Aaron', 'Brandon', 'Gerard', 'John']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, 
# but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized 
# with the person’s name.
names = ['Zander', 'Aaron', 'Brandon', 'Gerard', 'John']
message_1 = f"{names[2]} is so funny!"
print(message_1)

# My own list of modes of transportation and then printing a series of statements about each mode
transportation = ['car', 'train', 'plane', 'bike']
message_2 = f"I love to use my {transportation[3]} to ride around the park."
message_3 = f"I take a {transportation[2]} to the Dominican Republic every few years to visit my family." 
message_4 = f"I take my {transportation[-4]} to the gym every morning."
print(message_2)
print(message_3)
print(message_4)



