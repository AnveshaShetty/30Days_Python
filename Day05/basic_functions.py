#Declare an empty list
empty = [] 
print(empty)

#Declare a list with more than 5 items and find the length 
movies = ['scream', 'it', 'the ritual', 'mama', 'isolated', 'weapons', 'hereditiary']
first_item, *middle_item, last_item = movies
print(len(movies))  #7
print(first_item)   #scream
print(middle_item)  #['it', 'the ritual', 'mama', 'isolated', 'weapons']
print(last_item)    #hereditiary

#Declare a list called mixed_data_types, put your(name, age, height, address)
mixed_data_type = ['Anvesha', 20, {'height:' '5.3ft'}, {'country': 'India' , 'city': 'Mangalore'}]
print(mixed_data_type)
