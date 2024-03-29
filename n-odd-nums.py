lower = int(input('Enter Lower range :'))
upper = int(input("Enter Upper range : "))

for i in range(lower, upper+1):
  if i&1:
    print(i)