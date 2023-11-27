# List, set, dictionary

# List Comprehensions
my_list = [char for char in "hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list4)

# Sets Comprehensions
my_set = {char for char in "hello"}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num**2 for num in range(0, 100)}
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}
# print(my_set4)

# Dictionary Comprehensions
simple_dict = {
    "a": 1,
    "b": 2,
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}

print(my_dict)
