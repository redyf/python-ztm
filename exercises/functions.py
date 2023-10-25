# Exercise: Print highest even number


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([2, 5, 3, 72, 6, 3, 23, 1, 423, 10, 54, 29]))
