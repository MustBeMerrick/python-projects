# 6) Extra Credit: Write a program that prompts the user for an
#    integer and prints out that many values of the Fibonnaci sequence.
#    The max value of the integer should be 7

user=input('Please input an integer 1-7: ')

a,b,c,d,e,f=1,2,3,5,8,13

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

#if (user!='1'or'2'or'3'or'4'or'5'or'6'or'7'):
if (user!='1')and(user!='2')and(user!='3')and(user!='4')and(user!='5')and(user!='6')and(user!='7'):
  print('no')

numbers = ['1','2','3','4','5','6','7']
coords = [[1,2,3,4,5,6,7],[1,2,3,5,8,13,21]]
print('Fun Factz:')
print('Fibz biggest value for input', coords[1][6])
print('Fibz littlest value for input', coords[0][0])
