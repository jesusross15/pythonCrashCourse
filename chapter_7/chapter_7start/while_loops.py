# The for loop takes a collection of items and executes a block of code once for each item in the collection
# In contrast, a while loop runs as long as, or while a certain condition is true

print("Counting.py")
current_number = 1
while current_number <= 20:
    print(current_number)
    current_number += 3
# The += is shorthand for current_number = current_number + 1

print("\nLetting the User Choose When to Quit")
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
# remember != means in thid case print this as long or while the user does NOT enter the word "quit"
# this program works well, except that it prints the word 'quit' as if it were an actual message. 
# Now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value

print("Using break to Exit a Loop")
prompt_1 = "\nPlease enter the name of a city you have visited: "
prompt_1 += "\n(enter 'quit' when you are finished.) "

while True:
    city = input(prompt_1)

    if city == 'quit':
        break
    else:
        print(f"I'd love to do to go to {city.title()}!")
# To exit a loop immedietely without running any remaining code in the loop, regardless of the results of any conditional test, use the 'break' statement

print("\nUsing Continue in a Loop")
number = 0 
while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

