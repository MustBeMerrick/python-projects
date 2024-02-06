a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

res = (a * b) + c

if (res < 1000):
  print("a =", a, ", b =", b, ", c =", c, "   result =", res)
  while True:
    # if result is even
    if (res % 2 == 0):
      a_tmp = a
      a = b + 1
      b = c
      c = a_tmp
  
    else: # else if result is odd
      a += 1
      b += 2
      c *= 2
  
    res = (a * b) + c
    
    # if result is still < 1000, print it
    if (res < 1000):
      print("a =", a, ", b =", b, ", c =", c, "   result =", res)
  
    # otherwise, don't print and exit
    else:
      break