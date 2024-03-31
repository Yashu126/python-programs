#Python Program to Find Prime Numbers in a Given Range

r = int(input("Enter a max range : "))

for i in range(2, r+1):
  k = 0
  for j in range(2, i//2+1):
    if (i%j==0):
      k += 1
  if k<=0:
    print(i)