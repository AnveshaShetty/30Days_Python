#Compare the values of my_age and your_age using if … else.
#Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
#Output:
#Enter your age: 30
#You are 5 years older than me.

my_age = 20
your_age = int(input("Enter your age: "))
if my_age == your_age:
     print("YAYY!! We belong to same group!!")
elif my_age < your_age:
  diff = abs(my_age - your_age)
  if diff == 1:
    print("1 year difference!")
  else:
    print(f"You are {diff} years older than me")
else:
  diff = abs(your_age - my_age)
  print(f"You are {diff} years younger tham me")
