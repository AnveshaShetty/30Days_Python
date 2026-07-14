#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages) 

#Sort the list and find the min and max age
ages.sort()
print(ages)          #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = min(ages)
print(min_age)        #19
max_age = (max(ages))
print(max_age)        #26

#Add the min age and the max age again to the list
ages.append(min_age)
print(ages)           #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19]
ages.append(max_age)
print(ages)           #[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]

#Find the median age (one middle item or two middle items divided by two)
print(ages[len(ages)//2])    #24

#Find the average age 
avg_age = sum(ages) / len(ages)
print(avg_age)                #22.75

#Find the range of the ages
range_of_age = max_age - min_age
print(range_of_age)          #7

#Compare the value of (min - average) and (max - average)
min_avg = min_age - avg_age
print(min_avg)    #-3.75
max_avg = max_age - avg_age
print(max_avg)    #3.25

print(abs(min_avg))    #3.75
print(abs(max_avg))    #3.25

print(abs(min_avg) == abs(max_avg))  #False
