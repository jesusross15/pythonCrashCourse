# the value that the function returns is called a return value
# after it has processed some data then it returns the value
# the return statement takes a value from inside the function and send it back to the line that called the function
# return values allow you to move much of the gurnt work into functions

def get_formatted_name(first_name, last_name): # definition of get_formatted takes as parameters a first and last name
    """Return a full name, neatly formated."""
    full_name = f"{first_name} {last_name}" # function combines these two names adds a space bw them and assigns the results to full_name
    return full_name.title() # the value of full_name is converted to title case and then returned to the calling line

musician = get_formatted_name('jimi', 'hendrix') # the return variable is assigned to the variable musician
print(musician)

#-----------------------------------------------------------------------------------------------------------------------------------------------------

print("\nReturn Values")
def get_formatted_name(first_name, last_name, middle_name=''): # this is when you can make a return value optional 
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)