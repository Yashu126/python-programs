# Write a Python Program to reverse a given number.
'''
Method 1: Reverse a Number in Python using While Loop

'''

num = int(input("Enter a Nmber to reverse : "))
temp = num
rev = 0

while (num > 0):
  dig = num%10
  rev = rev * 10 + dig
  num = num // 10

print(rev)

'''  Method 2: Reverse a Number in Python using Slice Operator  '''

num2 = int(input("Enter a Nmber to reverse : "))

reversed_no = int(str(num2)[::-1])

print(reversed_no)

'''  Method 3: Reverse a Number in Python using Recursion   '''
def reverse_no(n):
  if n < 10:
    return n
  else:
    dig = n % 10
    rem_no = n//10
    reversed_num = reverse_no(rem_no)
    return int(str(dig) + str(reversed_num))


num3 = int(input("Enter a number to reverse : "))

print(reverse_no(num3))