#4)  Initialize the following dictionary:

#    carrots   : 4.50
#    apples    : 3.00
#    kiwis     : 5.00
#    olive oil : 9.99
#    coffee    : 13.50

#    Prompt the user to enter two items that are on sale, as well as their 
#    discounted prices. Then print out the new total

print(' carrots:\t 4.50\n','apples:\t 3.00\n','kiwis:\t\t 5.00\n','olive oil:\t 9.99\n','coffee:\t 13.50\n')

shopping_list={'carrots':4.50,'apples':3.00,'kiwis':5.00,'olive oil':9.99,'coffee':13.50}


print('Please advise which items are one sale and include the discounted price: ')
item1_name=input('Item 1 Name: ')
item1_price=float(input('Item 1 Price: '))
item2_name=input('Item 2 Name: ')
item2_price=float(input('Item 2 Price: '))

shopping_list[item1_name]=item1_price
shopping_list[item2_name]=item2_price

print(shopping_list)

