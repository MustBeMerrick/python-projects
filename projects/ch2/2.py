# 2) Write a program that prompts a user for their favorite
#    programming language, and if it's python, print out
#    "you're a nerd". Otherwise print out "cool story bro"

#Ask user for input
lang=input('What is your fav programming language?')
#Respond to user input
if (lang=='python') or (lang=='Python'):
#Can't figure out how to use 'you're' in a string. python is getting confused
  print(lang,'?','You are a nerd.')
else:
  print(lang,'?','Cool story, bro.')