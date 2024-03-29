'''
The program takes an upper range and lower range and finds those numbers within the range which are divisible by 7 and multiple of 5.
'''
lower = int(input('Enter a lower Range : '))
upper = int(input('Enter a upper Range : '))

[print(x) for x in range(lower, upper) if x%7==0 and x%5==0]


'''
The program prints all numbers in a range divisible by a given number.

'''
num = int(input("Enter a number to print numbers divible by number in range :"))
lower_r =  int(input("Enter a starting range : "))
upper_r = int(input("Enter a max range : "))

for i in range(lower_r, upper_r+1):
  if i% num == 0:
    print(i)