## Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

## Simulate printing each design, until none are left.
## Move each design to completed_models after printing.
# while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print(f"Printing model: {current_design}")
        
#    completed_models.append(current_design)
    
## Display all completed models.
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)

# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Now let's modify this list


# define the function print_models() 
# with 2 parameters; 
# a list of designs that need to be printed and a list of completed models
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
# given these lists the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models

# we define the function with one parameter: the list of the completed models. this function displays the name of each model that was printed
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# this program has the same output as the version without functions but the difference is is that this code is a lot more organized
# here were the steps:
# 1. we set up a list of unprinted designs and an empty list that will hold the completed models
# bc we have already defined our 2 functions all we have to do is call them and pass them the right arguments

# [:] slice notation makes a copy of the list to send to the function
# any changes the function makes to the list will affect only the copy leaving the original list intact


