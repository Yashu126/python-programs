# The program prints all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.


for i in range(51):
  if i % 2 != 0 and i%3 != 0:
    print(i)