#Use a tab escape sequence to write the following lines
#Name      Age     Country   City
#Gojo      37      Japan     Shibuya

col_name = ('Name\tAge\tCountry\tCity')
details = ('Gojo\t37\tJapan\tShibuya')
print(col_names.expandtabs(10))
print(details.expandtabs(10))
