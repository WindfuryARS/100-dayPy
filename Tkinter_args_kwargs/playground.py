def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def cal(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['b'])
    for key, value in kwargs.items():
        print(key, value)


cal(a=1, b=2)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Ford", model="Mustang")
print(my_car.make)
print(my_car.model)