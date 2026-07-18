#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. 
#December, January or February, the season is Winter. 
#March, April or May, the season is Spring. 
#June, July or August, the season is Summer

month = input("Enter the month: ")
if month == "september" or month == "october" or month == "november":
  print("The season is Autumn")
elif month == "december" or month == "january" or month == "february":
  print("The season is Winter")
elif month == "march" or month == "april" or month == "may":
  print("The season is Spring")
else:
  print("The season is Summer")
