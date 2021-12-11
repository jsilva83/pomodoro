def add(*args):
    a_sum = 0
    for a_n in args:
        a_sum += a_n
    return a_sum


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


class Car:

    def __init__(self, **kwargs):
        self.model = kwargs.get('model')    # If model is not specified the value is None.
        self.make = kwargs.get('make')      # If make key is not specified the value is None.


print(add(1, 2, 3, 4))
print(calculate(2, add=3, multiply=5))
my_car = Car(make='nissan', model='GT-R')
print(my_car.model)
