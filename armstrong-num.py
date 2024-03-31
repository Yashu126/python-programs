# Python Program to Check Armstrong Number

num = int(input())

l =  len(str(num))

s = [int(x)**l for x in str(num)]
if sum(s) == num:
  print(num, 'is a Armstrong Number')
else:
  print(num, 'is not a Armstrong Number')


#Using Lambda
  
n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number is not an arsmtrong number. ")