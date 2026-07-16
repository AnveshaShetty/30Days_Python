it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
companies = ('Meta', 'Nvidia', 'Intel', 'Infosys')
it_companies.update(companies)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Infosys')
print(it_companies)

#What is the difference between remove and discard
#remove(): it removes an element but in case if the set does not contain that specific element it raises an error
#discard(): it also removes an element but in case if the set does not contain that specific element it does not raise any error
