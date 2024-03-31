#Python Program to Read a Number n and Compute n+nn+nnn

n = int(input('Enter a number: '))

count = 0

for i in range(1,4):
  dig = str(n)*i
  count += int(dig)
print(count)