sandwich_orders = ['pastrami', 'blt', 'pastrami', 'baconator', 'pastrami', 'bagel']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich) 

print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(sandwich)