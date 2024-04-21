#--- Free Response ---
#1)  What is the difference between global and local variables?
#
#    'Global' and 'local' refers to the scope of variables within and outside of functions.
#     Global scope: a variable created outside of a function that can be referenced
#       from within the function. For example, say a function's job is to increment value 'a' by 1 and store that in b.
#       The code initializes a=1. The first time the function is called will produce b=2. Say later on in the code 'a'
#       is changed to value 2. If used again, the function will now produce b=3. This can be a problem if we don't want
#       to change the value of 'a' within the function. Maybe value 'a' serves a different purpose outside of the function.
#     Local Scope: a variable created inside a function. This only lives inside the function and cannot be referenced
#       outside the function. This is useful because changes in variables inside the functions won't alter how the code 
#       surrounding the functions work. Local variables in functions allows the functions to be plugged in anywhere in the code.
#       You can use the same function multiple times in code without the functions affecting one another.
#
#2)  Why are global variables not recommended when coding?
#
#       Global variables can be problematic because they are global. They supersede variables inside functions, and can alter how those
#       functions work. Sometimes, different portions of the code require different variable values. It can become messy and comfusing
#       when a change to one global variable affects all other parts of the code. You would need to ensure that this variable works throughout 
#       the code and in every case.
#
#3)  If a function declaration has 3 arguments/parameters, what is:
#
#  a)  the minimum number of arguments required to be passed to that function call if 1 argument has a default value defined?
#
#       The number of values used when calling a function must match the number of paramters/arguments in the function (if nothing is defined). So, if one of the 
#       parameters already has a specified value, then we would need to pass at least 2 argument values to the function (in the right order/or defined properly).
#
#  b)  the minimum number of arguments required to be passed to that function call if 2 arguments have default values defined?
#
#       Same answer as above, except we would need to pass at least 1 argument value.
#
#  c)  the minimum number of arguments required to be passed to that function call if all 3 arguments have default values defined?
#
#       You can call the function without passing argument values because the function already has all the information it needs. However, if you want
#       to pass arguments to the function that are different than what was initially defined - you will need to pass those new argument values to the function.

#
#  d)  the maximum number of arguments that may be passed to that function call?
#
#       Maximum number of arguments that can be accepted = 3 because that is what the function declared.
#
#4)  What is the difference between arguments by position and passing arguments by name?
#
#     Passing argument by positions requires that you give the argument value to the function in the same order as what the function declared.
#     This way you don't need to name the argument values because python will automatically pass the arguments by position. Passing the arguments
#     by name requires you to specify the name, but also allows you to pass the argument values in any order. You are telling python what's what.
#
#--- Coding Exercises ---
#5)  Define a function called inc2 that takes in a number and returns that number incremented by 2. In the main body of your code, prompt the user for a number, call the function, and print the result
#
#
#num=input('Please enter a number: ')

#def inc2(num):
#  if not num.isdigit() :
#    return 'Invalid Entry'
#
#  num = int( num )
#  return num +2
#
#print('Number Entry + 2 = ', inc2(num))
#
#
#6)  Define a function called product that takes in 2 numbers and returns their product. In the main body of your code, prompt the user for two numbers, call the function, and print the result
#
#num1=input('Please enter a number: ')
#num2=input('Please enter another number: ')
#
#
#def product(num1,num2):
#  if not num1.isdigit():
#    return 'Invalid Entry'
#  if not num2.isdigit():
#    return 'Invalid Entry'   
#
#  num1 = int( num1 )
#  num2 = int( num2 )
#  return num1 * num2
#
#print('Product of Entries = ', product(num1,num2))
#
#7)  Define a function called calculator that takes in 2 numbers and a string. The function does the following:
#      string = add      : return the sum of the two numbers
#      string = subtract : return the difference between the first and second numbers (first - second)
#      string = multiply : return the product of the two numbers
#      string = divide   : return the quotient of the first number divided by the second number
#      string = mod      : return the remainder when the first number is divided by the second number
#  In your main body code, prompt the user for two numbers and a string, execute the function, and print the result
#
#num1=input('Please enter an integer for our calculator: ')
#num2=input('Please enter another integer for calculator: ')
#string1=input('Enter instructions (add, subtract, multiply, divide, or mod): ' )
#
#def calculator(num1,num2,string1):
#  if not num1.isdigit():
#    return 'Invalid Entry'
#  if not num2.isdigit():
#    return 'Invalid Entry'
#
#  num1=int(num1)
#  num2=int(num2)
#
#  if string1=='add':
#    return num1+num2
#  if string1=='subtract':
#    return num1-num2  
#  if string1=='multiply':
#    return num1*num2
#  if string1=='divide':
#    return num1/num2
#  if string1=='mod':
#    return num1%num2
#
#print('Result: ', calculator(num1,num2,string1))
#
#
#8)  Use the function you defined in #7 to prompt the user for 8 numbers and 4 strings. Call the function 4 times. The first two numbers and first string will be arguments to the first function call, the second two numbers and second string will be arguments to the second function call, etc.
#
#num1=input('Please enter an integer for our calculator: ')
#num2=input('Please enter another integer for calculator: ')
#string1=input('Enter instructions (add, subtract, multiply, divide, or mod): ' )
#
#def calculator(num1,num2,string1):
#  if not num1.isdigit():
#    return 'Invalid Entry'
#  if not num2.isdigit():
#    return 'Invalid Entry'
#
#  num1=int(num1)
#  num2=int(num2)
#
#  if string1=='add':
#    return num1+num2
#  if string1=='subtract':
#    return num1-num2  
#  if string1=='multiply':
#    return num1*num2
#  if string1=='divide':
#    return num1/num2
#  if string1=='mod':
#    return num1%num2
#
#  print('Result: ',calculator(num1,num2,string1))
#
#for i in range(3):
#  num1=input('Please enter an integer for our calculator: ')
#  num2=input('Please enter another integer for calculator: ')
#  string1=input('Enter instructions (add, subtract, multiply, divide, or mod): ' )
#  print('Result: ',calculator(num1,num2,string1))

#9) Use the function you defined in #7. Prompt the user for two numbers and an operation indefinitely. After the result is computed and displayed, ask the user if they want to continue and repeat as needed.

#num1=input('Please enter an integer for our calculator: ')
#num2=input('Please enter another integer for calculator: ')
#string1=input('Enter instructions (add, subtract, multiply, divide, or mod): ' )
#
#def calculator(num1,num2,string1):
#  if not num1.isdigit():
#    return 'Invalid Entry'
#  if not num2.isdigit():
#    return 'Invalid Entry'
#
#  num1=int(num1)
#  num2=int(num2)
#
#  if string1=='add':
#    return num1+num2
#  if string1=='subtract':
#    return num1-num2  
#  if string1=='multiply':
#    return num1*num2
#  if string1=='divide':
#    return num1/num2
#  if string1=='mod':
#    return num1%num2
#
#print('Result: ',calculator(num1,num2,string1))
#answer1=input('Do you want to exit? Y/N: ')
#
#while answer1!='Y':
#    num1=input('Please enter an integer for our calculator: ')
#    num2=input('Please enter another integer for calculator: ')
#    string1=input('Enter instructions (add, subtract, multiply, divide, or mod): ' )
#    print('Result: ',calculator(num1,num2,string1)) 
#    answer1=input('Do you want to exit? Y/N: ')
#    if answer1!='Y' and answer1!='N':
#      print('Huh?')  
#    if answer1=='Y':
#      break 








