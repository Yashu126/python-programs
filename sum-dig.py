#The program takes in a number and finds the sum of digits in a number.

num = int(input("Enter a number to add : "))
su_no = 0

for i in str(num):
  su_no += int(i) 
print(su_no)

# using while loop

num2 = int(input("Enter a num to add : "))
result = 0
while num2>0:
  dig = num2%10
  result = result + dig
  num2 = num2//10
print(result)

#The program takes a number and finds the sum of the digits of the number recursively.

l=[]
def sum_digits(b):
    if(b==0):
        return l
    dig=b%10
    l.append(dig)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))