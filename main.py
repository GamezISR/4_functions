#warm up
'''
Take two intergers as inputs num1 and num2

if one number is greater than 10 print out the two numbers added
if one number is less than 3 print out the two numbers subtracted 
if neither of these conditions print them out multiplied 
'''
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
if num1 > 10 or num2 > 10:
  print(num1 + num2)
elif num1 < 3 or num2 < 3:
  print(num1 - num2)
else:
  print(num1 * num2)

'''

#functions
#defining 
#a function with no parameters
'''
def add_two_numbers():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  print(num1 + num2)


#calling
add_two_numbers()
add_two_numbers()
add_two_numbers()
add_two_numbers()
'''


#make a function that substracts two numbers
#make a fucntion that multiplies three numbers
#call each twice
"""
def subtract():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  print(num1 - num2)

subtract()
subtract()

def multiply_three_numbers():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter a second number: "))
  num3 = int(input("Enter a third number: "))
  print(num1 * num2 * num3)

multiply_three_numbers()
multiply_three_numbers()
"""

#functions with parameters, return statements

def add_numbers(num1, num2):
  return num1 + num2

number = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))

added_numbers = add_numbers(number,number2)
print(added_numbers)

# write a function subtracting two numbers with parameters being returned to be printed
# write a function three number being mulitplied with parameters being returned to be printed



