# 4) Write a program that takes in a user input, name, and
#    says hello to them. Display an error if the input is
#    a number

#Setting up a variable that the user will specify
user=input('Please enter name: ')
try:
    x=int(user)
    print('Error')
except ValueError:
    print('Hello, ',user)
