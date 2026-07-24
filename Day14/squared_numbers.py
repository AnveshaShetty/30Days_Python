#Use map to create a new list by changing each number to its square in the numbers list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(numbers):
  return numbers**2

squared_numbers = map(square,numbers)
print(list(squared_numbers))
