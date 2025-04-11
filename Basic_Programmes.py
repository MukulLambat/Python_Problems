
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

#%% Factorial of a Number
# Write a program that asks for a positive integer and computes its factorial.
# Fibonacci Series
# Write a program that generates and prints the Fibonacci sequence up to n terms (where n is input by the user).
# Swap Two Variables
# Write a program that swaps the values of two variables without using a temporary variable.
# Reverse a String
# Write a program that reverses a given string.
# Check Palindrome (String)
# Write a program to check if a given string is a palindrome (reads the same forwards and backwards).
# Armstrong Number
# Write a program that checks if a given number is an Armstrong (Narcissistic) number.
# Check Prime Number
# Write a program that determines if a given number is prime.
# Find the Largest Among Three Numbers
# Write a program that takes three numbers and prints which one is the largest.
# Sum of Digits of a Number
# Write a program that calculates the sum of all digits of a given number.
# Check Leap Year
# Write a program that checks if a given year is a leap year.
# ASCII Value of a Character
# Write a program that takes a single character and displays its ASCII (or Unicode) value.
# Guess the Number (Simple Game)
# Write a simple game where the user guesses a secret number (hardcode the secret number in your program).
# Multiplication Table
# Write a program that prints the multiplication table of a chosen number up to 10 terms.
# Simple List Operations
# Write a program that demonstrates basic operations on a list: creating, appending items, accessing elements, and removing items.
# Read and Write to a File
# Write a program that writes some text to a file, then reads and prints that file’s content.
# Dictionary Usage
# Write a program that creates a dictionary with some initial key-value pairs, prints specific values by key, updates an existing value, and adds a new key-value pair.
# Simple Calculator (Using If-Else)
# Write a program that takes two numbers and an operator (+, -, *, /) from the user, then performs the corresponding calculation.
# Counting Vowels in a String
# Write a program that counts and displays the number of vowels in a user-provided string.
# Rock, Paper, Scissors
# Write a simple Rock-Paper-Scissors game where the user plays against the computer (use random choice for the computer).
# Finding the Longest Word in a Sentence
# Write a program that takes a sentence from the user, splits it into words, and prints the longest word.

# %%
