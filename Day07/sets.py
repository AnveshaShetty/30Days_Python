age = [22, 19, 24, 25, 26, 24, 25, 24]

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
print(set_age)    #{19, 22, 24, 25, 26}
print(len(age))
print(len(set_age))

if(len(age) == len(set_age)):
  print("Length of both (list and set) are equal")
elif(len(age) > len(set_age)):
  print("Length of list is greater than set")
else:
  print("Length of set is greater than list")    #Length of list is greater than set

#Explain the difference between the following data types: string, list, tuple and set
#string: collection of items where various functions can be performed
#list: collection of ordered items which can be modified, duplication is allowed here
#tuple: collection of ordered items which cannot be modified, duplication is allwed
#set: coleection of unordered items which cannot be modified (but new items can be inserted), duplication is not allowed
  
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
set_sentence= set(sentence)
print(set_sentence)    #{'teacher', 'inspire', 'love', 'people', 'I', 'am', 'teach', 'and', 'to', 'a'}
print(len(set_sentence))    #10
