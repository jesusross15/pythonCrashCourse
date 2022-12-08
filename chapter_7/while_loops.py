# A while loop runs as long as a certain condition is true
print("counting.py")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\nparrot.py")
prompt ="\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    # this program works well but an if test fixes the fact that the program prints quit when you 
    # input quit 
    # don't worry i added it right below this
    if message != 'quit':
        print(message)

