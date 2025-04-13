#%%
# 1. Create a Set
# Create a set of 5 different fruits.
fruits = {"orange", "apple", "banana", "grapes", "mango"}
print(type(fruits))
# %%
# 2. Check Type of Set
# Verify the type of x = {1, 2, 3} using the type() function.
x = {1, 2, 3}
print(type(x))
# %%
# 3. Set with Mixed Data Types
# Create a set that includes an integer, float, string, and boolean.
s = {"mukul", 45, 14.04, True, False}
print(s)
# %%
# 4. Add Element to Set
# Add 'apple' to the set fruits = {'banana', 'cherry'}.
fruits = {'banana', 'cherry'}
fruits.add("apple")
print(fruits)
# %%
# 5. Add Multiple Elements
# Add multiple elements to a set using update().
fruits = {'banana', 'cherry'}
fruits.update(["apple","grapes"])
print(fruits)
# %%
# 6. Length of Set
# Find the number of items in the set nums = {1, 2, 3, 4}.
nums = {1, 2, 3, 4}
print(len(nums))
# %%
# 7. Check Element Exists
# Check if 'blue' is present in the set colors = {'red', 'green', 'blue'}.
colors = {'red', 'green', 'blue'}
print("blue" not in colors)
# %%
# 8. Remove an Element
# Remove the element 'banana' from a set using remove().
fruits = {'banana', 'cherry'}
fruits.remove("banana")
print(fruits)
# %%
# 9. Discard an Element
# Discard an element that may or may not exist from a set using discard().
fruits = {'banana', 'cherry'}
fruits.discard("banana")
fruits.discard("apple")
print(fruits)
# %%
# 10. Pop Element
# Use pop() to remove an arbitrary element from a set and print it.
fruits = {'banana', 'cherry'}
fruits.pop()
print(fruits)
# %%
# 11. Set Union
# Perform union of a = {1, 2} and b = {2, 3}.
a = {1, 2}
b = {2, 3}
print(a.union(b))
# %%
# 12. Set Intersection
# Find common elements between a = {1, 2, 3} and b = {2, 3, 4}.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))
# %%
# 13. Set Difference
# Find elements in a = {1, 2, 3} but not in b = {2, 4}.
a = {1, 2, 3}
b = {2, 4}
print(a.difference(b))
print(b.difference(a))
# %%
# 14. Symmetric Difference
# Find elements in either set a or b, but not both.
a = {1, 2, 3}
b = {2, 4}
print(a.symmetric_difference(b))
# %%
# 15. Is Subset
# Check if a = {1, 2} is a subset of b = {1, 2, 3}.
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
# %%
# 16. Is Superset
# Check if b = {1, 2, 3} is a superset of a = {2, 3}.
b = {1, 2, 3}
a = {2, 3}
print(b.issuperset(a)) 
# %%
# 17. Is Disjoint
# Check if a = {1, 2} and b = {3, 4} are disjoint.
a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))
# %%
# 18. Clear a Set
# Remove all elements from the set x = {1, 2, 3} using clear().
x = {1, 2, 3}
x.clear()
print(x)
# %%
# 19. Copy a Set
# Make a shallow copy of a set original = {1, 2, 3}.
original = {1, 2, 3}
copy_original = original.copy()
print(original,"\n",copy_original)
# %%
# 20. Use in and not in Operators
# Check if 5 is in nums = {1, 2, 5, 6} and if 3 is not.
nums = {1, 2, 5, 6}
print(5 in nums and not 3)
# %%
# 21. Length After Set Operations
# What’s the length of set1 | set2 if set1 = {1, 2, 3} and set2 = {3, 4}?
set1 = {1, 2, 3}
set2 = {3, 4}
set3 = set1.union(set2)
print(len(set3))
# %%
# 22. Convert List to Set
# Convert [1, 2, 3, 3, 2, 1] to a set and remove duplicates.
list1 = [1, 2, 3, 3, 2, 1]
set_list = set(list1)
print(set_list)
# %%
# 23. Convert Set to List
# Convert the set {10, 20, 30} to a list.
set1 = {10, 20, 30}
list_set = list(set1)
print(list_set,type(list_set))
# %%
# 24. Set of Characters in String
# Create a set of unique characters from the string "hello".
s = 'hello'
s_set = set(s)
print(s_set)
# %%
# 25. Set from String List
# Create a set of lowercase words from ['Apple', 'Banana', 'apple'].
fruits = ['Apple', 'Banana', 'apple']
fruits_lower = [] 
for items in fruits:
    a = items.lower()
    fruits_lower.append(a)
fruits_set = set(fruits_lower)
print(fruits_set)
# %%
# 26. Set of Squares
# Use set comprehension to create a set of squares from 1 to 10.
square_set = {i**2 for i in range(1,11)}
print(square_set)
# %%
# 27. Filter Even Numbers
# Use set comprehension to extract even numbers from a range of 1 to 20.
even_set = {i for i in range(1, 21) if i%2 == 0}
print(even_set)
# %%
# 28. Common Letters in Two Words
# Find common letters in "python" and "notebook" using set operations.
letter_set1 = {i for i in "python" if i in "notebook"} # one way
letter_set2 = {i for i in "python" for j in "notebook" if i == j} # second way
print(letter_set1)
print(letter_set2)
# %%
# 29. Letters in First but Not in Second
# Find letters in "computer" but not in "science".
letter_set = {i for i in "computer" if i not in "science"}
print(letter_set)
# %%
# 30. Symmetric Difference of Words
# Find unique letters in "python" and "typhoon" using symmetric difference.
set1 = set("python")
set2 = set("typhoon")
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)
# %%
# 31. Remove Duplicates from List
# Remove duplicates from nums = [1, 2, 2, 3, 4, 4] using a set.
nums = [1, 2, 2, 3, 4, 4]
nums_set = set(nums)
print(nums_set)
# %%
# 32. Count Unique Words in Sentence
# Count unique words in "this is a test this is only a test".
s = "this is a test this is only a test"
s_set = {word for word in s.split()}
print(len(s_set))
# %%
# 33. Find Common Students in Two Classes
# Given classA = {'Sam', 'John'} and classB = {'John', 'Emma'}, find common students.
classA = {'Sam', 'John'}
classB = {'John', 'Emma'}
print(classA.union(classB))
# %%
