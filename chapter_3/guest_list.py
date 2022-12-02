# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, 
# who would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, 
# inviting them to dinner.

#Joe Rogan said he couldn't make it so I modified the list
dinner_guests = ['Elon Musk', 'Joe Rogan', 'Seth Rogan', 'Dustin Pedroia']
dinner_guests[1] = 'John F. Kennedy'
print(dinner_guests)
message = f"Hey {dinner_guests[1]}, would you be down to grab some dinner some time soon?"
print(message)

call = "Hey guys, it seems I have found a bigger table, the Pope and Beyonce want to come too. Just thought i'd let you guys know. Tata for now"
print(call)
dinner_guests.insert(2, 'The Pope')
dinner_guests.insert(0, 'Beyonce')
dinner_guests.append('Jeff Bezos')
print(dinner_guests)

message_1 = f"Hey {dinner_guests[3]}, I am so glad you will be able to join us, can't wait it should be a great time!"
print(message_1)

message_3 = "Darn it guys, I can only fit 2 of you haha roflcopter"
print(message_3)

sorry_1 = dinner_guests.pop(1)
print(f"hey, sorry {sorry_1}, unfortunately people hate you and you can't come anymore.")
print(dinner_guests)

sorry_2 = dinner_guests.pop(2)
print(f"hey, sorry {sorry_2}, unfortunately people hate you and you can't come anymore.")
print(dinner_guests)

sorry_3 = dinner_guests.pop(3)
print(f"hey, sorry {sorry_3}, unfortunately people hate you and you can't come anymore.")
print(dinner_guests)

sorry_4 = dinner_guests.pop(3)
print(f"Hey, dude sorry {sorry_4} unfortunately my hamster died and I have to attend his funeral.")
print(dinner_guests)

sorry_5 = dinner_guests.pop(0)
print(f"yo {sorry_5}, what's crackalackin' dawg sorry you can't come anymore.")
print(dinner_guests)

del dinner_guests[0]
print(dinner_guests)
del dinner_guests[0]
print(dinner_guests)

dinner_guests_1 = ['Elon Musk', 'Joe Rogan', 'Seth Rogan', 'Dustin Pedroia']
print(dinner_guests_1)
yes = len(dinner_guests_1)
print(yes)
print(f"Hi all, I hope all {yes} of you can make it.")