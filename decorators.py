# Decorator
from time import time

# def my_decorator(func):
#     def wrap_func():
#         print("*********")
#         func()
#         print("*********")
#         return wrap_func
#
#
# @my_decorator
# def hello():
#     print("helloooooo")
#
#
# @my_decorator
# def bye():
#     print("see ya later")
#


# Conta quanto tempo demorou para executar uma função.
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Demorou {t2 - t1}s")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000):
        i * 5


long_time()
