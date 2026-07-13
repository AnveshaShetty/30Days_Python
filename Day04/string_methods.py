string = 'You cannot end a sentence with because because because is a conjunction'

#Use index or find to find the position of the first occurrence of the word 'because'
print(string.index('because')) #31

#Use rindex to find the position of the last occurrence of the word 'because'
print(string.rindex('because')) #47

#Slice out the phrase 'because because because' 
print(string[31:54])

#Find the position of the first occurrence of the word 'because'
print(string.find('because')) 
