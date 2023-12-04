# Decorator
def my_decorator(func):
    def wrap_func():
        print("*********")
        func()
        print("*********")
        return wrap_func


@my_decorator
def hello():
    print("helloooooo")


@my_decorator
def bye():
    print("see ya later")
