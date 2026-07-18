#Write a code which gives grade to students according to theirs scores:
#90-100, A
#80-89, B
#70-79, C
#60-69, D
#0-59, F

grades = int(input("Enter your grade: "))
if grades >= 90 and grades <= 100:
  print("A")
elif grades >= 80 and grades <= 89:
  print("B")
elif grades >= 70 and grades <= 79:
  print("C")
elif grades >= 60 and grades <= 69:
  print("D")
else:
  print("F")
