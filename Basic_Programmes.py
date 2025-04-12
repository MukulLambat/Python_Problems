
#%% Hello World
# Write a program that simply prints "Hello, World!" to the screen.
print("Hello, World!")

#%% Basic Arithmetic
# Write a program that stores two numbers in variables and prints the result of their addition, subtraction, multiplication, division, integer division, exponentiation, and modulo.
num1 = float(input("Enter First Number:"))
num2 = float(input('Enter Second Number:'))
print(f"Addition of {num1} and {num2} = ",num2 + num2)
print(f"Multiplication of {num1} and {num2} = ",num2 * num2)
print(f"Division of {num1} and {num2} = ",num2 / num2)
print(f"Integer Division (Floor division) of {num1} and {num2} = ",num2 // num2) # Quotient without remainder
print(f"Exponentiation of {num1} and {num2} = ",num2 ** num2)
print(f"Modulo of {num1} and {num2} = ",num2 % num2)

#%% Taking User Input
# Write a program that asks for your name and age, then displays a greeting using the provided name and age.
# Check Even or Odd
name = input("Enter you name: ")
age = int(input("Enter you age: "))
print(f"Hello, Greetings of Day {name}({age}) ")
#%% Check Even or Odd
# Write a program that takes an integer from the user and determines if it is even or odd.
num = float(input("Enter the number: "))
print(f"{num} is Even.") if (num % 2 == 0) else print(f"{num} is odd")

#%% Sum of First N Natural Numbers
# Write a program that reads a positive integer n and calculates the sum of the first n natural numbers.
num = int(input("Enter the number: "))
sum = 0
for i in range(num+1):
    sum = sum + i
print(f"Sum Of first {num} Natural Numbers is:", sum)
# using Formula
sum_for = num * (num + 1)/2
print(f"Sum Of first {num} Natural Numbers is:", sum_for)

#%% Factorial of a Number
# Write a program that asks for a positive integer and computes its factorial.
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"Factorial of a {num} is:", factorial)
#%% Fibonacci Series
# Write a program that generates and prints the Fibonacci sequence up to n terms (where n is input by the user).
num = int(input("Enter the number: "))
N1, N2 = 0, 1
for i in range(num+1):
    print(N1  , end = ",") # Here separator in print will not work because it only works with two arguments. 
    nth = N1 + N2         # So with end there will be a comma at the end
    N1 = N2               # To remove tha we can use list
    N2 = nth
# Second way to remove comma in the series
num = int(input("Enter the number: "))
N1, N2 = 0, 1
fibonacci_series = list()
for i in range(num+1):
    fibonacci_series.append(str(N1))
    Nth = N1 + N2
    N1 = N2
    N2 = N1 + Nth
print(",".join(fibonacci_series))

#%% Swap Two Variables
# Write a program that swaps the values of two variables without using a temporary variable.
num1 = float(input("Enter First Number:"))
num2 = float(input('Enter Second Number:'))
num3 , num4 = num2 , num1
print(f"After swaping {num1} becomes {num3} and {num2} becomes {num4}")
# using Temporary Variable
temp = num1
num1 = num2
num2 = temp
print(f"After swaping {num1} becomes {num2} and {num2} becomes {num1}")
#%% Reverse a String
# Write a program that reverses a given string.
s = 'mukul'
print(s[::-1])
#%% Check Palindrome (String)
# Write a program to check if a given string is a palindrome (reads the same forwards and backwards).
pal_string = input("Enter the string")
reverse_pal_string = pal_string[::-1]
print(f"{pal_string} is palindrome") if (pal_string == reverse_pal_string) else (f"{pal_string} is not palindrome")

#%% Armstrong Number
# Write a program that checks if a given number is an Armstrong (Narcissistic) number.
arm_number = int(input("Enter the number"))
arm_string = str(arm_number)
sum = 0
updated_arm_number = arm_number
for i in arm_string:
    last_digit =  updated_arm_number % 10
    sum = sum + last_digit ** (len(arm_string))
    updated_arm_number = updated_arm_number // 10
print("Number is Armstrong") if (arm_number == sum) else print("Not a armstrong")

#%% Check Prime Number
# Write a program that determines if a given number is prime.
num = int(input("Enter the number: "))
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i == 0):
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number") # Use of special case with else 
else:    
    print(f"{num} is not a prime number")
#%% Find the Largest Among Three Numbers
# Write a program that takes three numbers and prints which one is the largest.
num1 = float(input("Enter First Number:"))
num2 = float(input('Enter Second Number:'))
num3 = float(input("Enter Third Number:"))
if (num1 >= num2 and num1 >=num3):
    print(f"{num1} is greatest number")
elif (num2 >= num1 and num2 >= num3):
    print(f"{num2} is greatest number")
else:
    print(f"{num3} is greatest number")
#%% Sum of Digits of a Number
# Write a program that calculates the sum of all digits of a given number.
num1 = int(input("Enter First Number:"))
num1_str = str(num1)
sum = 0
update_num = num1
for i in range(len(num1_str)):
    last_digit = update_num % 10
    sum += last_digit
    update_num = update_num // 10
print(f"Sum of digits of {num1} is:",sum)

#%% Check Leap Year
# Write a program that checks if a given year is a leap year.
year = int(input("Enter year to check for leap year:"))
if ((year % 4 == 0) and (year % 100 != 0)):
    print(f"{year} is a leap year")
elif (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
# Second way to check for leap year
year = int(input("Enter year to check for leap year:"))
if (((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0))):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#%% ASCII Value of a Character
# Write a program that takes a single character and displays its ASCII (or Unicode) value.
# Program 16: ASCII Value of a Character
char = input("Enter a single character: ")

if len(char) == 1:
    print("The ASCII value of", char, "is", ord(char))
else:
    print("Please enter exactly one character.")

#%% Guess the Number (Simple Game)
# Write a simple game where the user guesses a secret number (hardcode the secret number in your program).
secret_number = 14
num = int(input("Enter the number between 1 to 20 to win the guess game"))
if secret_number == num:
    print("You guessed the number correctly")
else: 
    print("You guessed the number incorrect, try again!")
#%% Multiplication Table
# Write a program that prints the multiplication table of a chosen number up to 10 terms.
num = int(input("Enter number to write table"))
print(f"Multiplication Table of {num}:")
for i in range(1, 11, 1):
    print(f"{num} * {i} = ",num * i)
#%% Simple List Operations
# Write a program that demonstrates basic operations on a list: creating, appending items, accessing elements, and removing items.
my_list = []

# Adding items to the list
my_list.append("Apple")
my_list.append("Banana")
my_list.append("Cherry")

print("Current List:", my_list)
print("First item:", my_list[0])

# Remove item
my_list.remove("Banana")
print("List after removing 'Banana':", my_list)

#%% Read and Write to a File
# Write a program that writes some text to a file, then reads and prints that file’s content.
# Dictionary Usage
# Write a program that creates a dictionary with some initial key-value pairs, prints specific values by key, updates an existing value, and adds a new key-value pair.



#%% Simple Calculator (Using If-Else)
# Write a program that takes two numbers and an operator (+, -, *, /) from the user, then performs the corresponding calculation.
N1, N2 = map(float, input("Enter two numbers: ").split(' '))
operation = input("Enter which operation you want to perform from (+, -, *, /)")
if operation == "+":
    print (f"Addition of {N1} and {N2}: ", N1 + N2)
elif operation == "-":
    print (f"Subtraction of {N1} and {N2}: ", N1 - N2)
elif operation == "*":
    print (f"Multiplication of {N1} and {N2}: ", N1 * N2)
elif operation == "/":
    print (f"Division of {N1} and {N2}: ", N1 / N2)
else:
    print("Select appropriate operator")
# Counting Vowels in a String
# Write a program that counts and displays the number of vowels in a user-provided string.
# Rock, Paper, Scissors
# Write a simple Rock-Paper-Scissors game where the user plays against the computer (use random choice for the computer).
# Finding the Longest Word in a Sentence
# Write a program that takes a sentence from the user, splits it into words, and prints the longest word.

# %%
