# The program takes a number and generates all the divisors of the number.


num = int(input("Enter a number to find divisors of the number: "))

for i in range(1, num+1):
  if num%i==0:
    print(i)

#The program takes in an integer and prints the smallest divisor of the integer.

num1 = int(input("Enter a num to find smallest divisor: "))
divisors = []
for i in range(1, num1):
  if num1 % i == 0:
    divisors.append(i)
print(divisors.sort()[0])


