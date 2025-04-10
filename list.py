#%% Create and Print a List
# Q: Create a list of your 5 favorite fruits and print it.

fruit_list = ['orange', 'apple', 'kiwi', 'pineapple', 'sitafal']
print(fruit_list)
# %%
# ✅ 2. Access Elements by Index
# Q: Given the list colors = ['red', 'blue', 'green', 'yellow'], print the first and last elements.
colors = ['red', 'blue', 'green', 'yellow']

print(colors[0],colors[-1])

# %%
# ✅ 3. Negative Indexing
# Q: Using the colors list, access and print the second last element using negative indexing.
colors = ['red', 'blue', 'green', 'yellow']
print(colors[-2])
# %%
# ✅ 4. Slicing a List
# Q: Print the first 3 elements of numbers = [10, 20, 30, 40, 50] using slicing.
numbers = [10, 20, 30, 40, 50]
print(numbers[0:4])

# %%
# ✅ 5. Modify a List Element
# Q: Change the third element of the list names = ['Alice', 'Bob', 'Charlie'] to 'David'.
names = ['Alice', 'Bob', 'Charlie']
names[2] = 'David'
print(names)
# %%
# ✅ 6. Append an Element
# Q: Append the number 100 to the list scores = [80, 90, 70].
scores = [80, 90, 70]
scores.append(100)
print(scores)
# %%
# ✅ 7. Insert at Specific Position
# Q: Insert the value 85 at index 1 in the list marks = [90, 95, 100].

marks = [90, 95, 100]
marks[1] = 85
print(marks)
# %%
# ✅ 8. Remove a Value
# Q: Remove the value 50 from values = [10, 20, 30, 40, 50] using .remove().

values = [10, 20, 30, 40, 50]

values.remove(50)

print(values)
# %%
# ✅ 9. Remove by Index
# Q: Remove the element at index 2 from items = ['pen', 'book', 'eraser', 'pencil'] using del.

items = ['pen', 'book', 'eraser', 'pencil']
del(items[2])
print(items)
# %%
# ✅ 10. Pop the Last Element
# Q: Pop the last element from nums = [5, 10, 15, 20] and store it in a variable.
nums = [5, 10, 15, 20]
last_element = nums.pop() # default pop() removes last element
print(last_element)
# %%
# ✅ 11. Find Length
# Q: Find and print the length of the list cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata'].

cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata']
print(len(cities))
# %%
# ✅ 12. Loop Through List
# Q: Write a for-loop to print all elements in languages = ['Python', 'Java', 'C++'].

languages = ['Python', 'Java', 'C++']

# One to print items in the list
for i in languages:
    print(i)
# second way to items in list
for i in range(len(languages)):
    print(languages[i])
# %%
# ✅ 13. Check if Element Exists
# Q: Check if the value 'apple' is present in the list fruits = ['banana', 'apple', 'grapes'].

fruits = ['banana', 'grapes']

# One way to do it
if "apple" in fruits:
    print("apple is present in fruits list")
else:
    print("apple is not present in fruits list")

# second way to do it
print("apple is present in fruits list") if "apple" in fruits else print("apple is not present in fruits list")

# %%
# ✅ 14. Count Occurrences
# Q: Count how many times 7 appears in the list nums = [4, 7, 2, 7, 8, 7].

nums = [4, 7, 2, 7, 8, 7]
print(nums.count(7))
# %%
# ✅ 15. Sort a List
# Q: Sort the list ages = [45, 25, 60, 35, 20] in ascending order.
ages = [45, 25, 60, 35, 20]
ages.sort()
print(ages)

# %%
# ✅ 16. Reverse a List
# Q: Reverse the list letters = ['a', 'b', 'c', 'd'] without using slicing.

letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)
# %%
# ✅ 17. List Comprehension – Squares
# Q: Use list comprehension to create a list of squares from 1 to 10.
numbers = list(range(1,11))
#print(numbers)
#one way to do it
square_list = [i**2 for i in numbers]
print(square_list)
# second way to do it
squares = [i**2 for i in range(1,11)]
print(squares)
# %%
# ✅ 18. List Comprehension – Even Numbers
# Q: Use list comprehension to extract even numbers from numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = [i for i in numbers if ((i%2) == 0)]
print(even_num)
# %%
# ✅ 19. Join List into String
# Q: Join the list words = ['hello', 'world'] into a string with a space separator.
words = ['hello', 'world']
print(words[0] + " ", words[1])

# %%
# ✅ 20. Copy a List
# Q: Copy the list x = [1, 2, 3] to a new list y without using =, and prove they are independent.
x = [1, 2, 3]
y = x.copy()
print(id(x), id(y))
# %%
# ✅ 21. Nested List Access
# Q: Given matrix = [[1, 2], [3, 4], [5, 6]], print the value 4 using indexing.

matrix = [[1, 2], [3, 4], [5, 6]]                               #matrix = [ 1    2     
print(matrix[1][1])                                            #            3    4
                                                                #           5    6]
# %%
# ✅ 22. Flatten a Nested List
# Q: Write code to flatten nested = [[1, 2], [3, 4], [5, 6]] into [1, 2, 3, 4, 5, 6].
nested_list = [[1, 2], [3, 4], [5, 6]]
# need to use list comprehension to perform this
flatten_list = [item for item in nested_list for item in item]
print(flatten_list)

# %%
# ✅ 23. List with Mixed Types
# Q: Create a list that contains an integer, a string, a float, and a boolean.

mixed_list = [42, "hello", 3.14, True]
print(mixed_list)

# %%
# ✅ 24. Use of enumerate()
# Q: Print the index and value of each element in animals = ['cat', 'dog', 'elephant'] using enumerate
animals = ['cat', 'dog', 'elephant']

for i in enumerate(animals):
    print(i)
# %%
# ✅ 25. Remove All Duplicates
# Q: Remove all duplicate elements from the list data = [1, 2, 2, 3, 4, 4, 5] and print the new list.
data = [1, 2, 2, 3, 4, 4, 5]
# one way to remove duplicates from the list is use of set
unique_list = list(set(data))
print(unique_list)

# second way is to use for loop and append the unique numbers
unique_list = list()

for i in data:
    if i not in unique_list:
        unique_list.append(i)
    else:
        pass
print(unique_list)
# %%
# 26. Square of Even Numbers
# Q: Use list comprehension to get the square of all even numbers from 1 to 20.
number_list = list(range(1,21))

square_list = [i**2 for i in number_list if ( ( i%2 ) == 0 ) ]
print(square_list)
# %%
# 27. Extract Words with More Than 3 Letters
# Q: From words = ['hi', 'hello', 'sun', 'world', 'go'], create a new list of words that have more than 3 letters.
words = ['hi', 'hello', 'sun', 'world', 'go']

three_word_list = [i for i in words if (len(i)>3)]
print(three_word_list)
# %%
# 28. Convert List of Strings to Integers
# Q: Convert the list str_nums = ['1', '2', '3', '4'] to a list of integers using list comprehension.
str_nums = ['1', '2', '3', '4',7, 90]
# One way to do it
int_list = [int(i) for i in str_nums]
print(int_list)
# Second way to do it
int_list = [int(i) for i in str_nums if isinstance (i, (str, int) ) ]
print(int_list)
# %%
# 29. Filter and Capitalize Words
# Q: From names = ['john', 'amy', 'sara', 'ben'], use list comprehension to create a new list containing capitalized names that start with the letter 'a' or 's'.
names = ['john', 'amy', 'sara', 'ben']
capitalized_names = [i.upper() for i in names if i.startswith(('a','s')) ]
print(capitalized_names)
# %%
# 30. Flatten a 2D List
# Q: Flatten the 2D list matrix = [[1, 2], [3, 4], [5, 6]] using a nested list comprehension.
matrix = [[1, 2], [3, 4], [5, 6]]
# one way to do it via list comprehession
flatten_matrix = [item for row in matrix for item in row]
print(flatten_matrix)
#Second way to do it using normal loop
flatten_matrix_list =list()
for row in matrix:
    for item in row:
        flatten_matrix_list.append(item)
print(flatten_matrix_list)
# %%
# 31. Create a 3x3 Matrix of Zeroes
# Q: Write a list comprehension to create a 3x3 matrix filled with zeroes.
matrix = [ [0 for _ in range(3) ] for _ in range(3) ]
print(matrix)
# %%
# 32. Access Diagonal Elements of a Square Matrix
# Q: Given a 3x3 matrix, print all diagonal elements (i.e., elements at positions [0][0], [1][1], [2][2]).
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for i in range(len(matrix)):
    print(matrix[i][i])
# %%
# 33. Transpose a Matrix (Swap Rows and Columns)
# Q: Given the matrix: Use list comprehension to transpose it (columns become rows).

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
# %%
