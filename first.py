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
