#Python Program to Check Leap Year

#Method 1: Find Leap Year using Multiple else-if Statements

year = int(input("Enter any year to check givn year is leap year or not : "))

if (year%4==0 and year%100==0 and year%400==0):
  print(year, 'is a Leap Year')
else:
  print(year, 'is not a Leap year')



#Method 2: Find Leap Year using Multiple else-if Statements


year1 = int(input("Enter year to be checked: "))
 
if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")