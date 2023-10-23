# Tuple
my_tuple = (1, 2, 3, 4, 5, 5)
print(5 in my_tuple)
user = {(1, 2): [1, 2, 3], "greet": "hello", "age": 20}

print(user[(1, 2)])

x, y, z, *other = (1, 2, 3, 4, 5)

print(other)

print(my_tuple.index(5))
print(len(my_tuple))
