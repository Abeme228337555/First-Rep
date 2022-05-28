
import colorama


def first_function():
    pass


class Human:
    pass


rq = colorama
first_f = first_function
nick = Human

print(colorama.__name__)
print(rq.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)
print('-------------------')
my_int = 0
my_fl = 0.1
my_str = 'hi'
my_b = True
print(type(my_int))
print(type(my_fl))
print(type(my_str))
print(type(my_b))
print(type(colorama))
print(type(rq))
print(type(first_function))
print(type(first_f))
print(type(Human))
print(type(nick))
print('-------------------')
my_list = []
for method in dir(my_list):
    print(method)
print('-------------------')
data = 'string'
print(hasattr(data, 'reverse'))
print(hasattr(data, 'index'))

print(getattr(data, 'startswith'))
print(getattr(data, 'startswith', None))
print(getattr(data, 'reverse', None))
print('-------------------')
data = 'string'


def func():
    pass


print(callable(data))
print(callable(func))
print('-------------------')
class Class1:
    pass

class Class2(Class1):
    pass


print(issubclass(Class1, Class2))
print(issubclass(Class2, Class1))
print('-------------------')
obj2 = Class2()

print(isinstance(obj2, Class1))
print(isinstance(obj2, Class2))
print('-------------------')
import inspect

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(list))
print('-------------------')
import sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
