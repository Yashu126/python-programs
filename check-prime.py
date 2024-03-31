# Python Program to Check Prime Number

#Method 1: Prime Number in Python using For Loop


num = int(input('Enter a number to check if the given no is prie or not : '))
k = 0
for i in range(2, num//2+1):
  if num % i == 0:
    k += 1
if (k <=0):
  print(num, 'is a prime number')
else:
  print(num, 'is not a prime number')


#Method 2: Prime Number Program in Python using Recursion
  
def check(n, div=None):
  if div is None:
    div = n-1
  while div>=2:
    if n%div==0:
      print('Number is not a prime')
      return False
    else:
      check(n, div-1)
  else:
    print('Number is a prime number')
    return True


n = int(input())
check(n)