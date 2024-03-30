#The program takes the number and prints the number of digits in the number.
#Using for loop

num = int(input("Enter a number to count : "))
count = 0
for i in str(num):
  count += 1
print(count)

# Using While loop

num1 = int(input("Enter anu number : "))
cont = 0

while num1 > 0:
  cont += 1
  num1 = num1//10

print(cont)