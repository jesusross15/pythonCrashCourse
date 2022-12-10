def show_messages(yos):
    """A list containing a series of short text messages in which the function prints each text message"""
    for yo in yos:
        msg = (f"Printing text message: {yo}.")
        print(msg)

text = ['brb', 'lol', 'ttyl', 'omg']
show_messages(text)

