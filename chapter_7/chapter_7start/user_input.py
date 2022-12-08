print("USER INPUT AND WHILE LOOPS")
# This chapter will teach you how to accept user input so your program can then work with it
# To do this you use the input() function
# You will also learn how to keep programs running as long as users want them to
# You will use while loop to keep programs running as long as certain conditions remain true

# print("\nHow the input function works:")
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# ^ Here you see that the computer will literally respond back with exactly with what u typed in

# Writing clear promtps

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

print("\nTHe Modulo Operator")
# THe modulo operator is a useful tool when working with numerical information
# It divides one number by naother number and returns the information
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

