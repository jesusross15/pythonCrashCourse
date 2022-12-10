# defining the function
def describe_city(city, country='dominican republic'):
    """Describe a City."""
    print(f"{city.title()} is in {country.title()}.") # this is the message that it prints

describe_city('santo domingo') # calling the function to print santo domingo
describe_city('la vega') # calling the function to print la vega
describe_city('sydney', 'australia')
# calling the function to print a different city in a different country
