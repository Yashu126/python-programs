# Python Program to Check if a Date is Valid and Print the Incremented Date if it is

'''
This is a Python Program to check if a date is valid and print the incremented date if it is.

Problem Description
The program takes in a date and checks if it a valid date and prints the incremented date if it is.

Problem Solution
1. Take in the date of the form: dd/mm/yyyy.
2. Split the date and store the day, month and year in separate variables.
3. Use various if-statements to check if the day, month and year are valid.
4. Increment the date if the date is valid and print it
5. Exit.
'''
date=input("Enter the date: ")
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
if(mm<1 or mm>12):
    print("Date is invalid.")
elif(dd<1 or dd>max1):
    print("Date is invalid.")
elif(dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print("The incremented date is: ",dd,mm,yy)
elif(dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print("The incremented date is: ",dd,mm,yy)
else:
    dd=dd+1
    print("The incremented date is: ",dd,mm,yy)