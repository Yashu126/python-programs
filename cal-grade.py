#Python Program to Calculate Grade of a Student

marks = []
for i in range(1,6):
  m = int(input("Enter marks of {}st subject marks out of 100 : ".format(i)))
  marks.append(m)
print(marks)

avg = sum(marks)/5

if (avg >= 90):
  print('Grade : A')
elif (avg>=80 and avg<90):
  print('Grade : B')
elif (avg>=70 and avg<80):
  print('Grade : C')
elif (avg>=60 and avg<70):
  print('Grade : D')
else:
  print('Grade : F')