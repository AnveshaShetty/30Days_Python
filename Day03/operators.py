#General number system
age = 20           #Integer
height = 5.3       #Float 
complex = 1 + 3j   #Complex Number


#Finding area and perimeter of a triangle
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area_triangle = 0.5 * base * height
print('Area of the triangle is ', area_triangle)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter_triangle = a + b + c
print('Perimeter of the triangle is ', perimeter_triangle)


#Finding area and perimeter of a rectangle
l = int(input('Enter length: '))
w = int(input('Enter width: '))
area_rectangle = l * w
perimeter_rectangle = 2 * l * w
print('Area of the rectangle is ', area_rectangle)
print('Perimeter of the rectangle is ', perimeter_rectangle)


#Finding area and circumference of a circle
pi = 3.14   #Instead of declaring pi we can also import math library and continue 
r = int(input('Enter radius of the circle: '))
area_circle = pi * r * r   #math.pi incase if you use math library
circumference_circle = 2 * pi * r
print('Area of the cirle is ', area_circle)
print('Circumference of the rectangle is ', circumference_circle)


#Finding slope, x-intercept and y-intercept 
y = 2 * x - 2
m = 2
c = -2 
slope = m 
x_intercept = - c / m 
y_intercept = c
print('Slope: ', slope)
print(f'x-intercept : ', (x_intercept,0))
print(f'y-intercept: ',  (0,y_intercept))


#Finding slope and euclidean distance
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m = y2-y1 / x2-x1
euclidean_dist = (((x1 - x2) ** 2) + ((y2 - y1) ** 2)) ** 0.5 #Eucledian formula 
print('Slope ', m)
print('Eucledian Distance: ', euclidean_dist)


#Compare the above slopes
print(slope == m)


#Finding different values of x for y equation 
# y = x ** 2 + 6 * x + 9 
x = int(input('Enter the value of x: '))
y = x ** 2 + 6 * x + 9 

if y == 0:
  print(f'x and y values are: ', (x,y))
else:
  print('Try again!!')


#Comparision operation on strings
print(len('python')!=len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')


#Type conversion and casting
length = len('python')
print(type(length))
print(float(length))
print(str(length))


#Even or odd number identification
n = int(input('Enter a number: '))
if n % 2 == 0:
  print('The entered number is even')
else:
  print('The entered number is odd')


#Floor division
floor_division = 7 // 3
value = int(2.7)
print(floor_division==value)


#Comparision Operation 
print(type('10')==type(10))

print(int('9.8')==10) #ValueError: invalid literal for int() with base 10: '9.8'


#Calculating the pay of the person
hour = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
salary = hour * rate_per_hour
print('Your weekly salary is ', salary)


#Years to seconds conversion 
age_in_years = int(input('Enter your age in years: '))
age_in_seconds = age_in_years*365.25*24*60*60 #0.25 because there will be a leap year
print('Your age in seconds ', age_in_seconds)


#Simple table
row_1= 1, 1**0, 1**1, 1**2, 1**3
row_2 = 2, 2**0, 2**1, 2**2, 2**3
row_3 = 3, 3**0, 3**1, 3**2, 3**3
row_4 = 4, 4**0, 4**1, 4**2, 4**3
row_5 = 5, 5**0, 5**1, 5**2, 5**3
print(f"{row_1} \n{row_2} \n{row_3} \n{row_4} \n{row_5}")
