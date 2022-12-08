# To keep track of many users and pieces of information we need to use lists and dictionaries
# with while loops

# Start with the users that need to be verified
# and an empty list to hold confirmed users

unconfirmed_users = ['zander', 'aaron', 'john']
confirmed_users = []

# Verify each user unil there are no more unconfirmed users.
# move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
 
# Removing all instances of specific values from a list
# say you have a list of pets with the value 'cat' repeated several times, you can actually run a while loop
# like the one below

print("\npets.py")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)