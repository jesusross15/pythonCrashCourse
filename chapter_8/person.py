# in this program we look at how you can return a complicated data structure like lists and dictionaries (this one is a dictionary)
# a function like this takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it 

# function build_person takes in a first name and last name and puts these values in a dictionary 
def build_person(first_name, last_name, age=None): #none is used when the variable has no specific value assigned to it (basically it's just a placeholder)
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} # value of first_name is stored with the key 'first' (same with last_name) and then the entire dictionary is returned
    if age: 
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician) # the return value is printed here with the original two pieces of textual information now stored in a dictionary

