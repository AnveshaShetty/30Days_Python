#Create a student dictionary and add first_name, last_name, gender, age, skills, country, city and address as keys for the dictionary
student_dictionary = {
  'first_name': 'Anvesha',
  'last_name': 'Shetty',
  'gender': 'female',
  'age': '20',
  'skills': ['HTML', 'JavaScript', 'Python', 'C'],
  'country': 'India',
  'city': 'Mangalore',
  'address': {
    'street': 'xyz street',
    'pincode': '575101'
  }
}
print(student_dictionary)

#Get the length of the student dictionary
print(len(student_dictionary))

#Get the value of skills and check the data type, it should be a list
skills = list(student_dictionary['skills'])
print(type(skills))    #<class 'list'>

#Modify the skills values by adding one or two skills
skills.append('C')
print(skills)

#Get the dictionary keys as a list
keys = list(student_dictionary.keys())
print(keys)    #['first_name', 'last_name', 'gender', 'age', 'skills', 'country', 'city', 'address']

#Get the dictionary values as a list
values = list(student_dictionary.values())
print(values)    #['Anvesha', 'Shetty', 'female', '20', ['HTML', 'JavaScript', 'Python', 'C'], 'India', 'Mangalore', {'street': 'xyz street', 'pincode': '575101'}]

#Change the dictionary to a list of tuples using items() method
student_list = student_dictionary.items()
print(student_list)    #dict_items([('first_name', 'Anvesha'), ('last_name', 'Shetty'), ('gender', 'female'), ('age', '20'), ('skills', ['HTML', 'JavaScript', 'Python', 'C']), ('country', 'India'), ('city', 'Mangalore'), ('address', {'street': 'xyz street', 'pincode': '575101'})])

#Delete one of the items in the dictionary
del student_dictionary['skills']
print(student_dictionary)    #{'first_name': 'Anvesha', 'last_name': 'Shetty', 'gender': 'female', 'age': '20', 'country': 'India', 'city': 'Mangalore', 'address': {'street': 'xyz street', 'pincode': '575101'}}

#Delete one of the dictionaries
del student_dictionary
