# The modulo operator
# basically gives you the value that is left over from teh division
# So if you do 10 % 3
# 3 fits into 10 3 times and one left over so the modulo operator in this situation will be 1
# more examples:
# 4 % 3 = 1
# 5 % 3 = 2
# 6 % 3 = 0
# 7 % 3 = 1

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# IF YOU WANT TO KNOW IF ITS EVEN THE MODULO OPERATOR OF EVEN NUMBERS IS IF NUMBER % 2 == 0

