# Looping through a dictionary
# A single Python dictionary can contain just a few key-value pairs or millions of pairs
# You can loop thru a dict in Python bc it can contian large amounts of data
# You can loop through all of a dictionary's key-value pairs, through its keys, or through its values

print("Looping Through All Key-Value Pairs")
# the following dictionary would store one person's username, first name, and last name:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
