# defining the function city_country 
def city_country(city, country):
    """try it yourself exercise 8.6"""
    country_pair = f"{city}, {country}" # value of country pair is this
    return country_pair.title() #returning the value using titlecase

world = city_country('santiago', 'chile')
print(world)

world = city_country('new york city', 'usa')
print(world)

world = city_country('los angeles', 'california')
print(world)
