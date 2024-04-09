'''def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
'''


'''How would you modify the code for the decorator function to remove unneeded
messages and enclose the return value of the wrapped function in "<html>" and "
</html>", so that myfunction ("hello") would return "<html>hello<html>"?
'''
'''>>> def decorate(func):
... print("in decorate function, decorating", func.__name__) 1
... def wrapper_func(*args):
... print("Executing", func.__name__)
... return func(*args)
... return wrapper_func 2
...
>>> @decorate 3
... def myfunction(parameter):
... print(parameter)
...
in decorate function, decorating myfunction 4
>>> myfunction("hello")
Executing myfunction
hello
'''

def decorate(func):
    def wrapper_func(*args):
        print('<html>',end='')
        func(*args)
        print('</html>')
    return wrapper_func

@decorate
def myfunction(parameter):
    print(parameter,end="")

myfunction("Hello")

    
