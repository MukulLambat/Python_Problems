#%% 1. Create a lambda function that adds 10 to a number
# 📌 Input: 5 → Output: 15
x = lambda a : a + 10
print(x(5.02))
# %% 2. Write a lambda function to multiply two numbers
# 📌 Input: (3, 4) → Output: 12

x = lambda x, y : x * y
print(x(5,5))
# %% 3. Use a lambda to check if a number is even
# 📌 Input: 6 → Output: True

a = lambda b : print(f'{b} is even')if (b % 2) == 0 \
                                    else print(f'{b} is not even')
# %% 4. Write a lambda that returns the square of a number
# 📌 Input: 7 → Output: 49
a = lambda b : b ** 2
a(6)
# %% 5. Create a lambda that returns the maximum of two numbers
# 📌 Input: (9, 5) → Output: 9
my_max = lambda a, b : print(f"{a} is greater number") if (a > b) \
                       else print(f"{b} is greater number")                
my_max(9,5)
# %% 6. Use map with lambda to square each number in a list
# 📌 Input: [1, 2, 3] → Output: [1, 4, 9]
input_list = [10, 20, 30]
square_each = list(map(lambda x: x ** 2, input_list))
print(square_each)
# %% 7. Convert all words in a list to uppercase using map and lambda
# 📌 Input: ['hi', 'hello'] → Output: ['HI', 'HELLO']
Input_list = ['hi', 'hello']
upper_list = list(map(lambda x : x.upper(), Input_list))
# %% 8. Add 5 to every element in a list using lambda and map
# 📌 Input: [10, 20] → Output: [15, 25]
Input_list = [10, 20]
add_five = list(map(lambda d : d + 5, Input_list))
print(add_five)
# %% 9. Use map and lambda to convert list of floats to integers
# 📌 Input: [1.2, 3.7, 4.6] → Output: [1, 3, 4]
Input_list = [1.2, 3.7, 4.6]
float_list = list(map(lambda d : int(d), Input_list))
print(float_list)
# %% 10. Multiply corresponding elements of two lists using map and lambda
# 📌 Input: [1,2,3], [4,5,6] → Output: [4,10,18]
Input_list_1 = [1,2,3] 
Input_list_2 = [4,5,6]
mul_list = list(map(lambda d,b : d * b, Input_list_1, Input_list_2))
print(mul_list)
# %% 11. Use filter and lambda to keep only even numbers
# 📌 Input: [1, 2, 3, 4] → Output: [2, 4]
Input_list = [1, 2, 3, 4]
even_list = list(filter(lambda x : x % 2 == 0, Input_list))
print(even_list)
# %% 12. Use filter and lambda to remove empty strings from a list
# 📌 Input: ['hi', '', 'hello', ''] → Output: ['hi', 'hello']
Input_list = ['hi', '', 'hello', '']
empty_str_list = list(filter(lambda x : x != '', Input_list))
print(empty_str_list)
# %% 13. Keep only words longer than 3 letters using filter and lambda
# 📌 Input: ['hi', 'world', 'go'] → Output: ['world']
Input_list = ['hi', 'world', 'go']
long_3_list = list(filter(lambda x : len(x) > 3, Input_list))
print(long_3_list)
# %% 14. Use filter to find numbers greater than 10
# 📌 Input: [4, 12, 9, 20] → Output: [12, 20]
Input_list = [4, 12, 9, 20, 25, 10.5, 20.02]
great_num_list = list(filter(lambda x : x >= 20, Input_list))
print(great_num_list)
# %% 15. Filter out negative numbers from a list
# 📌 Input: [-2, 3, -5, 6] → Output: [3, 6]
Input_list = [-2, 3, -5, 6]
great_zero_list = list(filter(lambda x : x >= 0, Input_list))
print(great_zero_list)
# %% 16. Sort a list of tuples based on the second item using lambda
# 📌 Input: [(1, 2), (3, 1)] → Output: [(3, 1), (1, 2)]
Input_tuple_list = [(1, 2), (3, 1)]
sorted_data = sorted(Input_tuple_list, key=lambda x: x[1])
print(sorted_data)
# %% 17. Sort strings by length using sorted() and lambda
# 📌 Input: ['hi', 'hello', 'go'] → Output: ['hi', 'go', 'hello']
Input_list = ['hi', 'hello', 'go']
sorted_data = sorted(Input_list, key = lambda x : len(x))
print(sorted_data)
# %% 18. Find the longest word in a list using max() and lambda
# 📌 Input: ['hi', 'world', 'amazing'] → Output: 'amazing'
Input_list = ['hi', 'world', 'amazing']
longest_data = max(Input_list, key = lambda x : len(x))
print(longest_data)
# %% 19. Find the tuple with the highest second value using max()
# 📌 Input: [(1, 10), (2, 30)] → Output: (2, 30)
Input_list = [(1, 10), (2, 30)]
max_data = max(Input_list, key = lambda x : x[1])
print(max_data)
# %% 20. Sort list of dictionaries by value of key 'age' using lambda
# 📌 Input: [{'name': 'A', 'age': 25}, {'name': 'B', 'age': 20}] → Output: sorted by age
Input_list = [{'name': 'A', 'age': 25}, {'name': 'B', 'age': 20}]
sorted_by_age = sorted(Input_list, key = lambda x : x['age']) 
print(sorted_by_age)
# %% 21. Use a lambda inside a reduce() to calculate product of list
# 📌 Input: [1, 2, 3, 4] → Output: 24
Input_list = [1, 2, 3, 4]
import functools as fn
product_list = fn.reduce(lambda x, y : x * y, Input_list)
print(product_list)
# %% 22. Write a lambda to return "Even" or "Odd" for a given number
a = lambda x: print(f"{x} is even") if x % 2 == 0 else print(f'{x} is odd')
a(8)
# %% 23. Use lambda to create a function that checks if a string starts with 'A'
a = lambda x: x.startswith('A')
a('Askdf')
# %% 24. Use lambda to return the second last element of any list
Input_list = [1, 2, 3, 4]
a = lambda x : x[-2]
print(a(Input_list))