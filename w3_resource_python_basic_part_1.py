#%% 1. Formatted Twinkle Poem

# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

poem = print("Twinkle, twinkle, little star,\n\
\tHow I wonder what you are!\n\
\t\tUp above the world so high,\n\
\t\tLike a diamond in the sky.\n\
Twinkle, twinkle, little star,\n\
\tHow I wonder what you are")
# %% 2. Python Version Checker
# Write a Python program to find out what version of Python you are using.
import sys
print(sys.version)
# %% 3. Current DateTime Display

# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# %% 4. Circle Area Calculator
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
import math
radius = float(input("Enter the radius of circle:"))
area_of_circle1 = round((math.pi * radius ** 2),3)
area_of_circle2 = math.pi * radius ** 2
print(f"area of circle is {area_of_circle2} and three decimal rounded to {area_of_circle1}")
# %% 5. Reverse Full Name
# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
user_name = input("Enter you Full Name:")
print(user_name[::-1])
# %% 6. List and Tuple Generator

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
number = input("Enter comma separated number:")
number = number.split(',')
print(list(number),tuple(number))
# %% 7. File Extension Extractor

# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
file_name = input("Enter the file name with extension:")
print(f"file name without extension:{file_name.split('.')}")
# %% 8. First and Last Colors
# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print(color_list[1],"\n",color_list[-1])
# %% 9. Exam Schedule Formatter4
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]}/ {exam_st_date[1]}/{exam_st_date[2]}")
# %% 10. Number Expansion Calculator
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
value = input("Enter the number to get the result:")
n = int(value)
nn = int(value*2)
nnn = int(value*3) 
print(n+nn+nnn)
# %% 11. Function Documentation Printer
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# Click me to see the sample solution
print(sum.__doc__)
# %% 12. Monthly Calendar Display

# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.
import calendar
print(calendar.month(2025,4))

# %% 13. Multi-line Here Document

# Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
print("Sample string :\
\na string that you \"don\'t\" have to escape\
\nThis\
\nis a ....... multi-line\n\
heredoc string --------> example")
# %% Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import date
start_date = date(2014, 7, 2)
end_date = date(2014, 7, 11)
delta = end_date - start_date
print(delta.days)
# %% 15. Sphere Volume Calculator
# Write a Python program to get the volume of a sphere with radius six.
from math import pi
radius_sphere = float(input('Enter the radius of a sphere:'))
volume_sphere = round(((4/3) * pi * radius_sphere ** 3),3)
print(f"Volume of sphere is:{volume_sphere}")
# %% 16. Difference from 17
# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
num = float(input("Enter the number:"))
if num >=  17:
    print(2 * abs(17 - num))
else:
    print(abs(17 - num))
# %% 17. Number Range Tester
# Write a Python program to test whether a number is within 100 of 1000 or 2000.
num = int(input("Enter the number:"))
print("Number is between 100 to 2000 ") if (num >= 100) and (num <= 2000) else print("Entered number is out of range")

# %% 18. Triple Sum Calculator
# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
if num1 == num2 == num3:
    print(f"Sum of three equal numbers is: {(num1 + num2 + num3)*3}")
else:
    print(f"Sum of three numbers is: {num1 + num2 + num3}")
# By creating a function
def sum_three_num (num1,num2,num3):
    if num1 == num2 == num3:
        print(f"Sum of three equal numbers is: {(num1 + num2 + num3)*3}")
    else:
        print(f"Sum of three numbers is: {num1 + num2 + num3}")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

sum_three_num(num1, num2, num3)
# %% 19. Prefix "Is" String Modifier
# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
string = input("Enter the string:")
string_lower =string.lower()
if string_lower.startswith("is"):
    print(f"The entered string starts with \"IS\": {string}")
else:
    print(f"Entered string does not start with \"IS\": {string}")
# By creating a function
def check_is(string):
    if string_lower.startswith("is"):
        print(f"The entered string starts with \"IS\": {string}")
    else:
        print(f"Entered string does not start with \"IS\": {string}")
string = input("Enter the string:")
check_is(string)
# %% 20. String Copy Generator
# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
string = input("Enter the string:")
num = int(input("Enter how many time you this string to be printed:"))
print(string * num)

# Creating function
def Print_string (string, num = 1):
    mul_string = string * num
    return mul_string
string = input("Enter the string:")
num = int(input("Enter how many time you this string to be printed:"))
Print_string(string, num)
# %% 21. Even or Odd Checker
# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num = float(input("Enter the string:"))
if (num % 2) == 0:
    print("Entered number is Even")
else:
    print("Entered Number is Odd")
    
# Creating a function
def even_odd(num):
    num = num % 2
    return num

num = float(input("Enter the string:"))
remainder = even_odd(num)

if remainder == 0:
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")
# %% 22. Count 4 in List
# Write a Python program to count the number 4 in a given list.
four_list = [1, 6, 7, 4, 4, 5, 7, 4]
count = 0
for i in four_list:
    if i == 4:
        count += 1
print(f"4 is present {count} present in a given list")

# Creating function
def count_four(four_list):
    count = 0
    for i in four_list:
        if i == 4:
            count += 1
    return count
count = count_four(four_list)
print(f"Using created function: 4 is present {count} present in a given list")
# %% 23. String Prefix Copies
# Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.
num = int(input("Enter the number:"))
given_string = 'mu'
#print(given_string[0:2] * num)
if len(given_string) <= 2:
    print(given_string * 2)
else:
    print("Given string length is grater than 2")
# %%24. Vowel Tester
# Write a Python program to test whether a passed letter is a vowel or not.
def vowel_check(alphabet):
    alphabet = alphabet.lower()
    if (alphabet == "a" or \
        alphabet == "e" or \
        alphabet == "i" or \
        alphabet == "o" or \
        alphabet == "u") :
        print("Entered letter is vowel")
    else:
        print("Entered letter is not vowel")
        
vowel_check("B")
# %% 25. Value in Group Tester
# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
test_data = [1, 2, 5, 8]
num_check = int(input("Enter the Number to check"))
for i in test_data:
    if i == num_check: 
        print("Entered number is present in the data")

# %%26. List Histogram
# Write a Python program to create a histogram from a given list of integers.

#%% 27. List to String Concatenator
# Write a Python program that concatenates all elements in a list into a string and returns it.
test_data = [1, 2, 5, 8]
list_con_string = ''
for i in test_data:
    if type(i) is not str:
        i = str(i)
        list_con_string += i
    else:
        list_con_string+=i
# second method
list_con_string = ''
for i in test_data:
    if not isinstance(i, str):
        i = str(i)
        list_con_string += i
    else:
        list_con_string+=i
# Third way
test_data = [1, 2, 5, 8]
list_con_string = ''
for i in test_data:
    if type(i) != str:
        i = str(i)
        list_con_string += i
    else:
        list_con_string+=i
# %% 28. Even Numbers Until 237

# Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
even_list = []
for i in numbers:
    if i <= 237:
        if i % 2 == 0:
            even_list.append(i)
print(even_list)

# Second way
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
even_list1 = []
for i in numbers:
    if (i <= 237) and (i % 2 == 0):
        even_list1.append(i)
print(even_list)
# %% 29. Unique Colors Finder
# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3 = set.difference(color_list_2, color_list_1)
# %% 30. Triangle Area Calculator
# Write a Python program that will accept the base and height of a triangle and compute its area.
num1 = float(input("Enter Base of traiangle:"))
num2 = float(input("Enter Height of traiangle:"))
area_triangle = (1/2) * (num1 * num2)
print(f"Area of triangle is:{area_triangle}")
# %% 31. GCD Calculator
# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if (num1 and num2) == 0:
    print("GCD is undefined")

elif num1 == 0 or num2 == 0:
    if num1 == 0:
        print(f"GCD between two number is {num2}")
    else:
        print(f"GCD between two number is {num1}")
elif num1 == num2:
    print(f"Both number are same so GCD is {num1}")
else:
    num1_factors = []
    num2_factors = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            num1_factors.append(i)
    for j in range(1, num2 + 1):
        if num2 % j == 0:
            num2_factors.append(j)
common_factors = [x for x in num1_factors if x in num2_factors]
print(f"GCD between two numbers is {max(common_factors)}")

import math
print(math.gcd(12,48))
    
# %%
