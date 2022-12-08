# How the input function works
# The input() function pauses your program and waits for the user to enter some text
# and once Python recieves the input it assigns it t a variable to make it convenient for you to work with

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

