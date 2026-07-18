#The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
#If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_name = input("Enter a fruit: ")
if fruit_name in fruits:
  print("That fruit already exist")
else:
  fruits.append(fruit_name)
  print(fruits)
