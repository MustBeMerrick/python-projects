#5)  Create a game where the user inputs 3 integers: a, b, and c. A new number is generated by performing 
#    a*b+c. Depending on if the number is odd or even, the values of a,b,c are updated differently:

    #odd:
    # a = a + 1
    # b = b + 2
    # c = c * 2
    #even:
    # a = b + 1
    # b = c
    # c = a (previous value of a)

    #The game is over when the resulting number is greater than 1,000. Print out a,b,c for each iteration

#intro
print('Let\'s play a game')
print('Please choose three numbers below:')

#user input
num1=int(input('First Number: '))
num2=int(input('Second Number: '))
num3=int(input('Third Number: '))

#print input and complete initial result
print(num1,num2,num3)
result=num1*num2+num3

#print initial result
print('result:', result)

#while loop condition
while result < 1000: 

  if (result % 2 != 0):
    num1=num1+1
    num2=num2+2
    num3=num3*2

  else:
    #include _temp to sotre copy of num1 for later use
    num1_tmp=pum1
    num1=num2+1
    num2=num3
    num3=num1_tmp
#new result and print
  result=num1*num2+num3
  if result < 1000:
    print('new result:',result)
  else:
    print('end')






 