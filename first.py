#%%
print("Hello")
#%%
a=int(input("Enter a first number"))
b=int(input("Enter a second number"))
#%%
print("Addition of two numbers are", a+b)
# %%
print("Hello","World")
# %%
print(type({}))
# %%
list1=['a','b','g',1,5]
print(list1.pop)
# %%
var=2

print(2==2.0)
# %%
name = 'Hello World!'
print(name[1:5])
# %%
set1={1,5,6,4,3}

print(set1)
# %%
a='4.5'
print(int(a))
# %%
a, b = int(input('Enter two Number').split(','))
# %%
a = int(input('Enter first Number'))
b = int(input('Enter second Number'))

c=a+b

print('Sum of %d and %i is %d' %(a,b,c))
# %%
a = 15>10
print(a)
# %%
# Check Even or Odd

n = int(input("Enter a number "))

if (n%2) == 0:
    print("Number is Even")
else:
    print("Number is Odd")
# %%
# Which number is grater between two numbers

n1 = float(input("Enter first Number"))
n2 = float(input("Enter second Number"))

if n1 >= n2:
    print(f"{n1} is greater than{n2}")
else:
    print(f"{n2} is greater than {n1}")
# %%
# Palindrome Number
# One way to do it by using string
num = input("Enter the number to check for Palindrome:")
num2 = num[-1::-1] #[start:end:step]
if num == num2:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} not a palindrome number")

# Second way to do it via mathematically
num = int(input("Enter the number to check for Palindrome:"))
temp = num
string_converted = str(num)
reversed_number = 0
for i in string_converted:
    last_digit = temp % 10
    reversed_number = reversed_number * 10 + last_digit
    temp = temp // 10
print(f"{num} is a palindrome number") if num == reversed_number else print(f"{num} not a palindrome number")
    
# %%
# Armstrong Number
num = int(input("Enter the number to check for Armstrong"))
temp = num
string_converted = str(num)
count = 0

for i in string_converted:
    count += 1
raised_addition = 0
for i in string_converted:
    last_digit = temp % 10
    raised_addition += last_digit**count
    temp = temp // 10
print("Number is Armstrong") if num == raised_addition else print("Not Armstrong")  
# %%
# Nested loop
n = int(input("Enter the limit"))
for i in range(n):
    for j in range(i+1):
        print(j, end="")
    print()
# %%
