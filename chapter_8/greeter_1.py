# Using a function with a while loop.

def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    print("\nPLease tell me your name: ")
    print("enter 'q' at eny time to quit.")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    fullname = get_formatted_name(f_name, l_name)
    print(f"\nHello, {fullname}!")