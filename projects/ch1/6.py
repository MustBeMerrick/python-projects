# 6) Extra Credit: Write a program that prompts the user for an
#    integer and prints out that many values of the Fibonnaci sequence.
#    The max value of the integer should be 7

user=input('Please input an integer 1-7: ')
a=1
b=2
c=3
d=5
e=8
f=13

if (user=='1'):
  print(a)

if (user=='2'):
  print(a,',', a+a)

if (user=='3'):
  print(a,',', a+a,',',a+b)

if (user=='4'):
  print(a,',', a+a,',',a+b,',',b+c)

if (user=='5'):
  print(a,',', a+a,',',a+b,',',b+c,',',c+d)

if (user=='6'):
  print(a,',', a+a,',',a+b,',',b+c,',',c+d,',',d+e)

if (user=='7'):
  print(a,',', a+a,',',a+b,',',b+c,',',c+d,',',d+e,',',e+f)