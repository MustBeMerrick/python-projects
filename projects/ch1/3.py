# 3) Write a program that takes two user inputs, score1 and
#    score2, and prints out the higher score

#Create two variables based on user input
Score1=input('Enter Score1:')
Score2=input('Enter Score2:')
#Display the larger number
#Including function type = integer so that multiple digit numbers are recognized
try:
  if int(Score1)>int(Score2):
    print('Highscore: ',Score1)
  if int(Score1)<int(Score2):
    print('Highscore: ',Score2)
  if int(Score1)==int(Score2):
    print('Draw')
except ValueError:
  print('no')
  