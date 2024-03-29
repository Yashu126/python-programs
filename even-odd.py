''' 
Check Even or Odd in Python using if-else and Modulus Operator

Time Complexity: O(1)
The time complexity of the program being O(1) indicates that the execution time remains constant, regardless of the input size.

Space Complexity: O(1)
The space complexity of the program being O(1) signifies that the code utilizes a fixed amount of memory to store the input number and other variables, irrespective of the input number’s magnitude.
'''

n = int(input('Enter a number : '))

if n % 2 == 0:
  print(n, 'is a Even Number')
else:
  print(n, 'is a Odd Number')


# ---------------------------------------------------------------------------------------------------------------------

'''  
Check Even or Odd in Python using Bitwise Operator

Time Complexity: O(1)
The time complexity of the code is O(1) since it has a constant number of operations.

Space Complexity: O(1)
The space complexity is also O(1) as it uses a fixed amount of memory regardless of the input size.

'''
n2 = int(input('Enter a number : '))

if n2 & 1:
  print(n2, 'is a Odd Number')
else:
  print(n2, 'is a Even Number')

#--------------------------------------------------------------------------------------------------------------------

'''
Check Even or Odd in Python using Recursion

Time Complexity: O(n/2)
The time complexity of the code is O(n/2) since the function recursively calls itself n/2 times in the worst case.

Space Complexity: O(n)
The space complexity is O(n) due to the recursive function calls that create a stack frame for each call.

'''

n3 = int(input('Entr a nuumber : '))
def check(n3):
  if n3 < 2:
    return (n3 % 2 == 0)
  return check(n3-2)
if check(n3) == True:
  print(n3, 'is a Even Number')
else:
  print(n3, 'is a Odd Number')

# -------------------------------------------------------------------------------------------------------------------

'''
Check Even or Odd in Python using Lambda Function

Time Complexity: O(1)
The time complexity of the code is O(1) since the lambda function executes in constant time.

Space Complexity: O(1)
The space complexity is also O(1) as it uses a fixed amount of memory regardless of the input size.

'''
check_num = lambda n4 : "Even" if n4 % 2 == 0 else "Odd"

n4 = int(input('Entr a nuumber : '))

result = check_num(n4)

print(n4, 'is an', result, 'Number')

#--------------------------------------------------------------------------------------------------------------------