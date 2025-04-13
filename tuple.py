#%%
# 1. Create a Tuple
# Q: Create a tuple named colors with the values 'red', 'green', and 'blue'.
colors = ('red', 'green', 'blue')
print(colors, type(colors))
# %%
# 2. Access Tuple Elements
# Q: Given the tuple fruits = ('apple', 'banana', 'cherry'), print the second element.
fruits = ('apple', 'banana', 'cherry')
print(fruits[1])
# %%
# 3. Negative Indexing
# Q: Print the last element of the tuple nums = (10, 20, 30, 40) using negative indexing.
nums = (10, 20, 30, 40)
print(nums[-1])
# %%
# 4. Slicing a Tuple
# Q: Slice the tuple data = (1, 2, 3, 4, 5) to get (2, 3, 4).
data = (1, 2, 3, 4, 5)
print(data[1:len(data)-1])
# %%
# 5. Tuple with One Item
# Q: Create a tuple with a single item 'hello' and verify its type.
one_item_tuple = ("hello",)
print(type(one_item_tuple))
# %%
# 6. Check Length of Tuple
# Q: Find the length of the tuple names = ('Alice', 'Bob', 'Charlie').
names = ('Alice', 'Bob', 'Charlie')
print(len(names))
# %%
# 7. Tuple with Mixed Data Types
# Q: Create a tuple with an integer, float, string, and boolean.
mix_tuple = (10, 10.45, "Mukul", True, False)
print(mix_tuple, type(mix_tuple))
# %%
# 8. Concatenate Tuples
# Q: Join a = (1, 2) and b = (3, 4) into one tuple.
a = (1, 2)
b = (3, 4)
print(f"Combine tuples {a} and {b}:\nC = ", a + b)
# %%
# 9. Repeat Tuple Elements
# Q: Repeat the tuple t = (1, 2) three times using the * operator.
t = (1, 2)
print(t * 2)
# %%
# 10. Check if Element Exists
# Q: Check if 'python' is in the tuple langs = ('java', 'python', 'c').
langs = ('java', 'c')
if "python" in langs:
    print(f"\"python\" is present in langs tuple.")
else:
    print(f"\"python\" is not present in langs tuple.")
# %%
# 11. Count Occurrences
# Q: Count how many times 5 appears in numbers = (1, 5, 3, 5, 7, 5).
numbers = (1, 5, 3, 5, 7, 5)
print(numbers.count(5))
# %%
# 12. Find Index of Element
# Q: Find the index of 'blue' in the tuple colors = ('red', 'blue', 'green').
colors = ('red', 'blue', 'green')
print(colors.index('blue'))
# %%
# 13. Convert Tuple to List
# Q: Convert the tuple x = (1, 2, 3) to a list.
x = (1, 2, 3)
x = list(x)
print(type(x))
# %%
# 14. Convert List to Tuple
# Q: Convert the list y = [10, 20, 30] to a tuple.
y = [10, 20, 30]
y = tuple(y)
print(type(y))
# %%
# 15. Use of min() and max()
# Q: Find the minimum and maximum in the tuple scores = (66, 74, 89, 45).
scores = (66, 74, 89, 45)
print(f"Minimum score is {min(scores)} and maximum score is {max(scores)}")
# %%
# 16. Use of sum() Function
# Q: Find the sum of all elements in nums = (10, 20, 30).
nums = (10, 20, 30)
print(sum(nums))
# %%
# 17. Unpacking Tuple Values
# Q: Unpack the tuple info = ('Tom', 25, 'Engineer') into three variables.
info = ('Tom', 25, 'Engineer')
a, b, c = info
print(f"a = {a} \nb = {b} \nc = {c}")
print()
print("a = %s \nb = %i \nc = %s"%(a,b,c))
# %%
# 18. Use Tuples in a for Loop
# Q: Iterate through the tuple animals = ('dog', 'cat', 'elephant') and print each animal.
animals = ('dog', 'cat', 'elephant')
for i in animals:
    print(i)
# %%
# 19. Nested Tuple Access
# Q: Given nested = ((1, 2), (3, 4), (5, 6)), access the value 4.
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][1])
# %%
# 20. Tuple Inside List
# Q: Given data = [(1, 2), (3, 4), (5, 6)], print the second element of the first tuple.
data = [(1, 2), (3, 4), (5, 6)]
print(data[0][1])
# %%
# 21. List Inside Tuple
# Q: Create a tuple that contains a list, then modify the list element inside the tuple.
colors = ('red', 'blue', 'green', [1,3,4])
colors[3][2] = 6
print(colors)
# %%
# 22. Tuple as Dictionary Key
# Q: Create a dictionary with tuple keys. Example: {('a', 'b'): 1, ('c', 'd'): 2}.
# 23. Sort a Tuple (Workaround)
# Q: Sort the tuple t = (4, 1, 3, 2) in ascending order.
t = (4, 1, 3, 2)
t = tuple(sorted(t))
print(t)
# %%
# 24. Swap Variables Using Tuple
# Q: Swap the values of two variables a = 5 and b = 10 using a tuple.
a = 5
b = 10
t = (b,a)
print(t, type(t))
# %%
# 25. Tuple Immutability Test
# Q: Try modifying the tuple t = (1, 2, 3) at index 1. What happens?
t = (1, 2, 3)
t[1] = 8 # This will throw an error saying tuple does not allow assignment operations

# %%
