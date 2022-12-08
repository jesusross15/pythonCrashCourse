# Using a flag
# Lets add a flag to parrot.py

print("\nparrot.py")
prompt ="\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# This flag, which we’ll call active (though you can
# call it anything), will monitor whether or not the program should continue running:
active = True
while active: 
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

print("\n cities.py")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

