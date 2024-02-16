#2)  Write a program that initializes the following list:
  
#    ['carrots', 'apples', 'kiwis', 'olive oil', 'coffee']
  
#    Then prompt the user to enter an item and append it to the list.
#    Print this new list in alphabetical order

shopping_list=['carrots', 'apples', 'kiwis', 'olive oil', 'coffee']
print('\n')
print(shopping_list)
shopping_list_add=input('\nPlease add an item to this list: ')


shopping_list.append(shopping_list_add)
shopping_list.sort()

print('\nNew Alphabatized List:')
print('')
print(shopping_list)
print('')