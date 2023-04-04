# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x.upper()
    return inner
@decor1
def f():
    return "Hello"
print(f())
