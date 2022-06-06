class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def square(self):
        return self.a * self.b

timmy = Calculation(5, 8)
print(timmy.square())
print(timmy.add())

#timmy is a certain instance to have specific attribute a=5, b=8, maybe you have other instance jim, oliver etc...
#encapslute all operation/attribute in in class Calculation, just call method() to get what you want
