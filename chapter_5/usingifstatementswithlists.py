print("toppings.py")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")
# This is a pretty simple for loop BUT what if the pizzeria runs out of green peppers?? An if statement inside the for
# loop can handle this situation appropriately:
# if requested_topping == 'green peppers':
# print("Sorry, we are out of green peppers right now.")
# else:
# ^^^ THIS WAS WHAT WAS ADDED

print("\nCheccking that a list is not empty:")
requested_toppings_1 = []

if requested_toppings_1:
    for requested_topping_1 in requested_toppings_1:
        print(f"Adding {requested_topping_1}")
    print("\nFinished making your pizza!")
else: 
    print("Are you sure you want a plain pizza?")


