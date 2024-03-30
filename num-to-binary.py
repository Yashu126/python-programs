#  Python Program to Print Binary Equivalent of an Integer using Recursion


l = []

def convert(n):
  if (n == 0):
    return l
  dig = n%2
  l.append(dig)
  convert(n//2)

num = int(input("Enter a number: "))
binary_no = ''
convert(num)
l.reverse()
for i in l:
  binary_no += str(i)
print(int(binary_no))

#  Python Program to Print Binary Equivalent of an Integer without using Recursion

num1 = int(input("Enter a number : "))
b_no = []
while num1 > 0:
  dig = num1 % 2
  b_no.append(dig)
  num1 = num1//2
b_no.reverse()
for i in b_no:
  print(i, end=" ")