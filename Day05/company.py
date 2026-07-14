#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))


#Print the first, middle and last company
first, *middle, last = it_companies
print(first)     #Facebook
print(middle)    #['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']
print(last)      #Amazon


#Print the list after modifying one of the companies
it_companies[0] = 'Nvidia'
print(it_companies)   #['Nvidia', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


#Add an IT company to it_companies
it_companies.append('TCS')
print(it_companies)    #['Nvidia', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'TCS']


#Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Infosys')
print(it_companies)    #['Nvidia', 'Google', 'Microsoft', 'Apple', 'Infosys', 'IBM', 'Oracle', 'Amazon', 'TCS']


#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)    #['Nvidia', 'Google', 'Microsoft', 'APPLE', 'Infosys', 'IBM', 'Oracle', 'Amazon', 'TCS']


#Join the it_companies with a string '#;  '
it_company = '#; '.join(it_companies)
print(it_company)    #Nvidia#; Google#; Microsoft#; APPLE#; Infosys#; IBM#; Oracle#; Amazon#; TCS

it_company2 = '#; '.join(it_companies) + '#; '
print(it_company2)    #Nvidia#; Google#; Microsoft#; APPLE#; Infosys#; IBM#; Oracle#; Amazon#; TCS#;


#Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)
print('Facebook' in it_companies)


#Sort the list using sort() method
it_companies.sort()
print(it_companies)    #['APPLE', 'Amazon', 'Google', 'IBM', 'Infosys', 'Microsoft', 'Nvidia', 'Oracle', 'TCS']


#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)    #['TCS', 'Oracle', 'Nvidia', 'Microsoft', 'Infosys', 'IBM', 'Google', 'Amazon', 'APPLE']


#Slicing functions
print(it_companies[0:3])      #Slice out the first 3 companies from the list
print(it_companies[-4:-1])    #Slice out the last 3 companies from the list
print(it_companies[4:5])      #Slice out the middle IT company or companies from the list


#Deletion operation
#Remove the first IT company
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies 
it_companies.pop(len(it_companies)//2)  #IBM

#Remove the last IT company
it_companies.pop()

#Remove all IT companies
it_companies.clear()
print(it_companies)     #[]

#Destroy the IT companies list
del it_companies
print(it_companies)    #raises the error because the list has been destroyed
