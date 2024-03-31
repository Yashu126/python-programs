#Python Program to Check Whether a Given Number is Perfect Number

num = int(input('Enter a number to check perfect number : '))

sum = 0

for i in range(1, num):
  if num%i==0:
    sum += i 
if sum==num:
  print(num, 'is a perfect number')
else:
  print(num, 'is not a perfect number')