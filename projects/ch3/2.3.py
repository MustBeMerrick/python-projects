#3)  Prompt the user to enter 4 integers and place them into a list. 
#    Print out the reduced integer. "Reduction" can be achieved by building
#    a pyramid with the original list as the base, and each subsequent row 
#    being the sum #of the values in the row below. Example:

#                 [     35      ] <-- reduced result
#                 [   14  21    ]
#                 [  4  10  11  ]     
#   initial list: [ 3  1   9  2 ]

print('Choose 4 integers:\n')

num1=int(input('Num 1: '))
num2=int(input('Num 2: '))
num3=int(input('Num 3: '))
num4=int(input('Num 4: '))

num_list={num1,num2,num3,num4}

num1b=num1+num2
num2b=num2+num3
num3b=num3+num4
num1c=num1b+num2b
num2c=num2b+num3b
num1d=num1c+num2c

print(num_list)
print('Reduced Integer: ')
print(num1d)