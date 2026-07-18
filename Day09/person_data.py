#Here we have a person dictionary. 
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if ('skills' in person) == True:
  middle = len(person['skills']) // 2
  print(person['skills'][middle])    #Node
  
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if ('skills' in person) == True:
  if ('Python' in person['skills']) == True:
    print("Python is present in the sills section")    
else:
  print("Complete python!!!")    #Python is present in the sills section
  
#If a person skills has only JavaScript and React, print('He is a front end developer'), 
#if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#else print('unknown title')
if len(person['skills']) == 2:
  if ('JavaScript' in person['skills'] and 'React' in person['skills']):
    print("He is a frontend developer")
else:
  if ('Node' in person['skills'] and 'MongoDB' in person['skills'] and 'React' in person['skills']):
    print('He is a fullstack developer')
  elif ('Node' in person['skills'] and 'MongoDB' in person['skills'] and'Python' in person['skills']):
    print('He is a backend developer')
  else:
    print("Unkown title")    #He is a fullstack developer

#If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if ('is_married' in person) == True and person['country'] == 'Finland':
  print('Asabeneh Yetayeh lives in Finland. He is married.')
