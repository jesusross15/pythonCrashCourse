# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a 
# dictionary
# FOr example if you wanted to describe the type of pizza that someone is ordering instead of just toppings
# you can also describe the type of crust as well as the lsit of toppings

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    
