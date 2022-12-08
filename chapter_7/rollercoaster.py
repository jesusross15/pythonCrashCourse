height = input("How tall are you in inches? ")
height = int(height)
# You have to use the int() function when using an integer bc Python can't distinguish between strings and numbers

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 