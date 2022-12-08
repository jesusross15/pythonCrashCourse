# TRY IT YOURSELF 7.4 THROUGH 7.7
print("7.4 Pizza Toppings: ")
pizza = "Please enter your pizza toppings now..."
pizza += "(Enter 'quit' when you are done)"

while True:
    toppings = input(pizza)

    if toppings == 'quit':
        break
    else:
        print(f"Adding {toppings.title()} to your pizza!")

