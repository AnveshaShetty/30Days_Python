#Use map to create a new list by changing each country to uppercase in the countries list

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def upper_case(country):
  return country.upper()

country_uppercase = map(upper_case, countries)
print(list(country_uppercase))
