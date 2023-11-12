from functools import reduce

# Map, filter, zip and reduce
# Relacionado a programação funcional por resultar em uma função pura que não afeta o escopo global do código, e sim da funcão apenas.
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]


def multiply_by2(item):
    return item * 2


# print(list(map(multiply_by2, my_list)))
# print(my_list)


# Filter
def only_odd(item):
    return item % 2 != 0


# print(list(filter(only_odd, my_list)))
# print(my_list)

# Zip (Pega o primeiro iterável de cada lista e "zipa" eles juntos.)
# print(
#     list(zip(my_list, your_list, their_list))
# )  # Output: [(1, 10, 5), (2, 20, 4), (3,30, 3)]


# Reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print((reduce(accumulator, my_list, 0)))
print(my_list)
