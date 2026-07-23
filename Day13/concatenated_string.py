#Change the following list to a list of concatenated strings:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_string = [{'country': country.upper(), 'city': city.upper()} for [(country,city)] in countries]
print(country_string)
