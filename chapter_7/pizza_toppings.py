prompt = "\nPlease enter the topping that you would like for your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(f"Adding {pizza.lower()} to your pizza!")
        