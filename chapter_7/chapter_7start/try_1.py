# Try it yourself 

print("7.1 Rental Car")
car = input("What kind of car would you like? ")
print(f"\nLet me see if I can find you a {car}!")

print("\n7.2 Restaurant Seating")
restaurant = input("Good Evening, how many? ")
restaurant = int(restaurant)

if restaurant > 8:
    print("\nI'm sorry but there will be a wait time of 30 minutes.")
else: 
    print("\nAlrighty, come right this way!")

print("\n7.3 Multiples of Ten:")
number = input("Enter a number and I'll tell you if it's a multiple of 10 or not! ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multple of 10!")
else:
    print(f"\nThe number {number} is NOT a multiple of 10")

