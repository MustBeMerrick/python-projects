# 5) Write a program that prints out the following menu
#    and answers the question chosen (after prompting for user
#    input)
#    1: Print a smiley emoticon
#    2: Multiply a number by 3
#    3: Have python say hi to you

def display_menu():
  print(' ')
  print('Plesse input 1, 2, 3, or 4')
  print('  1: Print a smiley emoticon')
  print('  2: Multiply a number by 3')
  print('  3: Have python say hi to you')
  print('  4: Exit')

def execute_command(choice):
  if choice=='1':
    print(':)')
  elif choice=='2':
    user=input('choose number to multiply by 3: ')
    user=int(user)
    a=3
    print(user*a)
  elif choice=='3':
    print('Hi')
  elif choice=='4':
    print('Goodbye')
  else:
    print('Do you know what a number is?')

lang=input('Do you want to play a game? ')
if(lang=='yes') or (lang=='Yes'):
    while True:
      display_menu()
      user_choice=input()
      execute_command(user_choice)

      if user_choice=='4':
        break

