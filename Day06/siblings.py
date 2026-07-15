#Create an empty tuple
empty_tuple = ()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers 
brothers = ('Adi', 'Achu')
sisters = ('Anvi', 'Advi')    
print(brothers)
print(sisters)

#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)    #('Adi', 'Achu','Anvi', 'Advi')

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Dad', 'Mom')
family_members = siblings + parents
print(family_members)    #['Adi', 'Achu', 'Advi', 'Anvi', 'Dad', 'Mom']

#Unpack siblings and parents from family_members
*siblings , dad, mom = family_members
print(siblings)  #['Adi', 'Achu', 'Anvi', 'Advi']
print(dad)       #Dad
print(mom)       #Mom
