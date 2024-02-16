#1)  Write a program that prompts the user to enter 3 grocery items, 
# and puts them into a list. Then, print out the list in alphabetical order

print('Please input 3 grocery items below: ')
item_1=input('\n1: ')
item_2=input('2: ')
item_3=input('3: ')

grocery_list= [item_1,item_2,item_3]
grocery_list.sort()

print('\nAlphabatized List:\t')
print(grocery_list)