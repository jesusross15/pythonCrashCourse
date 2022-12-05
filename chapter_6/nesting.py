# Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a value in
# a dictionary
# THIS IS CALLED NESTING
# NESTING IS WHEN YOU STORE MULTIPLE DICTIONARIES IN A LIST/ WHEN YOU STORE A LIST OF ITEMS
# IN A DICTIONARY
# --------------------------------------------------------------------------------------------------------------------
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# You could expand this loop by adding an elif block taht turns yellow aliens into red, fast moving ones woeth 15 points
# each. 
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
