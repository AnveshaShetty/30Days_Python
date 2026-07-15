#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana','apple','strawberry','blue berry','mango')
vegetables = ('cucumber', 'lettuce', 'carrot', 'capsicum')
animal_products = ('paneer', 'cheese', 'meat')
food_stuff_tp = fruits + vegetables + animal_products 
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(type(food_stuff_lt))    #<class 'list'>

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_lt) % 2 == 0:
    middle = food_stuff_lt[len(food_stuff_lt)//2 - 1 : len(food_stuff_lt)//2 + 1]
else:
    middle = food_stuff_lt[len(food_stuff_lt)//2]

print(middle)    #['cucumber', 'lettuce']

#Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)    #['banana', 'apple', 'strawberry']
print(last_three)     #['paneer', 'cheese', 'meat']

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
