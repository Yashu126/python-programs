'''
Write a Python Program to check whether a given number is a palindrome.
'''

'''
 Method 1: Palindrome Program in Python using While Loop

Time Complexity: O(log n)
The time complexity of the program is O(log n) as it depends on the number of digits in the input.

Space Complexity: O(1)
The space complexity of this program is O(1) because it uses a constant amount of extra space to store the variables temp, rev, and dig.
'''

number = int(input("Enter any number to check if the given nmber is Palindrome : "))
p_num = 0
temp = number

while(number>0):
  dig = number % 10
  p_num = p_num*10+dig
  number = number//10

if (temp==p_num):
  print(p_num, 'is a Palindrome')
else:
  print(p_num, 'is not a Plaindrome')

#--------------------------------------------------------------------------------------------------------------------
  
'''
Method 2: Palindrome in Python using Built-in Function

Time complexity: O(n)
The time complexity of the program is O(n), where n is the number of digits in the number. This is because the str() function takes O(n) time to convert the number to a string, the reversed() function takes O(n) time to reverse the string, and the ”.join() function takes O(n) time to concatenate the strings.

Space complexity: O(1)
The space complexity of the program is O(1), because it only uses a constant amount of extra space to store the variables n, str(n), and ”.join(reversed(str(n))).

'''
def check_palindrome(n):
  return str(n) == ''.join(reversed(str(n)))

num2 = int(input("Enter a Number: "))

if check_palindrome(num2):
  print(num2, 'is a Palindrome')
else:
  print(num2, 'is not a Plaindrome')


'''
Method 3: Palindrome in Python using Recursion

Time Complexity: O(log10(n))
The program has a time complexity of O(log10(n)) because it processes each digit of the input number once, and the number of digits is approximately log10(n).

Space Complexity: O(log10(n))
The space complexity is also O(log10(n)) since the recursion depth and stack memory usage depend on the number of digits in the input.

'''
def is_palindrome(n, temp, rev=0):
  if (n==0):
    if (rev== temp):
      return "is a Palindrome"
    else:
      return 'is not a palindrome'
  else:
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
    return is_palindrome(n, temp, rev)
num3 = int(input("Enter any number to check a number is Palindrome : "))
result = is_palindrome(num3, num3)
print(num3, result)


'''
Method 4: Palindrome in Python using Slicing

Time Complexity: O(N)
The time complexity of this program is O(N), where N is the number of digits in the input number n. String slicing and string comparisons both have linear time complexity.

Space Complexity: O(N)
The space complexity is also linear and depends on the input’s size, used mainly for storing the reversed string reversed_str.

'''
def is_a_palindrome(n):
  num_str = str(n)
  reversed_num = num_str[::-1]
  return num_str == reversed_num
num4 = int(input("Enter a number : "))

if is_a_palindrome(num4):
  print(num4, 'is a plaindrome Number')
else:
  print(num4, 'is not a plaindrome Number')
