#Declare and print a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
print(company)
print(len(company)) #print length of the string


upper_case = (company.upper()) #change all characters into upper case
print(upper_case)


lower_case = (company.lower()) #change all characters into lower case
print(lower_case)


#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize()) #capitalize only the first letter of the string
print(company.title()) #change the font style to title 
print(company.swapcase()) #swap lower case to upper case and vice versa


#Cut(slice) out the first word of Coding For All string.
print(company[:6]) #Output: Coding 

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) #returns the index value


#Replace the word coding in the string 'Coding For All' to Python
replaced_string = (company.replace('Coding','Python')) 
print(replaced_string)


#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print(replaced_string.replace('All','Everyone')) 


#Spilt Operation 
#Split the string 'Coding For All' using space as the separator (split()) 
print(company.spilt())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.spilt(', ')) #prints: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']


#Index Operations
#What is the character at index 0 in the string Coding For All.
print(company[0]) 

#What is the last index of the string Coding For All.
print(len(company) - 1) 

#What character is at index 10 in "Coding For All" string.
print(company[10])
