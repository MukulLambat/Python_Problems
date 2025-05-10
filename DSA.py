#%% Find the lowest value in a array
my_array = [7, 12, 9, 44, 11]

lowest_num = my_array[0]
for i in my_array:
    if i < lowest_num:
        lowest_num = i
print(f"The lowest number in the arrary is {lowest_num}")
# %%
